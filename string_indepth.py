# Strings in Python

# String kya hoti hai?
#
# String characters (letters, numbers, symbols) ka collection hoti hai.
#
# String ko hum
#
# Single Quotes (' ')
# Double Quotes (" ")
# Triple Quotes (''' ''' ya """ """)
#
# mein likh sakte hain.


# Creating a String

name = "Ibrahim"

print(name)

# Output:
#
# Ibrahim


# String Indexing

# String ke har character ka apna index hota hai.

# Example

#  I  b  r  a  h  i  m
#  0  1  2  3  4  5  6

# Negative Index

#  I   b   r   a   h   i   m
# -7  -6  -5  -4  -3  -2  -1

# Positive indexing left se start hoti hai.

print(name[0])     # I
print(name[1])     # b
print(name[2])     # r
print(name[3])     # a
print(name[4])     # h
print(name[5])     # i
print(name[6])     # m


# Negative Indexing

print(name[-1])    # m
print(name[-2])    # i
print(name[-3])    # h
print(name[-4])    # a


# String Slicing

# Syntax

# string[start : end]

# Important Rule

# Start Index include hota hai.
# End Index include nahi hota.

# Matlab

# [0:3]

# 0 include hoga
# 3 include nahi hoga.

print(name[0:3])

# Output

# Ibr


print(name[1:3])

# Output

# br


print(name[0:8])

# Output

# Ibrahim

# String ki length 7 hai.
#
# Lekin agar end index zyada de do
#
# Python Error nahi deta.
#
# Jitna available hoga utna return kar dega.


# More Slicing Examples

print(name[2:5])

# Output

# rah


print(name[3:])

# Output

# ahim

# Agar end index na do
#
# To Python last character tak le jata hai.


print(name[:4])

# Output

# Ibra

# Agar start index na do
#
# To Python 0 se start karta hai.


print(name[:])

# Output

# Ibrahim

# Iska matlab
#
# Complete String.


# Negative Slicing

print(name[-4:-1])

# Output

# ahi

# Explanation

# -4 = a
# -3 = h
# -2 = i
# -1 = m (include nahi hoga)


# Step Slicing

# Syntax

# string[start:end:step]

print(name[0:7:1])

# Output

# Ibrahim

# Har character lo.


print(name[0:7:2])

# Output

# Irhm

# Har doosra character.


print(name[::2])

# Output

# Irhm


print(name[::-1])

# Output

# miharbI

# String Reverse.


# String Length

print(len(name))

# Output

# 7


# Strings are Immutable

# Immutable ka matlab

# String ko modify nahi kar sakte.

# Wrong

# name[0] = "A"

# Output

# TypeError

# Agar value change karni hai

name = "Ahmed"

print(name)

# Yahan purani string modify nahi hui.
#
# Nayi string create hui.


# String Concatenation

first_name = "Shaikh"

last_name = "Ibrahim"

full_name = first_name + " " + last_name

print(full_name)

# Output

# Shaikh Ibrahim


# String Repetition

print("Python " * 3)

# Output

# Python Python Python


# Membership Operator

print("I" in name)

# Output

# True


print("z" in name)

# Output

# False


print("z" not in name)

# Output

# True


# Escape Characters

print("Hello\nWorld")

# New Line


print("Hello\tWorld")

# Tab Space


print("He said \"Python is Awesome\"")

# Double Quotes


print('It\'s Python')

# Single Quote


# Common String Methods

text = "python learning"

print(text.upper())

# PYTHON LEARNING


print(text.lower())

# python learning


print(text.title())

# Python Learning


print(text.capitalize())

# Python learning


print(text.replace("python", "Java"))

# Java learning


print(text.startswith("python"))

# True


print(text.endswith("learning"))

# True


print(text.find("learn"))

# 7


print(text.count("n"))

# 3


print(len(text))

# Length


# Removing Spaces

message = "     Ibrahim     "

print(message.strip())

# Remove both side spaces


print(message.lstrip())

# Remove left spaces


print(message.rstrip())

# Remove right spaces


# Splitting String

course = "HTML,CSS,JavaScript,Python"

print(course.split(","))

# Output

# ['HTML', 'CSS', 'JavaScript', 'Python']


# Joining String

languages = ["HTML", "CSS", "Python"]

print(" | ".join(languages))

# Output

# HTML | CSS | Python


# String Formatting

name = "Ibrahim"
age = 22

print(f"My name is {name} and I am {age} years old.")

# f-string
# Modern aur Recommended Way


# Summary

# String = Characters ka collection.

# String Indexing starts from 0.

# Negative indexing bhi hoti hai.

# Slicing ka syntax:

# string[start:end:step]

# Start include hota hai.

# End include nahi hota.

# Strings Immutable hoti hain.

# len() length batata hai.

# Upper(), lower(), replace(), split(), join()
# sab commonly use hone wale methods hain.

# f-string string formatting ka best aur modern tareeqa hai.