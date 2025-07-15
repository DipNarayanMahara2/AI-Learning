
# Conditionals : Conditionals helps your progam to make decisions. You can execute defferent ode blocks depending whether certain condtions are true

# Syntax :
# if condtions_here :
  # code to run if condition is true
# elif another_condition_here :
  # code to run if another condition is true
# else :
  # if both if and elif condition is false then else will be executed

# 🟢 Question 1
# Write a program that takes a number as input.
# Print "Positive" if it is greater than zero.
# Print "Zero" if it is exactly zero.
# Print "Negative" if it is less than zero.

number = int(input("Enter a number: "))
if number == 0:
  print("The number is zero")
elif number > 0:
  print("The number is positive")
else :
  print("The number is negative")

# 🟢 Question 2
# Take a person's age as input.
# Print "Child" if age ≤ 12.
# Print "Teenager" if 13 ≤ age ≤ 19.
# Print "Adult" if 20 ≤ age ≤ 59.
# Print "Senior" if age ≥ 60.

person_age = int(input("Enter your age: "))
if person_age <= 12:
  print("Your are a child")
elif person_age >= 13 and person_age <= 19:
  print("You are a teenager")
elif person_age >= 20 and person_age <= 59:
  print("You are an adult")
else:
  print("You are a senior")

# 🟢 Question 3
# Ask the user to enter a year.
# Check and print whether it is a leap year or not.
# (Hint: A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisible by 400.)

year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100  != 0 or year % 400 == 0):
  print(year," This year is a leap year")
else :
  print(year, " This year is not a leap year")

# 🟢 Question 4
# Ask the user to input two numbers and print which one is larger, or if they are equal.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 == num2 :
  print("Both numbers are equal..")
elif num1 > num2:
  print(num1," numbers is greater than ", num2)
else :
  print(num2," numbers is greater than ", num1)

# 🟢 Question 5
# Ask the user to enter a character.
# Check whether it is a vowel or a consonant.
# (Hint: Check if character is in 'aeiouAEIOU')

character = input("Enter a character: ")[0].lower() #converting into lower case
# First and long approach
# if character == "A" or character == "a":
#   print(character," This is an vowel letter")
# elif character =="E" or character == "e":
#   print(character," This is a vowel letter")
# elif character =="I" or character == "i":
#   print(character," This is a vowel letter")
# elif character =="O" or character == "o":
#   print(character," This is a vowel letter")
# elif character =="U" or character == "u":
#   print(character," This is a vowel letter")
if character in 'aeiou':
  print(character," This is a vowel letter")
else :
  print(character," This is a consonant letter")


# 🟢 Question 6
# Take a number as input.
# Print "Even" if it is divisible by 2, else print "Odd".

num = int(input("Enter a number: "))
if num % 2 == 0:
  print(num, " The number is even")
else :
  print(num, " The number is odd")

# 🟢 Question 7
# Ask the user to enter a mark (0–100).
# Print "Fail" if < 40.
# Print "Pass" if 40–59.
# Print "Good" if 60–79.
# Print "Excellent" if 80–100.
# Print "Invalid Marks" otherwise.

mark = float(input("Enter mark you obtain: "))
if mark >=80 and mark <=100:
  print(mark, "Excellent")
elif mark >= 60 and mark <=79:
  print(mark, " Good")
elif mark >=40 and mark <=59:
  print(mark, " Pass")
elif mark < 40 :
  print(mark, " Fail")
else :
  print("Invalid mark")

# 🟢 Question 8
# Ask for the day number (1 to 7).
# Print the corresponding day name (e.g., 1 = "Monday", 2 = "Tuesday", etc.).
# Print "Invalid day number" if outside 1–7.

day_number = int(input("Enter day number: "))
if day_number == 1:
  print("Monday")
elif day_number == 2:
  print("Tuesday")
elif day_number == 3:
  print("Wednesday")
elif day_number == 4:
  print("Thursday")
elif day_number == 5:
  print("Friday")
elif day_number == 6:
  print("Saturday")
elif day_number == 7:
  print("Sunday")
else : 
  print("Invalid day number..")

# 🟢 Question 9
# Ask for a number.
# Check and print whether it is a multiple of 5 or not.

num = int(input("Enter a number: "))
if num % 5 == 0:
  print(num, " is multiple of 5")
else:
  print(num, " is not a multiple of 5")

# 🟢 Question 10
# Input three numbers.
# Print the largest of the three.

num1 = int(input("Enter first Number: "))
num2 =int(input("Enter second number: "))
num3 = int(input("Enter third number:"))
if num1>num2 and num1>num3:
  print(num1, "is the largest among ", num2, "and", num3)
elif num2>num1 and num2>num3:
  print(num2, "is the largest among ", num1, "and", num3)
else :
  print(num3, "is the largest among ", num1, "and", num2)
