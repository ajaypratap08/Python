# ==============================
# BASIC PRINT STATEMENTS
# ==============================

# print("Hello World!")  

# for i in range(10):
#     print("AJAY")
# -> Loop runs 10 times
# -> range(10) = 0 to 9

# print(("Hello World!\n") * 10)
# -> Prints same string 10 times
# -> \n means new line


# ==============================
# VARIABLES
# ==============================

# x = 10          # integer variable
# print(x)

# y = "Ajay"      # string variable
# print(y)

# print(id(y))
# -> id() gives memory location/address of variable

# print(x + y)
# ERROR:
# -> Cannot add int + string directly

# Method if forgotten:
# print(str(x) + y)
# -> Convert int to string using str()

# print(x, y)
# -> Comma prints with space automatically


# ==============================
# USER INPUT
# ==============================

# name = input("Enter your name- ")
# -> input() always returns STRING

# print("Hello " + name)

# age1 = input("Enter Your Age- ")
# age2 = input("Enter Your Age- ")

# print(int(age1) + int(age2))
# -> Convert string to int using int()

# Easy Reminder:
# input() -> string
# int()   -> integer
# float() -> decimal number
# str()   -> string


# ==============================
# ROUND FUNCTION
# ==============================

# x = 3.1415757575

# y = round(x, 2)
# -> round(number, digits)
# -> keeps only 2 digits after decimal

# print(y)


# ==============================
# AREA OF CIRCLE
# ==============================

# dia = input("Enter diameter of the circle")

# print(y * float(dia) * float(dia))

# Note
# Formula used here is wrong for circle area

# Correct Formula:
# radius = diameter / 2
# area = pi * r * r

# Easy Method:
# pi = 3.14
# radius = float(dia) / 2
# print(pi * radius * radius)


# ==============================
# DATA TYPES IN PYTHON
# ==============================

# x = 10          # int
# y = 3.14        # float
# name = "Ajay"   # string
# is_adult = True # boolean

# print(type(x))
# -> type() tells datatype

# print(type(y))

# Common Data Types:
# int    -> whole number
# float  -> decimal number
# str    -> text/string
# bool   -> True/False


# ==============================
# TYPE CONVERSION
# ==============================

# a = 10
# b = 3.14

# print(a + b)
# -> implicit conversion
# -> int automatically converted to float

# print(a + int(b))
# -> explicit conversion
# -> float manually converted to int

# print(a == b)
# -> checks equality

# print(b < a)
# -> comparison operator

# Remember:
# ==  -> equal to
# !=  -> not equal to
# >   -> greater than
# <   -> smaller than
# >=  -> greater or equal
# <=  -> smaller or equal


# ==============================
# LOGICAL OPERATORS
# ==============================

# print(a == b and (b < a))
# -> AND returns True only if BOTH are True

# print(a == b or (b > a))
# -> OR returns True if ANY ONE is True

# print(not(a == b))
# -> NOT reverses result

# Easy Trick:
# and -> both
# or  -> any one
# not -> opposite


# ==============================
# STRINGS
# ==============================

# name = "Ajay"

# print(name[0])
# -> indexing starts from 0

# print(name[-1])
# -> negative indexing starts from end

# print(len(name))
# -> length of string

# print("Hello " + name)
# -> string concatenation


# ==============================
# STRING SLICING
# ==============================

# print(name[1:3])
# -> start included, end excluded

# print(name[:3])
# -> from start to index 2

# print(name[2:])
# -> from index 2 till end

# print(name[-4:-1])
# -> slicing using negative index

# Easy Formula:
# string[start:end]
# -> end index NOT included


# ==============================
# STRING METHODS
# ==============================

# s = "Hello World"

# print(s.upper())
# -> converts all letters to uppercase

# print(s.lower())
# -> converts all letters to lowercase

# print(s.title())
# -> first letter capital

# print(s.find("orld"))
# -> gives starting index of substring

# print(s.replace("o", "a"))
# -> replace old value with new value

# print(s.count("l"))
# -> counts occurrences

# print("a" not in "apple")
# -> membership operator

# More Useful Methods:
# s.strip()   -> removes spaces
# s.split()   -> converts string to list
# "-".join()  -> joins list into string


# ==============================
# CONDITIONAL STATEMENTS
# ==============================

# age = 18

# print(age >= 18)

# if(age >= 18):
#     print("You are an adult")

# else:
#     print("You are a minor")

# if condition:
#     code
# else:
#     code

# IMPORTANT:
# Python uses INDENTATION instead of { }


# ==============================
# GRADE SYSTEM
# ==============================

# marks = int(input("Enter your marks- "))

# if(marks >= 90):
#     print("Grade A")

# elif(marks >= 80):
#     print("Grade B")

# elif(marks >= 70):
#     print("Grade C")

# elif(marks >= 60):
#     print("Grade D")

# else:
#     print("Grade F")

# Structure Reminder:
#
# if(condition):
#     code
#
# elif(condition):
#     code
#
# else:
#     code


# ==============================
# IMPORTANT REVISION NOTES
# ==============================

# 1. input() always gives STRING
# 2. Indexing starts from 0
# 3. Python uses indentation
# 4. end index in slicing is excluded
# 5. == is comparison
# 6. = is assignment
# 7. int + str gives ERROR
# 8. Use type() to check datatype


# ==============================
# SMALL PRACTICE IDEAS
# ==============================

# 1. Take 2 numbers and print sum
# 2. Find square of number
# 3. Print even/odd
# 4. Reverse a string
# 5. Find largest of 3 numbers
# 6. Count vowels in string
# 7. Check palindrome