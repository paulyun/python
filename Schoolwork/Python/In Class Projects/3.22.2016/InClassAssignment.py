tuition_cost_year_one = 15000
print("The tuition cost for the first year is", tuition_cost_year_one)
tuition_cost_year_two = ((tuition_cost_year_one * 0.04)+tuition_cost_year_one)
print("The tuition cost for the second year is", tuition_cost_year_two)
tuition_cost_year_three = ((tuition_cost_year_two * 0.04)+tuition_cost_year_two)
print("The tuition cost for the third year is", tuition_cost_year_three)
tuition_cost_year_four = ((tuition_cost_year_three * 0.04)+tuition_cost_year_three)
print("The tuition cost for the fourth year is", tuition_cost_year_four)
tuition_cost_year_five = ((tuition_cost_year_four * 0.04)+tuition_cost_year_four)
print("The tuition cost for the fifth year is", tuition_cost_year_five)
tuition_cost_year_six = ((tuition_cost_year_five * 0.04)+tuition_cost_year_five)
print("The tuition cost for the sixth year is", tuition_cost_year_six)
tuition_cost_year_seven = ((tuition_cost_year_six * 0.04)+tuition_cost_year_six)
print("The tuition cost for the seventh year is", tuition_cost_year_seven)
tuition_cost_year_eight = ((tuition_cost_year_seven * 0.04)+tuition_cost_year_seven)
print("The tuition cost for the eighth year is", tuition_cost_year_eight)
tuition_cost_year_nine = ((tuition_cost_year_eight * 0.04)+tuition_cost_year_eight)
print("The tuition cost for the ninth year is", tuition_cost_year_nine)
tuition_cost_year_ten = ((tuition_cost_year_nine * 0.04)+tuition_cost_year_nine)
print("The tuition cost for the tenth year is", tuition_cost_year_ten)

#----------------------------------------------------------------------------------
#Answer #1
current_tuition = 15000
increase_rate = 0.04

for i in range(1,11):
    print("The Current Tuition for year ", i, "is $", current_tradition)
    current_tuition = current_tuition + current_tuition*increase_rate
#----------------------------------------------------------------------------------
#Answer #2
current_tuition = 15000
increase_rate = float(input("What is your tuition's increase rate?"))
#validating user input
while(increase_rate <=0):
    print("Please enter a value higher than 0.0")
    increase_rate = float(input("Please enter a value higher than 0.0"))

for i in range(1,11):
    print("The Current Tuition for year ", i, "is $", format(current_tuition, '.2f'))
    current_tuition = current_tuition + current_tuition*increase_rate
#----------------------------------------------------------------------------------
#Answer #2
current_tuition = 15000
increase_rate = float(input("What is your tuition's increase rate?"))
#validating user input
def validate_user_input():
    while(increase_rate <=0):
        print("Please enter a value higher than 0.0")
        increase_rate = float(input("Please enter a value higher than 0.0"))

def calculate_tuition():
    for i in range(1,11):
        print("The Current Tuition for year ", i, "is $", format(current_tuition, '.2f'))
        current_tuition = current_tuition + current_tuition*increase_rate
#----------------------------------------------------------------------------------
#Answer #2
current_tuition = 15000
increase_rate = float(input("What is your tuition's increase rate?"))
#validating user input
def validate_user_input():
    global increase_rate
    while(increase_rate <=0):
        print("Please enter a value higher than 0.0")
        increase_rate = float(input("Please enter a value higher than 0.0"))

def calculate_tuition():
    global current_tuition
    for i in range(1,11):
        print("The Current Tuition for year ", i, "is $", format(current_tuition, '.2f'))
        current_tuition = current_tuition + current_tuition*increase_rate
        
validate_user_input()
calculate_tuition
#----------------------------------------------------------------------------------
#Answer #3
current_tuition = 15000
increase_rate = float(input("What is your tuition's increase rate for year"))
current_tuition = current_tuition + current_tuition*increase_rate
print("The cost of your tuition is", current_tuition)
    
for p in range(1,10):
    increase_rate = increase_rate + 0.05
    current_tuition = current_tuition * increase_rate
    print("The cost of your tuition is", current_tuition)
#----------------------------------------------------------------------------------
#Custom Answer
current_tuition = 15000
for p in range(1,11):
    increase_rate = float(input("What is your tuition's increase rate for year"))
    current_tuition = current_tuition + current_tuition*increase_rate
    print("The Current Tuition for year ", p, "is $", format(current_tuition, '.2f'))