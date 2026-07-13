# Indentation in Python

# Indentation ka matlab hota hai:
# Code ki line ke shuru mein spaces ya tab dena.

# Python mein indentation sirf code ko beautiful banane ke liye nahi hoti.
# Ye Python ki syntax ka hissa hai.
# Agar indentation galat ho to program Error dega.


# Example 1

if True:
    print("Hello Ibrahim")

print("Program End")

# Yahan
#
# if True:
#
# ke baad jo line hai uske shuru mein 4 spaces hain.
#
# Ye batata hai ke ye line if block ke andar hai.
#
# Output:
#
# Hello Ibrahim
# Program End


# Example 2

age = 20

if age >= 18:
    print("You can vote")

print("Done")

# Sirf print("You can vote")
# if block ke andar hai.
#
# print("Done")
# if ke bahar hai.
#
# Isliye Done hamesha print hoga.


# Example 3

number = 10

if number > 5:
    print("Greater than 5")
    print("This line is also inside if")
    print("Still inside if")

print("Outside if")

# Jitni lines same indentation mein hongi
# wo sab if block ke andar hongi.


# Example 4

number = 2

if number > 5:
    print("Greater than 5")

print("Program Finished")

# number > 5 False hai.
#
# Isliye if ke andar wala code execute nahi hoga.
#
# Lekin
#
# Program Finished
#
# phir bhi print hoga.


# Example 5

marks = 80

if marks >= 50:
    print("Pass")

    print("Congratulations")

    print("Keep Learning")

print("End")

# Teenon print statements if ke andar hain.
#
# Kyun?
#
# Kyun ke teenon ki indentation same hai.


# Wrong Indentation Example

# if True:
# print("Hello")

# Output
#
# IndentationError

# Kyun?
#
# Kyun ke if ke baad indentation dena compulsory hai.


# Another Wrong Example

# if True:
#     print("Hello")
#   print("Python")

# Output
#
# IndentationError

# Kyun?
#
# Dono lines ki indentation same honi chahiye.


# How Many Spaces?

# Python ka official recommendation hai

# 4 Spaces

# Example

if True:
    print("Correct Indentation")

# Ye best practice hai.


# Tabs vs Spaces

# Python Tabs bhi support karta hai.

# Lekin

# Tabs aur Spaces ko mix nahi karna chahiye.

# Wrong

# if True:
#     print("Hello")   <- Spaces
#     print("World")   <- Tab

# Isse Error aa sakta hai.

# Isliye hamesha sirf 4 spaces use karo.

# VS Code automatically 4 spaces use karta hai.


# Indentation Kis Kis Jagah Use Hoti Hai?

# if

if True:
    print("Inside if")

# else

if False:
    print("Hello")
else:
    print("World")

# for loop

for i in range(3):
    print(i)

# while loop

count = 1

while count <= 3:
    print(count)
    count += 1

# function

def greet():
    print("Assalam O Alaikum")

greet()

# class

class Student:

    def info(self):
        print("Student Class")

student = Student()
student.info()


# Why Python Uses Indentation?

# C, C++, Java, JavaScript mein

# Curly Braces {}

# use hoti hain.

# Example (JavaScript)

# if (true) {
#     console.log("Hello");
# }

# Python mein

# Curly Braces nahi hotin.

# Python indentation se hi samajhta hai
# ke block kahan start hua aur kahan end hua.

# Example

if True:
    print("Hello")

print("End")

# print("Hello")
# if block ke andar hai.

# print("End")
# if block ke bahar hai.


# Advantages of Indentation

# 1. Code readable hota hai.
# 2. Sab developers ek jaisa code likhte hain.
# 3. Block easily samajh aata hai.
# 4. Curly braces ki zarurat nahi padti.
# 5. Code clean lagta hai.


# Summary

# Indentation = Line ke shuru mein spaces dena.

# Python mein indentation compulsory hai.

# Recommended indentation = 4 Spaces.

# Tab aur Spaces ko mix nahi karna chahiye.

# Same indentation = Same Block.

# Indentation galat hogi to

# IndentationError

# aayega.

# if, else, for, while, function aur class
# sab indentation use karte hain.