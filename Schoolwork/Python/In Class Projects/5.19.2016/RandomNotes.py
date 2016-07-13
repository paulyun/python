import random
randnumbers = int(input("How many random integers do you want?"))

for i in range(randnumbers):
    x=random.randint(1,100)
    y=random.randrange(1, 100)
    answer = x * y
    print(x, "* ", y, "* ", answer)
    
    
    
import random
randnumbers = int(input("How many questions do you want to answer?"))
correct = 0

for i in range(randnumbers):
    x=random.randint(1,100)
    y=random.randrange(1, 100)
    answer = x * y
    myanswer = int(input("What is the answer " +str(x) + " * " + str(y)+ "*"))
    if (answer == myanswer):
        correct += 1
        print("Great Job....")
    else:
        print("Wrong answer")
        
print("You got", correct, "correct answers.")