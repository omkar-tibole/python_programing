"""
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""

x = int(1)             # x will be 1 
y = int(2.8)           # y will be 2 
z = int("3")           # z will be 3 

x = float(1)           # x will be 1.0 
y = float(2.8)         # y will be 2.8 
z = float("3")         # z will be 3.0 
w = float("4.2")       # w will be 4.2 


x = str("s1")          # x will be 's1'
y = str(2)             # y will be '2'
z = str(3.0)           # z will be '3.0'






Int=55
Float=float(Int)
print(type(Float))
print(Float)

Str="55"
Int=int(Str)
print(type(Int))
print(Int)


# Adding of String and int
# Using type cast


String="5"                # this is string value
String_number=int(String) # change the type 
number=7                  # this is the numeric value

sum=number+String_number  
print(sum)


# Python program to demonstrate 
# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 


# b to float 
b = 3.0
print(type(b)) 


# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))


# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))
