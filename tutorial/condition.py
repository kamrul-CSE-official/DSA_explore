marks = int(input("What is your marks in programming: "))

def show_grade(grade):
    print(f"You got: {grade}")

if marks >= 80:
    show_grade("A+")
elif marks < 80 and marks >= 70:
    show_grade("A")
elif marks < 70 and marks >= 60:
    show_grade("A-")
elif marks >= 33:
    show_grade("Passed")
else:
    show_grade("F")


if marks >= 80 or marks <= 10:
    print("You are very good or very bad")
    if marks >= 80:
        print("Excellent")
    else: 
        print("Not so good")
else: 
    print("You are okay")


# 2

the_user_is_good = 80 < 60
print(the_user_is_good)