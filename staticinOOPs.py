class employee:
    emp_no=0
    def __init__(self,name,salary,city,dept):
        self.emp_name = name
        self.emp_salary = salary
        self.emp_city = city
        self.emp_dept = dept
        self.empId = employee.emp_no+1
        employee.emp_no = employee.emp_no+1

    def __str__(self):
        return f"Employee ID: {self.empId}, Name: {self.emp_name}, Salary: {self.emp_salary}, City: {self.emp_city}, Department: {self.emp_dept}"   

l= list()

e1 = employee("John",50000,"New York","IT")
l.append(e1)

e2 = employee("Doe",60000,"Los Angeles","HR")
l.append(e2)

e3 = employee("Anna",55500,"Chicago","Finance")
l.append(e3)

for e in l:
     print(e)
         

def salary_income(L):
        for e in L:
            hike = e.emp_salary * 1.1
            e.emp_salary += hike    
            print(f"New salary is {e.emp_salary}")
print("Salary before hike:")
e1 = employee("John",50000,"New York","IT")
e2 = employee("Doe",60000,"Los Angeles","HR")
print("\nSalaries after 10% hike:")
salary_income([e1, e2])