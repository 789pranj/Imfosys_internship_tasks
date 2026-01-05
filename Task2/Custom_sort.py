def sort_by_salary_desc(employees):
    return sorted(employees, key=lambda x: x["salary"], reverse=True)

def sort_by_age_then_salary(employees):
    return sorted(employees, key=lambda x: (x["age"], x["salary"]))

employees = [
    {"name": "Ajay", "age": 22, "salary": 25000},
    {"name": "Rahul", "age": 25, "salary": 40000},
    {"name": "Kiran", "age": 21, "salary": 30000}
]

print(f"Sorted by salary descending order: \n {sort_by_salary_desc(employees)}")

print(f"Sorted by age then salary: \n {sort_by_age_then_salary(employees)}")

