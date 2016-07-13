# Paul Yun, March 3, 2016, Project 1-Program 2
# check split project

# Input command for user names
personOne = input("Enter first name")
personTwo = input("Enter first name")
personThree = input("Enter first name")

# Input command for lunch cost
lunchOne = float(input("Enter lunch cost for personOne"))
lunchTwo = float(input("Enter lunch cost personTwo"))
lunchThree = float(input("Enter lunch cost personThree"))

# Input command for drink cost
drinkOne = float(input("Enter drink cost personOne"))
drinkTwo = float(input("Enter drink cost personTwo"))
drinkThree = float(input("Enter drink cost personThree"))

# Executes the cost of tax
lunchtotalOne = (lunchOne + drinkOne) * .15
lunchtotalTwo = (lunchOne + drinkOne) * .15
lunchtotalThree = (lunchOne + drinkOne) * .15

# Executes the price of lunch cost + drink cost + cost of tax
totalOne = lunchOne + drinkOne + lunchtotalOne
totalTwo = lunchTwo + drinkTwo + lunchtotalTwo
totalThree = lunchThree + drinkThree + lunchtotalThree

# Displays Username, Total cost of lunch
print (personOne , float(totalOne))
print (personTwo , float(totalTwo))
print (personThree , float(totalThree))