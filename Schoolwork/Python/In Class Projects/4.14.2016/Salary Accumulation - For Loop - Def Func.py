employee_names = []
employee_salaries = []
total_salary = 0

for i in range (6):
    employee_names.append(str(input("What is the name for employee" +str(i+1) + "?")))
    
    def evaluate_salary(x,y):
        sum = x + y
        return sum
        
    salaries = float(input("Enter your salary"))
    employee_salaries.append(salaries)
    
    total_salary = evaluate_salary(total_salary,salaries)

print(employee_names)
print(employee_salaries)