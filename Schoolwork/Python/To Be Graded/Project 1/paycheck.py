# Paul Yun, March 3, 2016, Project 1-Program 1
# paycheck project

# Input command for users first name
firstName = input("Enter first name")

# Input command for users last name
lastName = input("Enter last name")

# Input command for users hours worked
hoursWorked = int(input ("Enter hours worked"))

# Input command for users hourly wage
hourlyWage = float(input ("Enter hourly wage"))

# Executes the creation of the users full name
userName = firstName + lastName

# Executes the users gross wage
grossWage = hoursWorked * hourlyWage

# Displays users full name, gross wage
print(userName)
print(grossWage)