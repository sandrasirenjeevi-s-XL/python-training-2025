import json
def load_json(filename):
    with open(filename,'r') as f:
        return json.load(f)
    
def filter_by_dept(data,department):
    filtered=[emp for emp in data if emp.get("department")==department]
    return filtered

def average_salary(data):
    sal=[emp.get('salary') for emp in data]
    avg=sum(sal)/len(data)
    return avg

def assign_level(data):
    for emp in data:
        salary=emp.get('salary',0)
        if salary>100000:
            emp['level']='Senior'
        else:
            emp['level']='Junior'
    return data
def save_json(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f,indent=4)
db=load_json('employee.json')
filtered_employees=filter_by_dept(db,'HR')
print(filtered_employees)
print(average_salary(db))
new_data=assign_level(db)
print(new_data)
save_json(new_data,'employee.json')
