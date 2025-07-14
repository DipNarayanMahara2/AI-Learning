
import math
import datetime

#vairables 
# A variable is a container which store a data or values

# Practice 1 : BMI calulator:
# Take weight (kg) and height (m) as input.
# Calculate BMI = weight / (height²).
# Print the BMI value and a message (e.g., “You are underweight,” “Normal,” “Overweight,” etc.).

weight = float(input("Enter your weight(in kg): "))
height = float(input("Enter your height(in meter): "))
#Here weight is variable and input is command which ask use to give data or value.
#Float is used to convert the input value data type to float

BMI = weight / (height * height)

if BMI < 18.5 :
  print(BMI, "Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
  print(f"{BMI:.2f} Normal")
elif BMI >= 25.0 and BMI <=29.9:
  print(BMI, "Overweight")
else:
  print(BMI, "Obese")


# 🟢 Extra Practice Exercises
# 1️⃣ Simple Calculator
# Take two numbers from the user.
# Ask which operation they want: add, subtract, multiply, divide.
# Perform the operation and print the result.

first_number = int(input("Enter First Number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter what you wanna do (eg: +, -, *, %): ")

if operator == "+":
  total_sum = first_number + second_number
  print(first_number, operator , second_number, "= ", total_sum)
elif operator == "-":
  subtraction = first_number - second_number
  print(first_number, operator, second_number, "= ", subtraction)
elif operator == "*":
  multiply = first_number * second_number
  print(first_number, operator, second_number, "= ", multiply)
elif operator == "/":
  if second_number == 0:
    print("Cannot divide by zero ")
  else:
    division = first_number / second_number
    print(first_number, operator, second_number, "= ", division)
elif operator == "%":
  reminder = first_number % second_number
  print(first_number, operator, second_number, "= ", reminder)
else:
  print("Invalid Operation...")



# 2️⃣ Temperature Converter
# Ask user to input temperature in Celsius.
# Convert it to Fahrenheit using:
# 𝐹=( 𝐶 × 1.8 ) + 32 F=(C×1.8)+32
# Print both values.

temperature = float(input("Enter your temperature(in Celsius): "))
f = (temperature * 1.8) + 32

print("Your temperature in Celsius: ",temperature)
print(f"Your temperature in fahrenheit: {f:.2f}")


# 3️⃣ Area of a Circle
# Take the radius as input.
# Calculate area:
# 𝐴 = 𝜋*r*r
# Use math.pi from Python's math library.

radius = float(input("Enter radius: "))
pi = math.pi

area = pi * radius * radius
print(f"The area of circle is : {area:.2f}")
 

# 4️⃣ Age in Days Calculator
# Ask user for their age in years.
# Calculate and print approximate age in days (ignoring leap years for simplicity).

DOB = int(input("Enter your Date of Birth(in years): "))
current_year = datetime.datetime.now().year
age = current_year - DOB
age = age * 365
print("Your current age in days: ", age)

# 5️⃣ Swapping Values
# Take two numbers as input.
# Swap their values (without using a third variable if possible).
# Print before and after values.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Values before swap: ", num1, " and ", num2 )

num1 , num2 = num2, num1
print("Values after swap: ", num1, " and ", num2 )

