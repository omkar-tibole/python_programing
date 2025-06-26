# """
# Variable:
#         Variables is like a container that hold's data

        

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
        
# """


# # Example
# # Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"


# # Example
# # Illegal variable names:
# """

# 2myvar = "John"
# my-var = "John"
# my var = "John"

# """



# # Camel Case
# # Each word, except the first, starts with a capital letter:

# myVariableName = "John"



# # Pascal Case
# # Each word starts with a capital letter:

# MyVariableName = "John"




# # Snake Case
# # Each word is separated by an underscore character:

# my_variable_name = "John"




#  # this is integer type data
# a=12  
# # We  can Print the type of any operator using type Function
# print(type(a))    

# # this is String value
# b="Hello World"  
# print(type(b))

# # This is a Boolean Value
# c=True   
# print(type(c))

#  # This is a None value
# d=None   
# print(type(d))



# # Multiple variable assignment
# x, y, z = 1, 2, 3
# print(x, y, z)

# # Assigning the same value to multiple variables
# a = b = c = "Python"
# print(a, b, c)

# # Unpacking a collection
# fruits = ["apple", "banana", "cherry"]
# f1, f2, f3 = fruits
# print(f1, f2, f3)

# # Variable reassignment
# num = 10
# print(num)
# num = "Now I'm a string"
# print(num)
# # String operations examples

# String = " Hello Friend I am a Student  !"
# print(String.upper())
# print(String.lower())
# print(String.isupper())
# print(String.find("e"))
# print(String.index("e"))
# print(String.isupper())
# print(String.islower())
# print(String.count("l"))
# print(String.strip(" "))
# print(String.rstrip("!"))
# print(String.replace("Hello", "hello"))
# print(String.endswith("!"))
# print(String.startswith(" "))
# print(String.title())
# print(String.swapcase())
# print(String.istitle())
# print(String.capitalize())
# print(String.isprintable())
# print(String.isalnum())
# print(String.split(" "))
# print(String.isalpha())
# print(String.isspace())
# print(String.center(60))

# # access index value 
# print(String[2])

# # count()
# # this is use to count 
# s = String.count("l")
# print(s)

# # upper() 
# # upper() method convert a string upper case
# print(String.upper())

# # lower()
# # lower() method covert a string lower case
# print(String.lower())

# # Find()
# # find() is used find the index given specific element
# print(String.find("F"))

# # Strip()
# # strip() is used to remove starting blank space and ending space
# print(String.strip())

# print(String.rstrip("!"))

# print(String.replace("!", "ram"))
# print(String.split())
# print(String)

# print(String.endswith(" "))
# print(String.replace("!", "ok"))
# print(String.index("e"))
# print(String.find("o"))
# print(String.isupper())
# print(String.islower())
# # print(String.isalsum())  # Typo: should be isalnum()
# print(String.strip())
# print(String.rstrip("!"))
# print(String.swapcase())
# print(String.capitalize())
# print(String.isdecimal())
# # print(String.isca)  # Incomplete method
# print(String.split(" "))
# print(String.startswith("H"))
# print(String.endswith(" "))




fruit=["mango","bannana","apple"]
f1,f2,f3=fruit
print(f1)
print(f2)
print(f3)
print(type(f1))
print(type(fruit)) 


print("hello")