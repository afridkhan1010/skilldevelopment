import json

with open('skills.json') as f:
    skills_json=json.load(f)
pk=1
for item in skills_json:
    item['pk']=pk
    pk+=1
with open('skills_data.json','w') as outfile1:
        json.dump(skills_json,outfile1, indent=4,ensure_ascii=False)