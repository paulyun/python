names_list=[]
grades_list = []
avg_list=[]
letter_grades= []
name_size = int(input("Enter the number of students you want to add to the list: "))
grades_size= int(input("Enter the number of scores you want to input for each student: "))

for i in range(name_size):
    names_list.append(input("Enter student "+str(i+1)+"'s name: "))
    
for i in range(name_size):
    scores=[]
    for p in range(grades_size):
        scores.append(float(input("Enter score "+ str(p+1) +" for student "+ names_list[i]+ ": ")))
        if p == (grades_size - 1):
            grades_list.append(scores)


for i in range(name_size):
    average = sum(grades_list[i]) / (grades_size)
    avg_list.append(average)
    
for item in (avg_list):
    if (item >= 90):
        letter_grades.append("A")              
    elif (item>= 80 and item < 90):
        letter_grades.append("B")
    elif (item >= 70 and item < 80):
        letter_grades.append("C")
    elif (item >= 60 and item < 70):
        letter_grades.append("D")
    elif (item < 60):
        letter_grades.append("F")


for i in range(name_size):
    print(names_list[i]+ "'s test average is", format(round(avg_list[i],2)))
    print(names_list[i]+ "'s letter grade is an", letter_grades[i])