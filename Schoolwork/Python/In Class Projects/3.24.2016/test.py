current_tuition = 15000
for p in range(1,11):
    increase_rate = float(input("What is your tuition's increase rate for year"))
    current_tuition = current_tuition + current_tuition*increase_rate
    print("The Current Tuition for year ", p, "is $", format(current_tuition, '.2f'))
    
current_tuition = 15000
    increase_rate = float(input("What is your tuition's increase rate for year"))
    current_tuition = current_tuition + current_tuition*increase_rate
    print("The cost of your tuition is", current_tuition)
    
for p in range(1,10):
    increase_rate = increase_rate + 0.05
    current_tuition = current_tuition + increase_rate
    print("The cost of your tuition is", current_tuition)