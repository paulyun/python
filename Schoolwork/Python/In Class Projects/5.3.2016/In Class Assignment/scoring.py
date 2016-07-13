file_read = open("scores.txt", "r")
file_write = open("scores_list.txt", "w")
list = []

counter = 0
hit = 0
#sum = 0

for line in file_read:
    str = line.split()
    list.append(str)

for row in list:
    del row[1]
    del row[0]
    
for item in list[0]:
    file_write.write(item + ", ")

for list 