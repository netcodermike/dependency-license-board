import argparse,json,re,unittest
from pathlib import Path
def inventory(folder):
 root=Path(folder);rows=[];errors=[]
 package=root/'package.json'
 if package.exists():
  try:
   data=json.loads(package.read_text(encoding='utf-8'))
   for group in ['dependencies','devDependencies','peerDependencies']:
    for name,version in data.get(group,{}).items():rows.append({'ecosystem':'npm','name':name,'requested':str(version),'group':group,'license':'unknown; inspect installed package/license evidence'})
  except(ValueError,AttributeError)as e:errors.append(str(e))
 req=root/'requirements.txt'
 if req.exists():
  for line in req.read_text(encoding='utf-8').splitlines():
   line=line.strip()
   if not line or line.startswith('#'):continue
   if line.startswith('-'):
    errors.append('Unsupported requirements directive: '+line);continue
   match=re.match(r'([A-Za-z0-9_.-]+)(.*)',line)
   if match:rows.append({'ecosystem':'pypi','name':match[1],'requested':match[2].strip(),'group':'requirements','license':'unknown; inspect distribution metadata'})
   else:errors.append('Unsupported requirements directive: '+line)
 evidence=[]
 for p in sorted(root.iterdir()):
  if p.is_file()and(p.name.upper().startswith(('LICENSE','COPYING','NOTICE'))):evidence.append({'path':p.name,'excerpt':p.read_text(encoding='utf-8',errors='replace')[:500]})
 return {'dependencies':rows,'local_license_evidence':evidence,'errors':errors,'scope':'direct manifest inventory; no inferred licenses, transitive resolution or legal conclusions'}
class Tests(unittest.TestCase):
 def test_manifests(self):
  import tempfile
  with tempfile.TemporaryDirectory()as d:
   p=Path(d);(p/'package.json').write_text('{"dependencies":{"example":"^1.0"}}');(p/'requirements.txt').write_text('demo==2.0\n# comment\n-r other.txt');r=inventory(p);self.assertEqual(len(r['dependencies']),2);self.assertTrue(r['errors']);self.assertIn('unknown',r['dependencies'][0]['license'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('folder',nargs='?',default='.');p.add_argument('--self-test',action='store_true');a=p.parse_args()
 if a.self_test:unittest.main(argv=['licenses'])
 else:print(json.dumps(inventory(a.folder),indent=2))
