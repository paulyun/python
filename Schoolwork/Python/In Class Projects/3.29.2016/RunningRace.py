#Race Results
#Paul_Yun CS_902 Spring 2016

first_runners_name = str(input("Please Enter the name for the first runner"))
second_runners_name = str(input("Please Enter the name for the second runner"))
third_runners_name = str(input("Please Enter the name for the third runner"))

first_runners_time = float(input("Please Enter the time for the first runner in seconds"))
while(first_runners_time <= 0):
    print( "runner three time cant be negative or zero")
    runner_three_time = float(input(" enter a value higher than zero for runner three time"))
    
second_runners_time = float(input("Please Enter the time for the first runner in seconds"))
while(second_runners_time <= 0):
    print( "runner three time cant be negative or zero")
    runner_three_time = float(input(" enter a value higher than zero for runner three time"))
    
third_runners_time = float(input("Please Enter the time for the first runner in seconds"))
while(third_runners_time <= 0):
    print( "runner three time cant be negative or zero")
    runner_three_time = float(input(" enter a value higher than zero for runner three time"))
    
if (first_runners_time < second_runners_time and first_runners_time < third_runners_time):
    print("The first place winner is", first_runners_name)

elif (first_runners_time > second_runners_time and first_runners_time < third_runners_time) or (first_runners_time < second_runners_time and first_runners_time > third_runners_time):
    print("The second place winner is", first_runners_name)
    
elif (first_runners_time > second_runners_time and first_runners_time > third_runners_time):
    print("The third place winner is", first_runners_name)
    
if (second_runners_time < first_runners_time and second_runners_time < third_runners_time) :
    print("The first place winner is", second_runners_name)

elif (second_runners_time < first_runners_time and second_runners_time < third_runners_time) or (second_runners_time > first_runners_time and second_runners_time > third_runners_time):
    print("The second place winner is", second_runners_name)
    
elif (second_runners_time > second_runners_time and second_runners_time > third_runners_time):
    print("The third place winner is", second_runners_name)

if (third_runners_time < second_runners_time and third_runners_time < first_runners_time):
    print("The first place winner is", third_runners_name)

elif (third_runners_time > second_runners_time and third_runners_time < first_runners_time) or (third_runners_time < second_runners_time and third_runners_time > first_runners_time):
    print("The second place winner is", third_runners_name)
    
elif (third_runners_time > second_runners_time and third_runners_time > first_runners_time):
    print("The third place winner is", third_runners_name)