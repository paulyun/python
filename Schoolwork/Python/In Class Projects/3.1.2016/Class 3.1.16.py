# 3/1/2016 classwork - Testing a Number to see if it's positive

numberOne = int(input ("Input a number"))
numberTwo = int(input ("Input a number"))

result = numberOne % numberTwo
resultTwo = result % 2

if (resultTwo == 0):
    print("number is even")
else:
    print("number is odd")
