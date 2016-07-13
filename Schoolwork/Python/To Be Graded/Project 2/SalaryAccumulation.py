#Employee Yearly Salary Accumulation
#Paul_Yun CS_902 Spring 2016

account_balance = 0

employee_one = float(input("Please input the salary for your first employee"))
account_balance = employee_one

employee_two = float(input("Please input the salary for your second employee"))
account_balance = account_balance + employee_two

employee_three = float(input("Please input the salary for your second employee"))
account_balance = account_balance + employee_three

employee_four = float(input("Please input the salary for your second employee"))
account_balance = account_balance + employee_four

employee_five = float(input("Please input the salary for your second employee"))
account_balance = account_balance + employee_five
print("The salary total for five employees is ", account_balance, format(account_balance, '.2f'))