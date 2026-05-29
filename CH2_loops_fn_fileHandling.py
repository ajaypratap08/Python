# # =========================
# # Loops in Python
# # =========================

# # While Loop
# # Print numbers from 1 to 5

# # num = 1
# # while num <= 5:
# #     print(num)
# #     num += 1


# # Check even and odd numbers from 1 to 20

# # num = 1
# # while num <= 20:
# #     if num % 2 != 0:
# #         print(num)          # Odd number
# #     else:
# #         print("Even number")
# #     num += 1


# # Pattern Printing
# # *
# # **
# # ***
# # ****

# # i = 1
# # while i <= 4:
# #     print("*" * i)
# #     i += 1


# # =========================
# # For Loop
# # =========================

# # range(start, end, step)

# # for i in range(1, 6, 1):
# #     print(i)


# # Countdown Program

# # import time

# # for i in range(5, -1, -1):
# #     print(i)
# #     time.sleep(1)   # Wait for 1 second

# #     if i == 0:
# #         print("Blastoff")


# # =========================
# # Functions in Python
# # =========================

# # Simple Function

# def sum1():
#     a = 4
#     b = 4
#     print("Sum =", a + b)

# sum1()


# # Parameterized Function
# # Values passed inside function

# def sum2(a, b, c):
#     print("Sum =", a + b + c)

# sum2(4, 5, 6)


# # Default Parameters
# # Default values used if no argument passed

# def fn(a=5, b=6, c=7):
#     print("Sum =", a + b + c)

# fn()
# fn(4, 6, 0)


# # Function with String Formatting

# def data(name, age):
#     print(f"{name} is {age} years old")

# data("Alice", 30)
# data("Ajay", 25)


# # Return Keyword
# # Function returns value

# def multiply(a, b):
#     return a * b

# result = multiply(4, 5)
# print("Multiplication =", result)


# # Square Function

# def square(num):
#     return num ** 2

# print("Square of 5 =", square(5))


# # Count vowels and consonants

# def count(word):
#     vowels = 0
#     consonants = 0

#     vowel_set = ('a', 'e', 'i', 'o', 'u')

#     for i in word.lower():

#         # Ignore spaces
#         if i == " ":
#             continue

#         if i in vowel_set:
#             vowels += 1
#         else:
#             consonants += 1

#     return vowels, consonants


# v, c = count("Hello World")
# print(f"Vowels = {v} and Consonants = {c}")


# # =========================
# # File Handling in Python
# # =========================

# # open("filename", "mode")
# # Modes:
# # r -> read
# # w -> write
# # a -> append

# # Reading a file

# file = open("demofile.txt", "r")

# data = file.read()

# # Print full file data
# print(data)

# # Find word in file
# x = data.find("Python")

# if x != -1:
#     print("Word Found")
# else:
#     print("Word Not Found")


# # Another way to check word

# if "Python" in data:
#     print("Yes")
# else:
#     print("No")

# file.close()


# # Writing into a file
# # File created automatically if not present

# file = open("demofile1.txt", "w")

# file.write("This is new File I made\n")
# file.write("This is second line\n")
# file.write("Learning Python File Handling")

# file.close()


# # =========================
# # with Keyword
# # Automatically closes file
# # =========================

# # Read full file

# with open("demofile.txt", "r") as f:
#     data = f.read()
#     print(data)


# # Read only one line

# with open("demofile.txt", "r") as f:
#     data = f.readline()
#     print(data)


# # Read all lines in list format

# with open("demofile.txt", "r") as f:
#     data = f.readlines()
#     print(data)


# # =========================
# # OS Module
# # File Operations
# # =========================

# import os

# # Rename file
# os.rename("demofile.txt", "newfile.txt")

# # Delete file
# os.remove("demofile1.txt")