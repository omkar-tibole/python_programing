
"""

Python Operators

Operators are used to perform operations on variables and values.

"""

# 1.Arithmatic Operator

# Addition
a=int(input("Enter value "))
b=int(input("Enter value "))

c=a+b

print(f"Output : {c}")


# Substraction 
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

c=a-b

print(f"Output : {c}")



# Multiplication
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

c=a*b

print(f"Output : {c}")



# Exponentiation
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

c=a**b

print(f"Output : {c}")



# Floor Division
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

c=a//b

print(f"Sub : {c}")

# Division 
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

c=a/b

print(f"Sub : {c}")



#2.Assignment operators
'''Assignment operators are used to assign values to variables'''

# '=' Operator 
a=10
print(a)


# '+=' 
a+=10
print(10)





#3.Comparision Operator


# '=='	Equal	
a=10
b=10
print(a==b)



# '!='  Not equal	
a=10
b=20
print(b!=a)



# '>'	Greater than
a=20
b=10
print(a>b)



# '<'	Less than
a=10
b=20
print(a>b)




# '>='	Greater than or equal to	

a=10
b=10
print(a>=b)



# '<='	Less than or equal to	

a=10
b=10
print(a<=b)



#4.Logical Operators
# Logical operators are used to combine conditional statements


# 'and' 	Returns True if both statements are true
x=11
if x >=0 and  x < 10:
    print("This value is less than 10")
else:
    print("This value is greater than 10")
	

# 'or'	Returns True if one of the statements is true	
x=5
if  x < 5 or x < 4:
    print(x)
else:
    print("this value is not greater than 5 or less than 4")




# not	Reverse the result, returns False if the result is true	
x=10
if not(x < 5 and x < 10):
    print(x)
else:
    print("Invalide number")






# 5.Identity Operators

# 'is' 	Returns True if both variables are the same object
x = ["apple", "mango"]
y = ["apple", "mango"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

	




# 'is not'	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y






# 6.Membership Operators
# Membership operators are used to test if a sequence is presented in an object


# 'in' 	Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list




# 'not in'	Returns True if a sequence with the specified value is not present in the object
x = ["mango", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
