import json

with open('domains.json') as f:
    domain_json=json.load(f)
pk=1
for item in domain_json:
    item['pk']=pk
    pk+=1
with open('domain_data.json','w') as outfile1:
        json.dump(domain_json,outfile1, indent=4,ensure_ascii=False)