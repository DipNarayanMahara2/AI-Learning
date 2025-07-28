# Function : A function is a reusable block of code that perform a specific task. It helps to organize the code, repitation and make program more readable.

# syntax :
# def function_name():
#   code here....

# def -> keyword to define the function
#function_name -> name of the function

# we have to call the function to run the function. It is called like this
# function_name()

# Example: function to add two number
def sum(): # defining function
  a=10
  b=20      # body of the function
  add = a + b
  print(add)

sum()  #function call

# We can also use parameterin function.
# Example : 
def add(num1, num2): # Function defination with parameter
  print(num1 + num2)

add(10,20)    # function call with parameter sending to function
