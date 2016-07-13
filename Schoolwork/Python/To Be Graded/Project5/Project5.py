#Program created Paul Yun.
#Program asks user how many miles the user ran throughout the week.
#Program prints how many days user ran more than 5 miles.
#Program prints how many days user ran between 5-10 miles.
#Program prints how many days user ran more than 10 miles.

item_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_list = []
list_five = []
list_between = []
list_ten = []

for p in item_list:
    time_list.append(float(input("Enter the miles you ran for "+str(p)+ "?  ")))

for i in (time_list):    
    if (i < 5):
        list_five.append(i)
    
for z in (time_list):
    if (z >= 5) and (z <= 10):
        list_between.append(z)
    
for y in (time_list):
    if y > 10:
        list_ten.append(y)

print("The runner ran less than 5 miles for", len(list_five), "days")
print("The runner ran between 5-10 miles for", len(list_between), "days")
print("The runner ran more than 10 miles for", len(list_ten), "days")