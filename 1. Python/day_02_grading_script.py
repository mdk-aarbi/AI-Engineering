# a simple grading script (marks in, letter grade out).

marks = float(input("Enter the marks out of 100: "))

if marks >= 85 and marks <= 100:
    print("Grade = A")
elif marks > 79 and marks < 85:
    print("Grade = A-")
elif marks > 74 and marks < 80:
    print("Grade = B+")
elif marks > 70 and marks < 75:
    print("Grade = B")
elif marks > 67 and marks < 71:
    print("Grade = B-")
elif marks > 63 and marks < 68:
    print("Grade = C+")
elif marks > 60 and marks < 64:
    print("Grade = C")
elif marks > 57 and marks < 61:
    print("Grade = C-")
elif marks > 53 and marks < 58:
    print("Grade = D+")
elif marks > 49 and marks < 54:
    print("Grade = D")
elif marks > 0 and marks < 50:
    print("Grade = F")
else:
    print("Invalid input. Try again.")