item_list = []
size_list = int(input("What is the size of the list you want to create?"))

for i in range(size_list):
    item_list.append(int(input("Enter the integer number" +str(i+1)+ "")))

#this functions returns the minimal value
#def FindMin():
    #minimumValue = 1000
    #for i in range(size_list):
        #if item_list[i] < minimumValue
            #minimumValue = item_list[i]
            
        #return minimumValue

#this functions returns the maximum value
def FindMax():
    maximumValue = 0
    for i in range(size_list):
        if item_list[i] > maximumValue:
            maximumValue = item_list[i]
            
        return maximumValue
        
print(item_list)
print("The largest value in the list is", FindMax())