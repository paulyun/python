item_list = []
size_list = int(input("What is the size of the list you want to create?"))

def userInput():
    for i in range(size_list):
        item_list.append(int(input("Enter the integer number"+str(i+1)+ "?  ")))


def sortList():
    for j in range(size_list-1):
        for i in range(size_list-1):
            if (item_list[i] > item_list[i+1]):
                tmp = item_list[i]
                item_list[i] = item_list[i+1]
                item_list[i+1]=tmp
     

print(item_list)
userInput()
sortList()