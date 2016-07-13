#Test Score Average
#Paul_Yun CS_902 Spring 2016

test_score_one = float(input("Enter your first test score"))
test_score_two = float(input("Enter your second test score"))
test_score_three = float(input("Enter your three test score"))

test_score_average = (test_score_one + test_score_two + test_score_three) / 3

if (test_score_average>=90):
    print("You received an A")
elif (test_score_average>=80):
    print("You received an B")
elif (test_score_average>=70):
    print("You received an C")
elif (test_score_average>=60):
    print("You received an D")
elif (test_score_average>=50):
    print("You received an F")
elif (test_score_average<=50):
    print("You received an F")