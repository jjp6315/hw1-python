# Author: Ji Woong Park jjp6315@psu.edu

letter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
gradepoint1 = float(input("Grade point for course 1 is: ")) 

letter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
gradepoint2 = float(input("Grade point for course 2 is: ")) 

letter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))
gradepoint3 = float(input("Grade point for course 3 is: ")) 

GPA = float(gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

print(f"Your GPA is: {GPA}")