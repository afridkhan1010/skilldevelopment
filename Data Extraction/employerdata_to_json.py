import json
import pandas as pd

#converting Xlsx file to json file
# df = pd.read_excel('Companies.xlsx')
# json_data = df.to_json(orient="records", force_ascii=False,indent=4)
# with open('companiesdata__all.json', 'w') as f1:
#     f1.write(json_data)

#read the json data
with open('companiesdata__all.json') as f2:
    res_json = json.load(f2) 
with open('locations.json','r') as loc:# The location file which has locations and primary key for a particular location
    loc_json = json.load(loc) 
for index,item in enumerate (res_json):
    attr = []
    item['model'] = "employers.employer"
    item['fields']={}
    # del item['url']
    del item['Github URL ']
    if item['LinkedIn URL'] is not None:
        del item['LinkedIn URL']
    if item['Facebook URL'] is not None:
        del item['Facebook URL']
    if item['Twitter URL'] is not None:
        del item['Twitter URL']
    # if item['Github URL '] is not None:   
    #     del item['Github URL ']
    if item['Instagram URL'] is not None:
        del item['Instagram URL']
    if item['Brand Name'] is not None :
        item['fields']['name']=item['Brand Name']
        del item['Brand Name']
    del item['LinkedIn Employees Size (# of Employees on LinkedIn)']
    if 'Industry\/sector' in item:
        del item["Industry\/sector"]
    if 'Industry/sector' in item:
        del item["Industry/sector"]

    if 'Description' in item:
        val=item['Description']
        if val is not None:
            if len(val) !=0:
                val=val.replace('"',"'")
                item['fields']['description']=val
            
        # item['fields']['description']=val
        del item['Description']
    if 'website' in item:
        value=item["website"]
        # item['fields']['website']=value
        if value is not None:
            if len(value) !=0:
                value=value.replace('\/','/')
                item['fields']['website'] = value
    #     # item['fields']['website']=item['website']
        if value is None:
            continue
        del item['website']
        if value=="":
            del item['website']
 
    if 'Logo' in item:
        value1=item['Logo']
        if value1 is not None:
            value1=value1.replace('\/','/')
            item['fields']['logo']=value1
        del item['Logo']
    del item['logo']   
    if 'Tag line'in item:  
        item['fields']['tagline']=item['Tag line']
        del item['Tag line']
    if 'domain'in item:  
        item['fields']['domain']=item['domain']
        del item['domain']
    if 'Company Size (# of Employees)'in item:    
        item['fields']['company_size']=item['Company Size (# of Employees)']
        del item['Company Size (# of Employees)']
    if 'Company Type (Pvt, Public, etc)'in item:
        item['fields']['company_type']=item['Company Type (Pvt, Public, etc)']
        del item['Company Type (Pvt, Public, etc)']
    if 'Phone Number'in item:  
        item['fields']['phone_number']=item['Phone Number']
        del item['Phone Number']
    if 'Email'in item:    
        item['fields']['email']=item['Email']
        del item['Email']
    if 'Year founded'in item: 
        item['fields']['year_founded']=item['Year founded']
        del item['Year founded']
        #converting year float format to readable string format
        if item['fields']['year_founded']=="":
             del item['fields']['year_founded']
        else:
            item['fields']['year_founded']=str(item['fields']['year_founded']).replace('.0','-01-01')

    if 'Specialties (Technologies, Services, Products)'in item: 
        item['fields']['specialities']=item['Specialties (Technologies, Services, Products)']
        del item['Specialties (Technologies, Services, Products)']
        if item['fields']['specialities']=="":
            del item['fields']['specialities']
    if "Work Type (Remote\/Office\/Hybrid)" in item: 
        item['fields']['work_type']=item["Work Type (Remote\/Office\/Hybrid)"]
        del item["Work Type (Remote\/Office\/Hybrid)"]
    if "Work Type (Remote/Office/Hybrid)" in item: 
        item['fields']['work_type']=item["Work Type (Remote/Office/Hybrid)"]
        del item["Work Type (Remote/Office/Hybrid)"]

    if item['Business Entity'] is not None:
        item['fields']['business_entity']=item['Business Entity']
        del item['Business Entity']
 
    # if 'links'in item: 
    item['fields']['links']=""
        # del item['links']
        
    if 'Total Funding' in item: 
        val_fund=item['Total Funding']
    #     item['fields']['total_fund']=item['Total Funding']
        if val_fund is not None:
            # val_fund=str(item['fields']['total_fund'])[-1]
            # item['fields']['total_fund_type']=val_fund
            fund_val=val_fund
            if '$' in fund_val:
                fund_val=str(fund_val).replace('$','')
                if fund_val[-1]=="M":
                    fund_val=fund_val.replace("M",'')
                    m_fund=int(float(fund_val))
                    m_fund=round((m_fund)*1000000)
                    item['fields']['total_fund']=m_fund
                    item['fields']['total_fund_type']="M"
                elif fund_val[-1]=="B":
                    fund_val=fund_val.replace("B",'')
                    b_fund=int(float(fund_val))
                    b_fund=round((b_fund)*100000000)
                    item['fields']['total_fund']=b_fund
                    item['fields']['total_fund_type']="B"
                elif fund_val[-1]=="K":
                    fund_val=fund_val.replace("K",'')
                    k_fund=int(float(fund_val))
                    k_fund=round((k_fund)*1000)
                    item['fields']['total_fund']=k_fund
                    item['fields']['total_fund_type']="K"
            elif 'Cr' in fund_val:
                oddvalue=fund_val
                oddvalue= oddvalue.replace("Cr",'')
                oddvalue=int(float(oddvalue))*10000000
                item['fields']['total_fund_type']="K"
                item['fields']['total_fund']=oddvalue
            elif "B+" in fund_val:
                oddvalue=fund_val
                oddvalue= oddvalue.replace("B+",'')
                oddvalue=int(float(oddvalue))*100000000
                item['fields']['total_fund_type']="B"
                item['fields']['total_fund']=oddvalue
            elif "M Euro" in fund_val:
                oddvalue=fund_val
                oddvalue= oddvalue.replace("M Euro",'')
                oddvalue=int(float(oddvalue))*1000000
                item['fields']['total_fund_type']="M"
                item['fields']['total_fund']=oddvalue
            elif "B Euro" in fund_val:
                if "Euros" in fund_val:
                    oddvalue=fund_val
                    oddvalue= oddvalue.replace("B Euros",'')
                    oddvalue=int(float(oddvalue))*100000000
                    item['fields']['total_fund_type']="B"
                    item['fields']['total_fund']=oddvalue

                else:
                    oddvalue=fund_val
                    oddvalue= oddvalue.replace("B Euro",'')
                    oddvalue=int(float(oddvalue))*100000000
                    item['fields']['total_fund_type']="B"
                    item['fields']['total_fund']=oddvalue
            elif "B Yen" in fund_val:
                oddvalue=fund_val
                oddvalue= oddvalue.replace("B Yen",'')
                oddvalue=int(float(oddvalue))*100000000
                item['fields']['total_fund_type']="B"
                item['fields']['total_fund']=oddvalue

            else:
                if '$' in fund_val:
                    fund_val=(fund_val.replace('$',''))
                    fund_val=round(float(fund_val)*1000)
                    item['fields']['total_fund_type']="K"
                    item['fields']['total_fund']=fund_val
                elif 'M' in fund_val:
                    oddvalue=fund_val
                    oddvalue= oddvalue.replace("M",'')
                    oddvalue=int(float(oddvalue))*1000000
                    item['fields']['total_fund_type']="M"
                    item['fields']['total_fund']=oddvalue
                else:
                    oddvalue=fund_val
                    oddvalue= oddvalue.replace("K",'')
                    oddvalue=int(float(oddvalue))*1000
                    item['fields']['total_fund_type']="K"
                    item['fields']['total_fund']=oddvalue
        else:
            item['fields']['total_fund_type']="K"
    del item['Total Funding']

    if 'B2X' in item: 
        item['fields']['b2x']=item['B2X']
        del item['B2X']
        if item['fields']['b2x']=="":
            del item['fields']['b2x']

    if 'Technologies used' in item: 

        technologies_val=item['Technologies used']
        # tech_val=item['fields']['technologies']
        

        if technologies_val is not None:
            technologies_val=[technologies_val]
            if 'and' in technologies_val:
                technologies_val=technologies_val.replace('and','')
            if technologies_val==['']:
                technologies_val=[]
            else:
                if technologies_val is not None:
                    for j in technologies_val:
                        technologies_val=j.split(",")
            item['fields']['technologies']=technologies_val
        del item['Technologies used']
    # if 'tags' in item: 
    item['fields']['tags']=[]
        # del item['tags']
    if 'Product or Service'in item: 
        item['fields']['prod_service']=item['Product or Service']
        del item['Product or Service']

    # if 'attributes'in item: 
    # item['fields']['attributes']=[]
        # del item['attributes']

    if item['is Unicorn'] == 'Yes':
