#Program created by Paul Yun 4/19/2016.
#Gathers user name, user salary, and calculates tax.
#Displays username and net salary.

employee_name = str(input("Enter your name"))
    
def evaluate_salary(x, y, z):
    sum = x - (y + z)
    return sum 
        
salary = float(input("Enter your salary"))
if (salary>100000):
    federal_tax = (salary * 0.2)
elif (salary<=100000):
    federal_tax = (salary * 0.15)
    
state_tax = salary * 0.05
        
total_salary = evaluate_salary(salary, federal_tax, state_tax)
    
print("For user", employee_name)
print("Net salary is", total_salary)