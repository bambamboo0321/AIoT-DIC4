#!/usr/bin/env python3
"""Produce a genuine flattened latexdiff and a source-level unified comparison."""
import difflib, hashlib, json, os, pathlib, re, shutil, subprocess, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
env=dict(os.environ)
if env.get('SMARTINTAKE_TEXBIN'): env['PATH']=env['SMARTINTAKE_TEXBIN']+':'+env['PATH']
old=ROOT/'paper/v1-initial';new=ROOT/'paper/v2-revised';out=ROOT/'deliverables'
with tempfile.TemporaryDirectory(prefix='smartintake-bibliographies-') as temp:
    base=pathlib.Path(temp)
    for name,source_dir in [('old',old),('new',new)]:
        target=base/name;shutil.copytree(source_dir,target)
        prep=subprocess.run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=target,env=env,capture_output=True,text=True)
        if prep.returncode: raise SystemExit((prep.stdout+prep.stderr)[-3000:])
        bbl=target/'main.bbl'
        bbl.write_text(bbl.read_text().replace(r'\csname url@samestyle\endcsname',r'\urlstyle{same}'))
        preamble=target/'preamble.tex'
        preamble.write_text(preamble.read_text()+r'\newenvironment{DIFnomarkup}{}{}'+'\n')
        if name=='new':
            method=target/'sections/method.tex'
            method.write_text(method.read_text().replace(r'\input{figures/states}',r'\begin{DIFnomarkup}\begingroup\color{blue}\input{figures/states}\endgroup\end{DIFnomarkup}'))
            states=target/'figures/states.tex'
            states.write_text(states.read_text().replace(r'\begin{table*}[t]',r'\begin{table*}[t]\color{blue}'))
    r=subprocess.run(['latexdiff','--flatten','--type=CFONT','--math-markup=whole','--graphics-markup=none',str(base/'old/main.tex'),str(base/'new/main.tex')],env=env,capture_output=True,text=True,cwd=base)
    r.stdout=r.stdout.replace(str(base/'old'),'paper/v1-initial').replace(str(base/'new'),'paper/v2-revised')
if r.returncode: raise SystemExit(r.stderr)
source=out/'SmartIntake_V1_V2_Diff.tex'
# Preserve all diff content; make CFONT deletion styling valid in math and hyphenate a long table label.
markup=r.stdout.replace(r'\color{red} \scriptsize #1',r'\color{red} \ifmmode #1\else\scriptsize #1\fi')
markup=markup.replace(r'\begin{document}',r'\hyphenation{Tool-for-mer}'+ '\n' + r'\begin{document}')
source.write_text(markup)
warning=r.stderr.strip().replace(str(ROOT),'<repository>').replace('/private/tmp/smartintake-tools','<toolchain>')
with tempfile.TemporaryDirectory(prefix='smartintake-diff-') as tmp:
    tmp=pathlib.Path(tmp);shutil.copy2(source,tmp/'main.tex');shutil.copy2(new/'references.bib',tmp/'references.bib')
    r=subprocess.run(['latexmk','-g','-pdf','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=tmp,env=env,capture_output=True,text=True)
    pathlib.Path('/private/tmp/smartintake-diff-output.txt').write_text(r.stdout+r.stderr)
    if r.returncode:
        print((r.stdout+r.stderr)[-5000:]);raise SystemExit(r.returncode)
    log=(tmp/'main.log').read_text(errors='replace');pathlib.Path('/private/tmp/smartintake-diff.log').write_text(log)
    bad=[x for x in log.splitlines() if re.search(r'Overfull \\[hv]box|Citation .*undefined|Reference .*undefined|There were undefined|LaTeX Error',x)]
    if bad: print('\n'.join(bad));raise SystemExit(1)
    pdf=out/'SmartIntake_V1_V2_Diff.pdf';shutil.copy2(tmp/'main.pdf',pdf)
    info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
names=sorted({p.relative_to(base).as_posix() for base in [old,new] for p in base.rglob('*') if p.is_file()})
diff=[];changed=[]
for n in names:
    a=(old/n).read_text().splitlines(True) if (old/n).exists() else []
    b=(new/n).read_text().splitlines(True) if (new/n).exists() else []
    if a!=b:
        changed.append(n);diff.extend(difflib.unified_diff(a,b,fromfile='paper/v1-initial/'+n,tofile='paper/v2-revised/'+n))
(out/'V1_V2_source.diff').write_text(''.join(diff))
record={'command':'latexdiff --flatten --type=CFONT --math-markup=whole --graphics-markup=none paper/v1-initial/main.tex paper/v2-revised/main.tex','latexdiff_exit':0,'latexmk_exit':0,'bibliography_flattened':True,'style_adjustments':'Equivalent IEEE bibliography URL-font setup, math-safe CFONT deletion font and Toolformer hyphenation; newly introduced lifecycle table rendered as one intact blue block to prevent cross-table token alignment. No changed content removed.','markup':'CFONT: added text blue, removed text red (smaller in prose; normal math size); not a clean manuscript','warning':warning,'overfull_boxes':0,'changed_paths':changed,'pdf_pages':int(re.search(r'Pages:\s+(\d+)',info).group(1)),'artifacts':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [source,pdf,out/'V1_V2_source.diff']},'visual_inspection':'pending; see version validation report'}
(ROOT/'docs/validation/v1-v2-diff.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'diff_build':'passed','pages':record['pdf_pages'],'changed_source_paths':len(changed),'warning':warning}))
