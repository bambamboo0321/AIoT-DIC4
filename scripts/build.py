#!/usr/bin/env python3
"""Build a snapshot and independently compile its source-only Overleaf ZIP."""
import argparse, hashlib, json, os, pathlib, re, shutil, subprocess, tempfile, zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]

def run(args,cwd,env):
    r=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True)
    if r.returncode:
        print((r.stdout+r.stderr)[-7000:])
        raise SystemExit(r.returncode)
    return r.stdout+r.stderr

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def build(source,work,env):
    shutil.copytree(source,work)
    run(['latexmk','-g','-pdf','-interaction=nonstopmode','-halt-on-error','-file-line-error','main.tex'],work,env)
    log=(work/'main.log').read_text(errors='replace')
    pathlib.Path('/private/tmp/smartintake-last-build.log').write_text(log)
    errors=[line for line in log.splitlines() if re.search(r'Overfull \\[hv]box|Citation .*undefined|Reference .*undefined|There were undefined|LaTeX Error|! ',line)]
    if errors: raise RuntimeError('\n'.join(errors))
    return log

def main():
    ap=argparse.ArgumentParser();ap.add_argument('version',choices=['v1','v2','v3']);args=ap.parse_args()
    version=args.version;stage={'v1':'initial','v2':'revised','v3':'refined'}[version]
    source=ROOT/'paper'/f'{version}-{stage}'
    env=dict(os.environ)
    if env.get('SMARTINTAKE_TEXBIN'): env['PATH']=env['SMARTINTAKE_TEXBIN']+':'+env['PATH']
    for tool in ['latexmk','bibtex','pdfinfo','pdftotext']:
        if not shutil.which(tool,path=env['PATH']): raise SystemExit(f'Missing required tool: {tool}')
    output=ROOT/'deliverables';output.mkdir(exist_ok=True)
    archive=output/f'Overleaf_{version.upper()}.zip'
    names=[]
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(source.rglob('*')):
            if p.is_file() and (p.suffix in ['.tex','.bib'] or p.name=='README.md'):
                name=p.relative_to(source).as_posix();names.append(name);z.write(p,name)
    with tempfile.TemporaryDirectory(prefix='smartintake-build-') as temp:
        temp=pathlib.Path(temp);log=build(source,temp/'source',env)
        pdf=output/f'SmartIntake_{version.upper()}_{stage.title()}.pdf';shutil.copy2(temp/'source/main.pdf',pdf)
        extracted=temp/'extracted';extracted.mkdir()
        with zipfile.ZipFile(archive) as z: z.extractall(extracted)
        zlog=build(extracted,temp/'zip-build',env)
        src_text=run(['pdftotext','-layout',str(pdf),'-'],ROOT,env)
        zip_text=run(['pdftotext','-layout',str(temp/'zip-build/main.pdf'),'-'],ROOT,env)
        if src_text!=zip_text: raise RuntimeError('Extracted ZIP PDF text differs from source build')
        info=run(['pdfinfo',str(pdf)],ROOT,env)
        source_hashes={p.relative_to(source).as_posix():digest(p) for p in sorted(source.rglob('*')) if p.is_file()}
        report={'version':version,'build_command':'latexmk -g -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex','source_build_exit':0,'independent_zip_build_exit':0,'resolved_citations_and_references':True,'overfull_boxes':0,'source_zip_pdf_text_equal':True,'zip_members':names,'source_hashes':source_hashes,'artifacts':{str(p.relative_to(ROOT)):digest(p) for p in [pdf,archive]},'pdfinfo':info.splitlines(),'visual_inspection':'pending; record separately after rendering','scope':'Build results, not E1-E5 research measurements'}
        # Remove host-dependent metadata; artifact paths are repository-relative.
        (ROOT/f'docs/validation/{version}-build.json').write_text(json.dumps(report,indent=2)+'\n')
        pathlib.Path(f'/private/tmp/smartintake-{version}-final.log').write_text(log)
        print(json.dumps({'pdf':str(pdf.relative_to(ROOT)),'zip':str(archive.relative_to(ROOT)),'source_and_zip_builds':'passed','pages':re.search(r'Pages:\s+(\d+)',info).group(1),'sha256':digest(pdf)}))
if __name__=='__main__': main()
