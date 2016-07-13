#reads only one line
filed_read = open("Rainfall.txt", "r")
month_first = filed_read.readline()
month_last = filed_read.readline()
sum = float
sum = 0

for line in filed_read:
    str = line.split()
    print(str)
    for p in range(len(str)):
        sum = sum + float(str[p])
        avg = sum / 4
        
    print("The total rainfall between", month_first, "-", month_last, "is", sum)
    print("The average rainfall between", month_first, "-", month_last, "is", avg)