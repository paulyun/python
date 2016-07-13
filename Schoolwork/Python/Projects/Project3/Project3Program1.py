#Gross Pay
#Paul_Yun CS_902 Spring 2016

employee_name = str(input("Please enter your name"))
employee_salary = float(input("Please enter your salary").replace(",", ""))

if (employee_salary>100000):
    federal_tax = (employee_salary * 0.2)
elif (employee_salary<100000):
    federal_tax = (employee_salary * 0.15)

state_tax = (employee_salary * 0.05)

net_salary = employee_salary - (federal_tax+state_tax)

print("Youre net salary is", net_salary)