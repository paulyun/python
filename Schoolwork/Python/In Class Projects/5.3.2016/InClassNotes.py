file_read = open("Rainfall.txt", "r")
file_write = open("RainFallResult.txt", "w")

counter = 0
sum = 0
for line in file_read:
    counter +=1
    if counter == 3:
        str = line.split()
        for i in range(len(str)):
            print(str[i])
            sum += float(str[i])
            file_write.write(str[i] + ", ")