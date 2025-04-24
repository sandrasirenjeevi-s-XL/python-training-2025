import json

# with open('employee.json','r') as f:
#     data=json.load(f)       # read            json.load()
#     print(data)
#    #  json.dump()    # write

# json_str ='{"name":"jani","dept":"cse","id":43}'
# data=json.loads(json_str)
# json_out=json.dumps(data)
# print(json_out)


def load_json(filename):
    with open(filename,'r') as f:
        return json.load(f)
    
# filter by dept
# def filter_by_dept(data,department):
#     filtered=[emp for emp in data if emp.get("department") == department]

#     return filtered

db=load_json('employee.json')

# filtered_emp=filter_by_dept(db,'HR')
# print(filtered_emp)

def avg_salary(data):
    sal=[emp.get('salary') for emp in data]
    avg=sum(sal)/len(data)
    return avg
db=load_json('employee.json')
#print(avg_salary(db))

def add_level(data):
    for emp in data:
        salary=emp.get('salary',0)
        if salary>10000:
            emp['level']='senior'
        else:
            emp['level']="mid"
    return data
new_data=add_level(db)


def save_json(data,filename):
    with open(filename, 'w') as f:
        json.dump(data,f,indent=4)
print(new_data)
save_json(new_data,'employee.json')
