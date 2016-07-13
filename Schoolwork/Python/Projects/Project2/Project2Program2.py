#Weekly food and gas expenses
#Paul_Yun CS_902 Spring 2016

days_spent_more = 0
day_one_food = float(input("Please input the amount of money you spent on food for Monday"))
day_one_gas = float(input("Please input the amount of money you spent on gas for Monday"))
if (day_one_food >20 and day_one_gas> 10):
    days_spent_more = days_spent_more +1
    
day_two_food = float(input("Please input the amount of money you spent on food for Tuesday"))
day_two_gas = float(input("Please input the amount of money you spent on gas for Tuesday"))
if (day_two_food >20 and day_two_gas> 10):
    days_spent_more = days_spent_more +1
    
day_three_food = float(input("Please input the amount of money you spent on food for Wednesday"))
day_three_gas = float(input("Please input the amount of money you spent on gas for Wednesday"))
if (day_three_food >20 and day_three_gas> 10):
    days_spent_more = days_spent_more +1
    
day_four_food = float(input("Please input the amount of money you spent on food for Thursday"))
day_four_gas = float(input("Please input the amount of money you spent on gas for Thursday"))
if (day_four_food >20 and  day_four_gas> 10):
    days_spent_more = days_spent_more +1
    
day_five_food = float(input("Please input the amount of money you spent on food for Friday"))
day_five_gas = float(input("Please input the amount of money you spent on gas for Friday"))
if (day_five_food >20 and day_five_gas> 10):
    days_spent_more = days_spent_more +1
    
day_six_food = float(input("Please input the amount of money you spent on food for Saturday"))
day_six_gas = float(input("Please input the amount of money you spent on gas for Saturday"))
if (day_six_food >20 and day_six_gas> 10):
    days_spent_more = days_spent_more +1
    
day_seven_food = float(input("Please input the amount of money you spent on food for Sunday"))
day_seven_gas = float(input("Please input the amount of money you spent on gas for Sunday"))
if (day_seven_food >20 and day_seven_gas> 10):
    days_spent_more = days_spent_more +1

print("Amount of days in the week the user spent more than $20 for food or $10 for gas", days_spent_more)