#         #item['attributes'] += ['unicorn']
        attr.append("unicorn")
    if item['is Bootstrapped'] == 'Yes':
#         #item['attributes'] += ['bootstrap']
        attr.append("bootstrap")
    item['fields']['attributes'] = attr
    del item['is Bootstrapped']
    del item['is Unicorn']

    # print(item)
    # break
    item['fields']['location']=[]
    value=item['fields']['location']   
    temp=[]

    if item['Headquarters location'] is not None:
        head=item['Headquarters location'].split(',')
        for locid in loc_json:
            if head[0] in locid['fields']['city']:
                head_location={"location_name":"headquarters",
                                    "location_id":locid['pk'],
                                    "address":head[0],
                                    "primary":True}
                break
            else:
                head_location={"location_name":"headquarters",
                    "address":head[0],
                    "primary":True}  
        temp.append(head_location)
    if item['Other locations'] is not None:
        other=item['Other locations'].split(',')
        for otherlocations in other:
            for locid in loc_json:
                if otherlocations in locid['fields']['city']:
                    head_location={"location_name":"branch","location_id":locid['pk'],"address":otherlocations,"primary":False}

                    break
                else:
                    head_location={"location_name":"branch",
                    "address":otherlocations,
                        "primary":False}
            temp.append(head_location)
    item['fields']['location']=temp 
    del item['Headquarters location']
    del item['Other locations']
    item['fields']["created_on"]= "2022-07-01T09:00:00.000Z"
    item['fields']["updated_on"]= "2022-07-01T09:00:00.000Z"
    item['fields']["is_deleted"]=False
with open("employers1.json", "w") as outfile:
    json.dump(res_json,outfile, ensure_ascii=False, indent=4)

# with open('employers1.json') as f1:
#     res_json = json.load(f1)

# for index, item in enumerate(res_json):
    # print(item)



    # attr = []


# print(item)

# with open("employer.json", "w") as outfile:
#     json.dump(res_json,outfile)