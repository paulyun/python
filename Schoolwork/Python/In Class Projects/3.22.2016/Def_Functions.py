def printName():
    strName = input("Please enter first name: ")
    print (strName)

printName() #This calls the function def printName() written on line one.

#-----------------------------------------------------------------------------------

def printName():
    strName = input("Please enter first name: ")
    return strName

returnedValue = printName()
print(returnedValue)

#-----------------------------------------------------------------------------------

def sumofNumbers(x,y):
    sum = x + y
    return sum

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the first number"))

sumofValues = sumofNumbers(num1, num2)
print(sumofValues)

#-----------------------------------------------------------------------------------

def compareTwoValues(x, y):
    if (x >= y):
        return True
    else:
        return False

print(compareTwoValues (8,9))

#-----------------------------------------------------------------------------------

def compareTwoValues(x, y):
    if (x >= y):
        return True
    else:
        return False

for i in range (5):        
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the first number"))
    print("Is X greater than or equal to Y?", compareTwoValues(num1 ,num2))