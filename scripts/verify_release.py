#!/usr/bin/env python3
"""Check frozen artifacts, packaging, PDF readability, specs and secret patterns."""
import hashlib,json,os,pathlib,re,subprocess,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
checks=[]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def check(ok,message):
    if not ok: raise SystemExit('FAIL: '+message)
    checks.append(message)
for version,stage in [('v1','initial'),('v2','revised')]:
    manifest=json.loads((ROOT/f'docs/validation/{version}-build.json').read_text());source=ROOT/f'paper/{version}-{stage}'
    actual={p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}
    check(actual==set(manifest['source_hashes']),f'{version} exact source file set')
    for name,expected in manifest['source_hashes'].items():check(digest(source/name)==expected,f'{version} source hash {name}')
    for name,expected in manifest['artifacts'].items():check(digest(ROOT/name)==expected,f'artifact hash {name}')
    with zipfile.ZipFile(ROOT/f'deliverables/Overleaf_{version.upper()}.zip') as z:
        check(z.testzip() is None,f'{version} ZIP integrity')
        check(sorted(z.namelist())==sorted(manifest['zip_members']),f'{version} ZIP exact members')
        for name in z.namelist():
            check(not name.startswith('/') and '..' not in pathlib.PurePosixPath(name).parts,f'{version} safe ZIP path {name}')
            check(z.read(name)==(source/name).read_bytes(),f'{version} ZIP/source equality {name}')
record=json.loads((ROOT/'docs/validation/v1-v2-diff.json').read_text())
for name,expected in record['artifacts'].items():check(digest(ROOT/'deliverables'/name)==expected,'difference artifact hash '+name)
for name in ['SmartIntake_V1_Initial.pdf','SmartIntake_V2_Revised.pdf','SmartIntake_V1_V2_Diff.pdf']:
    p=ROOT/'deliverables'/name
    r=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True)
    check(r.returncode==0 and int(re.search(r'Pages:\s+(\d+)',r.stdout).group(1))>0,'readable PDF '+name)
    fonts=subprocess.run(['pdffonts',str(p)],capture_output=True,text=True,check=True).stdout.splitlines()[2:]
    check(bool(fonts) and all(re.search(r'\byes\s+yes\s+(?:yes|no)\s+\d+\s+\d+$',line) for line in fonts),'embedded subset fonts '+name)
# No values are printed on a failed match. Public scholarly names/identifiers are intentional citation metadata.
patterns=[r'gh[pousr]_[A-Za-z0-9]{20,}',r'github_pat_[A-Za-z0-9_]{30,}',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'AKIA[0-9A-Z]{16}',r'https://[^/\s]+:[^@\s]+@']
files=subprocess.run(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT,capture_output=True,check=True).stdout.decode().split('\0')
scanned=0
for name in sorted(set(files)-{''}):
    p=ROOT/name
    if p.exists() and p.suffix in ['.md','.tex','.bib','.py','.yaml','.json','.diff']:
        text=p.read_text(errors='replace');check(not any(re.search(pattern,text) for pattern in patterns),'no secret pattern '+name);scanned+=1
cli=os.environ.get('SMARTINTAKE_OPENSPEC','openspec')
for args in [['validate','--all','--strict','--json','--no-interactive'],['validate','--archived','--json','--no-interactive']]:
    r=subprocess.run([cli,*args],cwd=ROOT,env=dict(os.environ,OPENSPEC_TELEMETRY='0'),capture_output=True,text=True)
    check(r.returncode==0,'OpenSpec '+' '.join(args))
for change in ['2026-11-25-initialize-ieee-paper','2026-11-25-revise-ieee-conference-paper']:
    d=ROOT/'openspec/changes/archive'/change
    for name in ['goal.md','proposal.md','design.md','tasks.md']:
        check((d/name).is_file(),'archived course artifact '+change+'/'+name)
    check('- [ ]' not in (d/'tasks.md').read_text(),'completed archive task list '+change)
result={'checks_passed':len(checks),'checks':checks,'secret_scan_text_files':scanned,'manual_review_required':'Source meaning, citations and visual quality are attested in version reports; this script cannot prove absence of all sensitive data or research validity.','research_results':'E1-E5 pending; no measured research data generated','overleaf':'No live MCP/service verification; local ZIP compilation recorded separately'}
(ROOT/'docs/validation/final-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks_passed':len(checks),'secret_scan_text_files':scanned,'result':'passed'}))
