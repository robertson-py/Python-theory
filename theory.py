# Python programming language

# Variables
# There are a space in computer's memory, where it'll contain a value that could change on the fly during de program execution.
# Type of variables and how to declare them
age = 10                    # Integer (int)
first_name = "Roberto"      # String (str)
height = 1.83               # Floating point number (float)
winning = True              # Boolean

# If/else statements
a = 10
b = 15

if a>b:
    print("a is bigger than b")
elif a<b:
    print("b is bigger than a")
else:
    print("a is equal b")

# In python there is no "switch" command as JavaScript
# but they can be made with if/else statements

# Functions
# In essence, they are a block of code that works as a one unit to do an especific job.
# Functions in python can return values and they can have arguments.
# When they are inside a class (OOP), we call them "methods"
# They've got a big utility that is code reusing.
# Let's see an example:


def name_printer(): # This function has no parameters
    name = input("Please, write your name: ")           # Local variable
    lastname = input("Please, write your lastname: ")   # Local variable
    
    # Here I show two different forms to format a string
    return f'Your name is {name} and your lastname is {lastname}'
    # return 'Your name is {name} and your lastname is {lastname}'.format(name=name, lastname=lastname)

def second_name_printer(name, lastname): # This function has parameters
    return f'Your name is {name} and your lastname is {lastname}'

# To interact with the second function, we have to pass through two parameters
# So, we have to declare a couple of variables first:
name = input("Please, write your name: ")           # Global variable
lastname = input("Please, write your lastname: ")   # Global variable

second_name_printer(name, lastname)

# Lists
# There are a data structure that let us store a big quantity of values (like an array in C or JavaScript).
# In python, lists can save different types of values.
friends_list = ["Joaquin", "Agustin", "Alvaro"]

# Tuples
# There are inmutable lists, they can't be modified.
friends_tuple = ("Joaquin", "Agustin", "Alvaro")

# Dictionaries
# The principal feature of this type of data structure is that data it's store associated
# The elements are not organized, the order is independent from the data stored.

player_features = {"attack": 15, "defense": 35, "move": 3}

# Other way to create a dictionary
player_two_features = {
    "attack": 10,
    "defense": 25,
    "move": 2
    }

# Loops
# For loop; let's see some examples

#Small program that prints 3 times i->10;
for i in range(0, 11):
    print(3*i)

#Small program that reads user's input, add it to a list and print the final list.
list_example = []
for i in range(0, 11):
    user = input("Write a number: ")
    list_example.append(user)

print(list_example)

# While loop; let's see some examples.

#Small program that prints 3 times i->10;
i = 0
while i <= 10:
    print(3*i)
    i += 1

#Small program that reads user's input, add it to a list and print the final list.
list_example_two = []
z = 0
while z <= 10:
    user = input("Write a number: ")
    list_example_two.append(user)
    z += 1

print(list_example_two)

# There are some features that we'll use later (continue, break, else)

#Exceptions
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try and except blocks.

try:
  print(z)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(x)  # The "x" variable is not declared, so it will go right to the except, and after to finally.
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")