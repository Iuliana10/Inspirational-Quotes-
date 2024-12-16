# 1. gradingsystem

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'
def main():
    print("Welcome to the grading system")
    try:
        score= float(input("Enter the student's score (0-100): "))
        if 0<= score <= 100:
            grade = assign_grade(score)
            print("The student's grade is: ", grade)
        else:
            print("Score must be between 0 and 100.")
    except valueError:
        print("Please enter a valid number.")
if __name__== "__main__":
    main()

