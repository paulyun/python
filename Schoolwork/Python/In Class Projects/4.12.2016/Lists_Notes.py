list1= ['physics', 'computerscience', 1998, 2000]
print(list1[3])

list1= ['physics', 'computerscience', 1998, 2000]
print(list1[1:]) #prints everything after index 1

list1= ['physics', 'computerscience', 1998, 2000]
print(list1[0:2]) #prints everything between index 0 and 2 but not index 2

list1= ['physics', 'computerscience', 1998, 2000]
print(list1)
list1.append('calculus') #append adds more items to your list
print(list1)

list1= ['physics', 'computerscience', 1998, 2000]
list1[1] = 'computer Science' #this code updates the index1 value of list1
print(list1)
list1.append('calculus') #append adds more items to your list
print(list1)

list1= ['physics', 'computerscience', 1998, 2000]
list1[1] = 'computer Science' #this code updates the index1 value of list1
print(list1)
list1.append('calculus') #append adds more items to your list
print(list1)
list1.insert(2, 'calculus') #this code inserts a value at index2
print(list1)
#del list1[5] #this code deletes index5 on list1
list1.remove(list1[5]) #this is another code that deletes index5 on list1
print(list1)

list2= [45, 5.4, 89, 9, 7, 1]
list1= list1 + list2 #adds the item on list1 and list2 together and adds it to list1
print(list1)

print(list1[-3]) #this starts the list from the highest index listed (which starts at -1) to index0
print("The length of the list is", len(list1)) #len tells you the size of your list

for i in list1:
    print(i) #prints all the indexes in list1

flag = 45 in list2 #this code searches if the value 45 is actually in list2, it will be display true or false
print(flag)

list2.sort() #sort will return the list sorted in ascending order)
print("After sorting the items in list 2", list2)

for i in range(len(list1)):
    print(i+1)