#import random
#operatorList = ['*', "/", '+', '-']
#print(random.choice(operatorList))


import random
operatorList = ['*', "/", '+', '-']
x = random.randint(1, 30)
y = random.randint(1, 10)

operation = random.choice(operatorList)
print(x)
print(y)
print(operation)
print(eval(str(x)+operation+str(y)))