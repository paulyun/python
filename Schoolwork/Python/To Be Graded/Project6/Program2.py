#Program created by Paul Yun 4/19/2016.
#Gathers user name, three test scores, and evaluates test score average
#Displays username and test scores grade.

student_name = str(input("What is your name?"))

def evaluate_grade(x, y , z):
    sum = (x + y + z) / 3
    return sum
    
grade1 = float(input("Enter the grade for your first exam"))
grade2 = float(input("Enter the grade for your second exam"))
grade3 = float(input("Enter the grade for your third exam"))

if (evaluate_grade(grade1, grade2, grade3)>=90):
    print(student_name, "You received an A")
elif (evaluate_grade(grade1, grade2, grade3)>=80):
    print(student_name, "You received a B")
elif (evaluate_grade(grade1, grade2, grade3)>=70):
    print(student_name, "You received a C")
elif (evaluate_grade(grade1, grade2, grade3)<=69):
    print(student_name, "You received a F")