import json

f = file('paihang.json')
data = json.load(f)
f.close()

for x in data:
	jsonstr = json.dumps(x)
	fout = file(x['name']+'.json', 'w')
	fout.write(jsonstr)
	fout.close()

