# loops :  A loop is used to excute the same code multiple times.

# there are two types of loop in python
# 1. while Loop
# 2. For loop

# 1. While Loop: A while loop repeats a code as long as statement or condition is true

#For example :
# count = 1
# while count <=5:
#   print(count)
#   count += 1
# The loop will start from 1 and end to 5 print 1 to 5.

# 2. For Loop : A for loop is uses to iterate over a sequence(like list, string, range etc)

# for example :

# for i in range(1,6):
#   print(i)

# the for loop will execute the from 1 to 5 exluding 6 from it.
# Printing 1 to 5.

# 💪 Day 3 — Practice Set: Loops
# 🟢 Question 1: Print numbers 1 to 10
# Write a program using a while loop that prints numbers from 1 to 10.

num =1 
while num <=10:
  print(num)
  num += 1

# 🟢 Question 2: Sum of first n natural numbers
# Ask the user to input a number n.
# Print the sum of first n natural numbers (1 + 2 + ... + n).

num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num :
  sum = sum + i
  i += 1
# print("The sum of first ", num, 'is: ', sum)

# 🟢 Question 3: Factorial of a number
# Take a number as input.
# Calculate and print its factorial using a for loop.
# (Factorial of n = n × (n-1) × (n-2) × ... × 1)

num = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= num:
  factorial = factorial * i
  i += 1
print(factorial)

# 🟢 Question 4: Multiplication table
# Ask the user to enter a number.
# Print its multiplication table up to 10.

num = int(input("Enter a number: "))

for i in range (1,11):
  print(num,"*",i,"= ", num*i)

# 🟢 Question 5: Count digits
# Ask user to enter a number.
# Count and print how many digits are in it.
# (Hint: Use a while loop and repeatedly divide by 10.)

num = int(input("Enter a number: "))
count = 0
if num == 0:
  count = 1
else :
  while num != 0:
    num = num // 10
    count += 1
print("The total number of digit is = ", count)

# 🟢 Question 6: Sum of digits
# Ask user to enter a number.
# Find and print the sum of its digits.

num = int(input("Enter a number : "))
sum_digits = 0
while num != 0:
  digit = num % 10 # get the last number
  sum_digits += digit
  num = num // 10 # remove the last number
print("Sum of digits is: ", sum_digits)

# 🟢 Question 8 (LeetCode inspired): Check palindrome number
# Ask user to enter a number.
# Check if it is a palindrome number (same forward and backward).
# Print "Palindrome" or "Not Palindrome".

num = int(input("Enter a number: "))
original = num
reversed_number = 0
while num != 0:
  digit = num % 10
  reversed_number = reversed_number * 10 + digit
  num = num // 10
if original == reversed_number:
  print("Palindrome")
else:
  print("Not Palindrome")

# 🟢 Question 9 (HackerRank style): Print all even numbers between two numbers
# Ask for two numbers (start and end).
# Print all even numbers between them (inclusive).

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter second number: "))
print("All even numbers between ", num1 ,"and", num2 ,"is: ")
while num1 <=num2:
  if num1 % 2 == 0:
    print(num1, end =" ")
  num1 += 1

# 🟢 Question 10 (LeetCode easy): FizzBuzz
# Write a program that prints numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz".

num = int(input("Enter a number: "))

for i in range(1, num+1):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

# ⭐ Question 11
# Print a pattern like this (if n = 5):
# *
# **
# ***
# ****
# *****

num = int(input("Enter a number: "))

for i in range (num):
  for j in range(i):
    print("*", end="")
  print()