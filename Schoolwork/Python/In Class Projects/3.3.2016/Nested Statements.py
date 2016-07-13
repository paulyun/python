#using nested values

x = int(input ("Enter an integer value for x" + "\n"))
y = int(input ("Enter an integer value for y" + "\n"))

# tests if the value of x is less than y
if(x < y):
    print("x is less than y")
    if(x <= 0):
        print("x is less than or equal to zero")
    else:
        print("x is greater than zero")
# tests if the value of x is greater than y
else:
    if (x > 20):
        print("x is greater than 20")
    else:
        print("x is less than 20")
    print("x is greater than y")
    
print("Finished")