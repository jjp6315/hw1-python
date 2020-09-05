# Author: Ji Woong Park jjp6315@psu.edu

letter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
if letter1 == "A" or "a":
  gradepoint1 = 4.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "A-" or "a-":
  gradepoint1 = 3.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B+" or "b+":
  gradepoint1 = 3.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B" or "b":
  gradepoint1 = 3.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B-" or "b-":
  gradepoint1 = 2.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C+" or "c+":
  gradepoint1 = 2.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C" or "c":
  gradepoint1 = 2.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "D" or "d":
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "F" or "f":
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")

else:
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")


letter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if letter2 == "A" or "a":
  gradepoint2 = 4.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "A-" or "a-":
  gradepoint2 = 3.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B+" or "b+":
  gradepoint2 = 3.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B" or "b":
  gradepoint2 = 3.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B-" or "b-":
  gradepoint2 = 2.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C+" or "c+":
  gradepoint2 = 2.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C" or "c":
  gradepoint2 = 2.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "D" or "d":
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "F" or "f":
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

else:
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

letter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))

if letter3 == "A" or "a":
  gradepoint3 = 4.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "A-" or "a-":
  gradepoint3 = 3.67
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B+" or "b+":
  gradepoint3 = 3.33
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B" or "b":
  gradepoint3 = 3.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B-" or "b-":
  gradepoint3 = 2.67
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "C+" or "c+":
  gradepoint3 = 2.33
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "C" or "c":
  gradepoint3 = 2.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "D" or "d":
  gradepoint3 = 1.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "F" or "f":
  gradepoint3 = 0.0
  print(f"Grade point for course 2 is: {gradepoint3}")

else:
  gradepoint3 = 0.0
  print(f"Grade point for course 2 is: {gradepoint3}")

GPA = float(gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

print(f"Your GPA is: {GPA}")