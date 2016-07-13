import random
level = input("Choose a level - Beginner, Intermediate, or Advanced:")
type = input("Choose - Addition, Subtraction, Multiplication, or Mixed")
randnumbers = int(input("How many questions do you want to answer?"))
correct = 0

def addition():
	answer = x + y
	myanswer = int(input("What is the answer " +str(x) + " + " + str(y)))
	if (answer == myanswer):
	    correct += 1

def multiplication():
	answer = x * y
	myanswer = int(input("What is the answer " +str(x) + " * " + str(y)))
	if (answer == myanswer):
	    correct += 1

def subtraction():
	answer = x - y
	myanswer = int(input("What is the answer " +str(x) + " - " + str(y)))
	if (answer == myanswer):
	    correct += 1
	
def mixed():
    answer = x + y
    myanswer = int(input("What is the answer " +str(x) + " + " + str(y)))
    if (answer == myanswer):
	    correct += 1
    answer = x * y
    myanswer = int(input("What is the answer " +str(x) + " * " + str(y)))
    if (answer == myanswer):
	    correct += 1
    answer = x - y
    myanswer = int(input("What is the answer " +str(x) + " - " + str(y)))
    if (answer == myanswer):
	    correct += 1
    
        
        

if level == "Beginner":
    for i in range(randnumbers):
	    x=random.randint(1,10)
	    y=random.randrange(1, 10)
	    
    if type == "Addition":
	    addition()
    elif type == "Subtraction":
	    subtraction()
    elif type == "Multiplication":
	    multiplication()
    elif type == "Mixed":
	    mixed()
	    
if level == "Intermediate":
    for i in range(randnumbers):
	    x=random.randint(1,25)
	    y=random.randrange(1, 25)

    if type == "Addition":
	    addition()
    elif type == "Subtraction":
	    subtraction()
    elif type == "Multiplication":
	    multiplication()
    elif type == "Mixed":
	    mixed()

if level == "Advanced":
    for i in range(randnumbers):
	    x=random.randint(1,100)
	    y=random.randrange(1, 100)

    if type == "Addition":
	    addition()
    elif type == "Subtraction":
	    subtraction()
    elif type == "Multiplication":
	    multiplication()
    elif type == "Mixed":
	    mixed()
        
if correct == 3:
    print("Well Done!")
elif correct == 2:
    print("You need more practice!")
elif correct == 1:
    print("Please ask your math teacher for help!")