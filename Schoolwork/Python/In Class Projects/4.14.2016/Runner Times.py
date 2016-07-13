#Program created by Paul Yun 4/14/2016
#Gathering runners names and times.
#Placing the runners in first, second, and third ranking.

runner_names = []
runner_time = []

for i in range (3):
    runner_names.append(input("What is the name for the runner" +str(i+1) + "?"))
    runner_time.append(float(input("What is the time for the runner" +str(i+1) + "? In seconds")))

   
if(runner_time[0] < runner_time[1] and runner_time[0] < runner_time[2]):
    if(runner_time[1] < runner_time[2]):
        print(runner_names[0] , "is the first place runner with a time of:", runner_time[0])
        print(runner_names[1] , "is the second place runner with a time of:", runner_time[1])
        print(runner_names[2] , "is the third place runner with a time of:", runner_time[2])
        
if(runner_time[2] < runner_time[0] and runner_time[2] < runner_time[1]):
    if(runner_time[0] < runner_time[1]):
        print(runner_names[2] , "is the first place runner with a time of:", runner_time[2])
        print(runner_names[0] , "is the second place runner with a time of:", runner_time[0])
        print(runner_names[1] , "is the third place runner with a time of:", runner_time[1])

if(runner_time[1] < runner_time[0] and runner_time[1] < runner_time[2]):
    if(runner_time[2] < runner_time[0]):
        print(runner_names[1] , "is the first place runner with a time of:", runner_time[1])
        print(runner_names[2] , "is the second place runner with a time of:", runner_time[2])
        print(runner_names[0] , "is the third place runner with a time of:", runner_time[0])
                
        
print(runner_names)
print(runner_time)