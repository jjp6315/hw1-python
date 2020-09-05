# Author: Ji Woong John Park jjp6315@psu.edu

letter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))

if letter1 == "A":
  gradepoint1 = 4.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "A-":
  gradepoint1 = 3.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B+":
  gradepoint1 = 3.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B":
  gradepoint1 = 3.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B-":
  gradepoint1 = 2.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C+":
  gradepoint1 = 2.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C":
  gradepoint1 = 2.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "D":
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "F":
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")

else:
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")


letter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if letter2 == "A":
  gradepoint2 = 4.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "A-":
  gradepoint2 = 3.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B+":
  gradepoint2 = 3.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B":
  gradepoint2 = 3.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B-":
  gradepoint2 = 2.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C+":
  gradepoint2 = 2.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C":
  gradepoint2 = 2.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "D":
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "F":
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

else:
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

letter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))

if letter3 == "A":
  gradepoint3 = 4.0
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "A-":
  gradepoint3 = 3.67
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "B+":
  gradepoint3 = 3.33
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "B":
  gradepoint3 = 3.0
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "B-":
  gradepoint3 = 2.67
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "C+":
  gradepoint3 = 2.33
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "C":
  gradepoint3 = 2.0
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "D":
  gradepoint3 = 1.0
  print(f"Grade point for course 3 is: {gradepoint3}")

elif letter3 == "F":
  gradepoint3 = 0.0
  print(f"Grade point for course 3 is: {gradepoint3}")

else:
  gradepoint3 = 0.0
  print(f"Grade point for course 3 is: {gradepoint3}")

GPA = float(gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

print(f"Your GPA is: {GPA}")