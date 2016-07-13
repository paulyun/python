# Paul Yun, March 3, 2016, Project 1-Program 2

personOne = input("Enter first name")
personTwo = input("Enter first name")
personThree = input("Enter first name")

lunchOne = float(input("Enter lunch cost for personOne"))
lunchTwo = float(input("Enter lunch cost personTwo"))
lunchThree = float(input("Enter lunch cost personThree"))

drinkOne = float(input("Enter drink cost personOne"))
drinkTwo = float(input("Enter drink cost personTwo"))
drinkThree = float(input("Enter drink cost personThree"))

lunchtotalOne = (lunchOne + drinkOne) * .15
lunchtotalTwo = (lunchOne + drinkOne) * .15
lunchtotalThree = (lunchOne + drinkOne) * .15

totalOne = lunchOne + drinkOne + lunchtotalOne
totalTwo = lunchTwo + drinkTwo + lunchtotalTwo
totalThree = lunchThree + drinkThree + lunchtotalThree

print (personOne , float(totalOne))
print (personTwo , float(totalTwo))
print (personThree , float(totalThree))