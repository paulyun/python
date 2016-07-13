file_read = open("scores.txt", "r")
file_write = open("scores1.txt", "w")
strlist = []

def find_max (mylist):
    maximum = float
    maximum = 1
    for i in range(len(mylist)):
        if float(mylist[i]) > maximum:
            maximum = float(mylist[i])
    return maximum
    
def find_min (mylist):
    minimum = float
    minimum = 1000
    for i in range(len(mylist)):
        if float(mylist[i]) < minimum:
            minimum = float(mylist[i])
    return minimum
    
def find_avg (mylist):
    total = 0
    average = 0
    for value in range(len(mylist)):
        total += float(mylist[value])
    average = (total)/(len(mylist))
    return average


for line in file_read:
    strValue = line.split()
    file_write.write("Student" +strValue[0]+" "+strValue[1] + " scores are: ")
    for i in range(2,len(strValue)):
        strlist.append(strValue[i])
        maxValue = find_max(strlist)
        minValue = find_min(strlist)
        findAverage = find_avg(strlist)
        print(maxValue)
        if i == 11:
            file_write.write(strValue[i])
        else:
            file_write.write(strValue[i] + " ,")
    file_write.write(" Maximum value is:")
    file_write.write(str(maxValue))
    file_write.write(" Minimum value is:")
    file_write.write(str(minValue))
    file_write.write(" Average value is:")
    file_write.write(str(findAverage))
    strlist = []    
    file_write.write("\n")
    
        
file_read.close()
file_write.close()