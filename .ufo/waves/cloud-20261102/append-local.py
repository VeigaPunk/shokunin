#!/usr/bin/env python3
"""Cloud operator append wrapper. Preserves original validator and exact ledger prefix.
No push, ref movement or credentials. Exit0 verified/applied;1 refused;2 usage/error.
Use --selftest for isolated negative controls. Original jj helper remains unchanged.
"""
import argparse,fcntl,hashlib,json,os,pathlib,runpy,tempfile
DUMP=dict(indent=1,ensure_ascii=False,separators=(',', ': '))
def prepare(raw, entry):
    doc=json.loads(raw); nl=raw.endswith(b'\n')
    if (json.dumps(doc,**DUMP)+('\n' if nl else '')).encode()!=raw: raise ValueError('serialization_mismatch')
    old=doc['rounds']
    if any(r.get('campaign')=='hyaku' and r.get('lane')==entry['lane'] and r.get('lane_round')==entry['lane_round'] and r.get('type')==entry['type']=='closure' for r in old): raise ValueError('duplicate_closure')
    doc['rounds']=old+[entry]; out=(json.dumps(doc,**DUMP)+('\n' if nl else '')).encode()
    if json.loads(out)['rounds'][:-1]!=old or not out.startswith(raw.rstrip(b'\n')[:-len(b'\n ]\n}')]):raise ValueError('history_changed')
    return out,len(old)
def selftest():
    base={'roster':[{'id':'x'}],'rounds':[{'round':1,'value':'immutable'}]}; raw=(json.dumps(base,**DUMP)+'\n').encode()
    e={'campaign':'hyaku','lane':'x','lane_round':2,'type':'closure'}
    out,n=prepare(raw,e); assert n==1 and json.loads(out)['rounds'][0]==base['rounds'][0]
    for payload,entry,want in [(out,e,'duplicate_closure'),(json.dumps(base).encode(),e,'serialization_mismatch')]:
        try:prepare(payload,entry)
        except ValueError as ex: assert str(ex)==want
        else:raise AssertionError('negative_control_survived')
    print('selftest clean=1 negative=2 pass');return
p=argparse.ArgumentParser();p.add_argument('--root');p.add_argument('--entry');p.add_argument('--expected-manifest-sha');p.add_argument('--apply',action='store_true');p.add_argument('--selftest',action='store_true');a=p.parse_args()
if a.selftest:selftest();raise SystemExit(0)
if not all((a.root,a.entry,a.expected_manifest_sha)):p.error('root, entry and expected-manifest-sha required')
r=pathlib.Path(a.root).resolve();os.environ['SHOKUNIN_ROOT']=str(r)
mod=runpy.run_path(str(r/'scripts/hyaku/append-closure.py'),run_name='closure_validation_only')
e=json.loads(pathlib.Path(a.entry).read_text());mod['validate'](e)
with open(r/'.git/cloud-closure.lock','w') as lock:
    fcntl.flock(lock,fcntl.LOCK_EX); path=r/'MANIFEST.json';raw=path.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=a.expected_manifest_sha:raise ValueError('concurrent_manifest_change')
    out,index=prepare(raw,e)
    receipt={'index':index,'lane':e['lane'],'round':e['lane_round'],'before':digest,'after':hashlib.sha256(out).hexdigest(),'prior_entries_preserved':True,'applied':a.apply}
    if a.apply:
        fd,tmp=tempfile.mkstemp(prefix='.manifest-cloud-',dir=r)
        try:
            with os.fdopen(fd,'wb') as f:f.write(out);f.flush();os.fsync(f.fileno())
            os.replace(tmp,path)
        finally:
            if os.path.exists(tmp):os.unlink(tmp)
    print(json.dumps(receipt,sort_keys=True))
