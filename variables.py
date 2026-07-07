# Python code top to bottom execute karta hai.

# Variable Naming Convention

# Variable Naming Convention ka matlab:
# Variables ko aise naam dena jo readable, meaningful aur professional hon.

# Python mein recommended style = snake_case


# ✅ Good Variable Names (Recommended)

first_name = "Ibrahim"         # Snake Case ✅
last_name = "Shaikh"
phone_number = "03123456789"
student_age = 22
is_logged_in = True
total_marks = 500

print(first_name)
print(last_name)
print(phone_number)
print(student_age)
print(is_logged_in)
print(total_marks)


# ❌ Bad Variable Names

a = "Ibrahim"                  # Samajh nahi aa raha kis liye use ho raha hai
b = 22
c = True

# Beginners ke liye theek hai, lekin real projects mein meaningful names use karo.


# Variable Rules

name = "Ibrahim"               # ✅ Letter se start
_name = "Ali"                  # ✅ Underscore se start

name1 = "Ahmed"                # ✅ Number end mein ho sakta hai
student2026 = "BSCS"           # ✅ Number beech ya end mein allowed hai

# 1name = "Ali"                # ❌ Number se start nahi kar sakte

# first name = "Ali"           # ❌ Space allowed nahi

# first-name = "Ali"           # ❌ Hyphen (-) allowed nahi

# class = "BSCS"               # ❌ Python Keyword use nahi kar sakte

# if = True                    # ❌ Keyword


# Different Naming Styles

# Snake Case (Python mein Recommended)
first_name = "Ibrahim"

# Camel Case (JavaScript mein common)
firstName = "Ibrahim"

# Pascal Case (Classes ke liye)
StudentData = "Example"

# Upper Case (Constants ke liye)
PI = 3.14159
MAX_USERS = 100


# Best Practice

# ❌ Avoid
x = 50000

# ✅ Better
employee_salary = 50000

print(employee_salary)


# Summary

# Variables  -> snake_case ✅
# Functions  -> snake_case ✅
# Classes    -> PascalCase ✅
# Constants  -> UPPER_CASE ✅


# ------------------------ Data Types ------------------------  

# Basic Data Types
a = 3                  # Integer (Poora Number) | Immutable
print(a)

b = 6.2                # Float (Decimal Number) | Immutable
print(b)

c = True               # Boolean (True / False) | Immutable
print(c)

d = "Ibrahim"          # String (Double Quotes) | Immutable
print(d)

e = 'Pakistan'         # String (Single Quotes) | Immutable
print(e)

f = None               # NoneType (No Value) | Immutable
print(f)


# Collection Data Types
g = [10, 20, 30]       # List
                       # Ordered ✅
                       # Mutable ✅ (Items Add / Update / Delete kar sakte hain)
print(g)

h = (10, 20, 30)       # Tuple
                       # Ordered ✅
                       # Immutable ❌ (Create hone ke baad change nahi hoti)
print(h)

i = {10, 20, 30}       # Set
                       # Unordered ✅
                       # Mutable ✅
                       # Duplicate values allow nahi karta
print(i)

j = {
    "name": "Ibrahim",
    "age": 22,
    "city": "Karachi"
}                      # Dictionary
                       # Key : Value Pair
                       # Mutable ✅
                       # Ordered ✅ (Python 3.7+)
print(j)


# Binary Data Types
k = b"Hello"           # Bytes
                       # Immutable ❌
                       # Binary Data Store karta hai
print(k)

l = bytearray(b"Hello") # Bytearray
                        # Mutable ✅
                        # Binary Data ko Modify kar sakte hain
print(l)

m = memoryview(bytes(5)) # MemoryView
                         # Memory ko bina copy kiye access karta hai
                         # Mutable ya Immutable underlying object par depend karta hai
print(m)


# Complex Number
n = 4 + 5j             # Complex Number
                        # Real + Imaginary Part
                        # Immutable ❌
print(n)


# Range
o = range(5)           # Range
                        # Number Sequence Generate karta hai
                        # Immutable ❌
print(o)



# Type Casting
p = "5"                # String (Text)
print(p)

q = 5                  # Integer (Number)
print(q)

# Type Casting ka matlab hota hai:
# Ek Data Type ko doosre Data Type mein convert karna.

# String ➜ Integer
r = int(p)
print(r)

# Integer ➜ String
s = str(q)
print(s)

# Integer ➜ Float
t = float(q)
print(t)

# Float ➜ Integer (Decimal remove ho jata hai)
u = int(6.9)
print(u)

# Integer ➜ Boolean
v = bool(q)
print(v)

# Boolean ➜ Integer
w = int(True)
print(w)

x = int(False)
print(x)

# Float ➜ String
y = str(3.14)
print(y)

# String ➜ Float
z = float("10.5")
print(z)