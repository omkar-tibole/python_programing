"""
Datatype

Data type specities the type of value a variable holds


Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

# 1.Numeric Data: int,float,complex
# int:3,-3,0
# float:7.34
# complex:6*2i

# 2.Text Data:str 
# str:"hello world"

# 3.Boolean Data 
# Boolean Data consists of values True or false 

# Sequenced data: list,tuple 
# list :  list is a ordered collection of data with element sepreted by a Commaand enclosed within square bracket List are mutable and can be modified after creation
List=[8,2,3,[-4,5],["apple","Banana"]]
print(List)
print(type(List))


# Tuple : tuple same as list but tuple is immutable and can not be modified after creation


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Example	Data Type	Try it
x = "Hello World"
print(x)	                                          #  str	
x = 20	 
print(x)                                              #  int	
x = 20.5
print(x)	                                          #  float	
x = 1j	 
print(x)                                              #  complex	
x = ["apple", "banana", "cherry"]	
print(x)                                              #  list	
x = ("apple", "banana", "cherry")	 
print(x)                                              #  tuple	
x = range(6)	
print(x)                                              #  range	
x = {"name" : "John", "age" : 36}	
print(x)                                              #  dict	
x = {"apple", "banana", "cherry"}	
print(x)                                          #  set	
x = frozenset({"apple", "banana", "cherry"})	
print(x)                                        #  frozenset	
x = True	 
print(x)                                          #  bool	
x = b"Hello"	
print(x)                                       #  bytes	
x = bytearray(5)	
print(x)                                     #  bytearray	
x = memoryview(bytes(5))	 
print(x)                                    #  memoryview	
x = None	    
print(x)                                     #  NoneType	                    

