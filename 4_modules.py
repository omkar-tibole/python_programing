# Modules 
"""
Create a Module
To create a module just save the code you want in a file with the file extension .py:
Basically modules are used to borrow someone else's code.Which means we can use someone else's code in your program with help of modules 

ExampleGet your own Python Server
Save this code in a file named mymodule.py

"""

def greeting(name):
  print("Hello, " + name)


# First Program
print("Hello World")


"""
Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:

"""


"""
Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

Example
Save this code in the file mymodule.py

"""

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}







# Python Comments : A Python comments means that code is not part coding files that the programer does not to excute.

# Single-Line-Code 

# You can write comments in Python you can use "#" special Charector
# for example : # this code was not execute 
print("This is a Print Statement")



# Multi-Line Comment 
# To write a Multi-line you can use "#" each line or you can use the multiple string 
print("Hello World")



def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# create a other file calling this function to that file
# ex.
# crete mani.py
# import mymodule

# mymodule.greeting("Amit")

# print(mymodule.person1["name"])



def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}


# crete a new file and call this method
# greeting("your name")


def add(a, b):
    return a + b


# crete a new file and call this method
# and import this file
# import modules

# add(integer,integer)

