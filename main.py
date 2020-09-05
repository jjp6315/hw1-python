# Author: Ji Woong Park jjp6315@psu.edu

letter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))

if letter1 == "A" or letter1 == "a":
  gradepoint1 = 4.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "A-" or letter1 == "a-":
  gradepoint1 = 3.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B+" or letter1 == "b+":
  gradepoint1 = 3.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B" or letter1 == "b":
  gradepoint1 = 3.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "B-" or letter1 == "b-":
  gradepoint1 = 2.67
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C+" or letter1 == "c+":
  gradepoint1 = 2.33
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "C" or letter1 == "c":
  gradepoint1 = 2.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "D" or letter1 == "d":
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}")

elif letter1 == "F" or letter1 == "f":
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")

else:
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}")


letter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if letter2 == "A" or letter2 == "a":
  gradepoint2 = 4.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "A-" or letter2 == "a-":
  gradepoint2 = 3.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B+" or letter2 == "b+":
  gradepoint2 = 3.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B" or letter2 == "b":
  gradepoint2 = 3.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "B-" or letter2 == "b-":
  gradepoint2 = 2.67
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C+" or letter2 == "c+":
  gradepoint2 = 2.33
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "C" or letter2 == "c":
  gradepoint2 = 2.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "D" or letter2 == "d":
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")

elif letter2 == "F" or letter2 == "f":
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

else:
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}")

letter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))

if letter3 == "A" or letter3 == "a":
  gradepoint3 = 4.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "A-" or letter3 == "a-":
  gradepoint3 = 3.67
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B+" or letter3 == "b+":
  gradepoint3 = 3.33
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B" or letter3 =="b":
  gradepoint3 = 3.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "B-" or letter3 == "b-":
  gradepoint3 = 2.67
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "C+" or letter3 == "c+":
  gradepoint3 = 2.33
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "C" or letter3 == "c":
  gradepoint3 = 2.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "D" or letter3 == "d":
  gradepoint3 = 1.0
  print(f"Grade point for course 2 is: {gradepoint3}")

elif letter3 == "F" or letter3 == "f":
  gradepoint3 = 0.0
  print(f"Grade point for course 2 is: {gradepoint3}")

else:
  gradepoint3 = 0.0
  print(f"Grade point for course 2 is: {gradepoint3}")

GPA = float(gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3) 

print(f"Your GPA is: {GPA}")