import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open('D:\EdYoda\_assignment_6\_1_employee.json', 'r') as file:
    data = json.load(file)
    employee_list = []

    for emp_info in data['employees']:
        employee = Employee(emp_info['Name'], emp_info['DOB'], emp_info['Height'], emp_info['City'], emp_info['State'])
        employee_list.append(employee)

for employee in employee_list:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()
