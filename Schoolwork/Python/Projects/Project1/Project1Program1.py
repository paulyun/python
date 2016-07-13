# Paul Yun, March 3, 2016, Project 1-Program 1

firstName = input("Enter first name")
lastName = input("Enter last name")
hoursWorked = int(input ("Enter hours worked"))
hourlyWage = float(input ("Enter hourly wage"))
userName = firstName + lastName
grossWage = hoursWorked * hourlyWage
print(userName)
print(grossWage)