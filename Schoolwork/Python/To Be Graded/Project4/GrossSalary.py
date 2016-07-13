#Paul yun cs902 Spring 2016 4/5/2016
#Project 4 Program 1

for p in range(1,7):
    employee_name = str(input("Please enter your name"))
    employee_salary = float(input("What is your annual salary?"))

    if (employee_salary>100000):
        federal_tax = (employee_salary * 0.2)
    elif (employee_salary<=100000):
        federal_tax = (employee_salary * 0.15)
    
    valid_options_ten = ['CA', 'NV', 'AZ', 'WA']
    valid_options_twelve = ['AK', 'AL', 'AR', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WV', 'WI', 'WY']
    state = input("Enter the 2 letter abbreviation of your state").upper()
    if state in valid_options_ten:
        state_tax = (employee_salary * 0.1)
    elif state in valid_options_twelve:
        state_tax = (employee_salary * 0.12)
    elif state not in valid_options_ten or valid_options_twelve:
        print("Start over and enter a valid 2 letter state abbreviation")
        
    gross_salary = employee_salary - federal_tax - state_tax

    print("For employee", employee_name)
    print("Federal tax is", federal_tax)
    print("State tax is", state_tax)
    print("Gross Salary is", gross_salary)