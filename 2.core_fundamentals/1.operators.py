# Operators in Python

# Operators wo symbols hote hain jo values ya variables par operation perform karte hain.

num1 = 10
num2 = 5

print(num1)
print(num2)


# Arithmetic Operators

# Arithmetic Operators ka use Mathematical Calculations ke liye hota hai.

# Addition (+)
# Dono numbers ko add karta hai.
print( "Addition", num1 + num2)      # Output: 15

# Subtraction (-)
# Pehle number mein se doosra number minus karta hai.
print( "Subtraction", num1 - num2)      # Output: 5

# Multiplication (*)
# Dono numbers ko multiply karta hai.
print( "Multiplication", num1 * num2)      # Output: 50

# Division (/)
# Division karta hai aur hamesha Float return karta hai.
print( "Division", num1 / num2)      # Output: 2.0

# Floor Division (//)
# Sirf poora (integer) result deta hai, decimal hata deta hai.
print( "Float Division", num1 // num2)     # Output: 2

# Modulus (%)
# Division ka remainder (baqi) return karta hai.
print("Remainder", num1 % num2)      # Output: 0

# Exponent (**)
# Power calculate karta hai.
print("Power Calculate", num1 ** num2)     # Output: 100000 (10^5)


# Assignment Operators

# Assignment Operator (=)
# Kisi variable ko value assign karne ke liye use hota hai.

a = 4
print(a)               # Output: 4


# Addition Assignment (+=)
# a = a + 2
# Pehle wali value mein 2 add karega.

a += 2
print(a)               # Output: 6


# Subtraction Assignment (-=)
# a = a - 2
# Current value mein se 2 minus karega.

a -= 2
print(a)               # Output: 4


# Multiplication Assignment (*=)
# a = a * 3

a *= 3
print(a)               # Output: 12


# Division Assignment (/=)
# a = a / 2

a /= 2
print(a)               # Output: 6.0


# Floor Division Assignment (//=)
# a = a // 2

a //= 2
print(a)               # Output: 3.0


# Modulus Assignment (%=)
# a = a % 2

a %= 2
print(a)               # Output: 1.0


# Exponent Assignment (**=)
# a = a ** 3

a **= 3
print(a)               # Output: 1.0


# Comparison Operators

# Comparison Operators ka use
# Do values ya variables ko compare karne ke liye hota hai.
# Inka output hamesha True ya False hota hai.

x = 8
y = 9

print(x)
print(y)


# Less Than (<)
# Check karta hai kya x y se chhota hai?

print(x < y)           # Output: True


# Greater Than (>)
# Check karta hai kya x y se bada hai?

print(x > y)           # Output: False


# Equal To (==)
# Check karta hai kya dono values equal hain?

print(x == y)          # Output: False


# Not Equal To (!=)
# Check karta hai kya dono values different hain?

print(x != y)          # Output: True


# Greater Than or Equal To (>=)
# Check karta hai kya x bada ya barabar hai y ke?

print(x >= y)          # Output: False


# Less Than or Equal To (<=)
# Check karta hai kya x chhota ya barabar hai y ke?

print(x <= y)          # Output: True


# Logical Operators

# Logical Operators ka use
# Multiple conditions ko combine karne ke liye hota hai.
# Inka output hamesha True ya False hota hai.

x = 8
y = 9

print(x)
print(y)


# AND Operator (and)
# Agar dono conditions True hongi tabhi result True hoga.

print(x == y and x < y)      # Output: False


# OR Operator (or)
# Agar ek bhi condition True ho to result True hoga.

print(x == y or x < y)       # Output: True


# NOT Operator (not)
# Result ko ulta (reverse) kar deta hai.

print(not(x == y))           # Output: True
print(not(x < y))            # Output: False