import json

with open('roles.json') as f:
    roles_json=json.load(f)
pk=1
for item in roles_json:
    item['pk']=pk
    pk+=1
with open('roles_data.json','w') as outfile1:
        json.dump(roles_json,outfile1, indent=4,ensure_ascii=False)