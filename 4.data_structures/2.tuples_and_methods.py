# Tuples in Python

# Tuple kya hota hai?
#
# Tuple ek collection hai jisme hum multiple items store kar sakte hain.
# Tuple ORDERED hota hai (har item ka apna index hota hai).
# Tuple IMMUTABLE hota hai (create hone ke baad change nahi kar sakte).


# Creating a Tuple

tuple1 = (3, 5, 20, 23)

print(type(tuple1))    # <class 'tuple'>
print(tuple1)          # (3, 5, 20, 23)


# Tuple without Parentheses (Packing)

# Parentheses optional hain! Bina parentheses ke bhi tuple ban sakta hai.

tuple2 = 10, 20, 30

print(type(tuple2))    # <class 'tuple'>
print(tuple2)          # (10, 20, 30)


# Single Element Tuple (Important!)

# Agar tuple mein sirf EK item ho to comma dena ZAROORI hai.

single = (5,)          # ✅ Comma ke saath — Tuple hai
not_tuple = (5)        # ❌ Comma nahi — Ye Integer hai, Tuple nahi!

print(type(single))    # <class 'tuple'>
print(type(not_tuple)) # <class 'int'>


# Different Data Types in Tuple

# Tuple mein different data types bhi store kar sakte hain.

mixed_tuple = (3, 5.5, "Ibrahim", True, None)

print(mixed_tuple)     # (3, 5.5, 'Ibrahim', True, None)


# ------------------------ Tuple Indexing ------------------------

# Bilkul String aur List ki tarah!
# Tuple ke har item ka apna index hota hai.

#         0   1   2   3   4   ← Positive Index
#       (10, 20, 30, 40, 50)
#        -5  -4  -3  -2  -1  ← Negative Index

numbers = (10, 20, 30, 40, 50)

print(numbers[0])      # 10
print(numbers[1])      # 20
print(numbers[3])      # 40
print(numbers[-1])     # 50
print(numbers[-2])     # 40
print(numbers[-3])     # 30


# ------------------------ Tuple Slicing ------------------------

# Bilkul String aur List ki tarah!
# Same syntax, same rules!

# Syntax:
# tuple[start : end]
# tuple[start : end : step]

# Rules (Bilkul string/list jaisi):
# ✅ Start index include hota hai
# ❌ End index include nahi hota


numbers = (10, 20, 30, 40, 50, 60, 70)

print("Original Tuple:", numbers)

print(numbers[0:3])    # (10, 20, 30)
print(numbers[1:4])    # (20, 30, 40)
print(numbers[3:])     # (40, 50, 60, 70)    (End nahi diya → last tak)
print(numbers[:4])     # (10, 20, 30, 40)    (Start nahi diya → 0 se)
print(numbers[:])      # (10, 20, 30, 40, 50, 60, 70)  (Poori copy)


# Negative Slicing

print(numbers[-4:-1])  # (40, 50, 60)
print(numbers[-3:])    # (50, 60, 70)


# Step Slicing

print(numbers[::2])    # (10, 30, 50, 70)     (Har doosra item)
print(numbers[::3])    # (10, 40, 70)         (Har teesra item)


# Reverse Tuple

print(numbers[::-1])   # (70, 60, 50, 40, 30, 20, 10)  (Reverse!)


# ⚠️ Important:
# Tuple slicing NEW TUPLE return karta hai.
# Original tuple change nahi hota.


# ------------------------ Tuple is Immutable ------------------------

# Immutable ka matlab:
# Create hone ke baad tuple ko CHANGE nahi kar sakte.

# Iska matlab:
# ❌ Item ki value change nahi kar sakte
# ❌ Naya item add nahi kar sakte
# ❌ Item delete nahi kar sakte


# Example 1: Item Assignment (Error)

tuple1 = (3, 5, 20, 23)

# tuple1[0] = 1
# Output:
# TypeError: 'tuple' object does not support item assignment

# Iska matlab:
# Tuple mein kisi specific index ki value CHANGE nahi kar sakte!


# Example 2: Delete Item (Error)

# del tuple1[0]
# Output:
# TypeError: 'tuple' object doesn't support item deletion


# Example 3: Add Item (Error) — Tuple ke paas append() nahi hota!

# tuple1.append(100)
# Output:
# AttributeError: 'tuple' object has no attribute 'append'


# ------------------------ Immutable vs Mutable ------------------------

# String → Immutable ❌ (Change nahi kar sakte)
# List   → Mutable   ✅ (Change kar sakte)
# Tuple  → Immutable ❌ (Change nahi kar sakte)


# Example: List vs Tuple

# List (Mutable)
my_list = [1, 2, 3]
my_list[0] = 100        # ✅ Change ho gaya!
print(my_list)          # [100, 2, 3]

# Tuple (Immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 100     # ❌ TypeError aayega!
print(my_tuple)         # (1, 2, 3) — Waisi hi rahegi


# ------------------------ Tuple Methods ------------------------

# Tuple ke sirf DO methods hote hain!
# Kyun?
# Kyunke tuple immutable hai, isliye zyada tar list methods kaam nahi karte.


# 1. count() — Item kitni baar aaya hai

numbers = (1, 2, 2, 3, 2, 4, 2, 5)

print(numbers.count(2))    # 4 (2 kitni baar aaya?)
print(numbers.count(5))    # 1
print(numbers.count(10))   # 0 (10 tuple mein nahi hai)

# count() VALUE RETURN karta hai (integer).
# Original tuple MODIFY nahi karta.


# 2. index() — Item ka index batata hai

fruits = ("Apple", "Banana", "Mango", "Banana")

print(fruits.index("Banana"))   # 1 (Pehla Banana index 1 par hai)
print(fruits.index("Mango"))    # 2

# Agar item tuple mein nahi hai to ERROR aayega:

# print(fruits.index("Orange"))
# Output:
# ValueError: tuple.index(x): x not in tuple


# ------------------------ len() Function ------------------------

# len() tuple ki length batata hai.

items = (10, 20, 30, 40, 50)
print(len(items))       # 5


# ------------------------ Membership Operator ------------------------

# Check karna ke item tuple mein hai ya nahi.

colors = ("Red", "Green", "Blue")

print("Red" in colors)       # True
print("Yellow" in colors)    # False
print("Yellow" not in colors) # True


# ------------------------ Tuple Concatenation ------------------------

# Do tuples ko jod kar naya tuple bana sakte hain.

tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)

combined = tuple_a + tuple_b
print(combined)         # (1, 2, 3, 4, 5, 6)


# ------------------------ Tuple Repetition ------------------------

# Tuple ko repeat kar sakte hain.

repeat_tuple = ("Hello",) * 3
print(repeat_tuple)     # ('Hello', 'Hello', 'Hello')


# ------------------------ Tuple Unpacking ------------------------

# Tuple ke items ko alag-alag variables mein assign kar sakte hain.

student = ("Ibrahim", 22, "BSCS")

name, age, course = student

print(name)      # Ibrahim
print(age)       # 22
print(course)    # BSCS

# Isi ko TUPLE UNPACKING kehte hain!


# ------------------------ When to Use Tuple vs List? ------------------------

# Tuple use karo jab:
# ✅ Data change nahi hoga (e.g., days of week, months)
# ✅ Data ko protect karna hai accidental changes se
# ✅ Performance chahiye (Tuple list se thoda fast hota hai)
# ✅ Dictionary keys chahiye (Tuple hashable hai, List nahi)


# List use karo jab:
# ✅ Data frequently change hoga
# ✅ Items add/remove karni hai
# ✅ append(), remove(), sort() jaise methods chahiye


# Example:

# Tuple — Days of week (Kabhi change nahi honge)
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# List — Shopping cart (Items add/remove hote rahenge)
shopping_cart = ["Milk", "Bread"]
shopping_cart.append("Eggs")
shopping_cart.remove("Bread")


# ------------------------ Key Differences Table ------------------------

# | Property         | String     | List        | Tuple       |
# |------------------|------------|-------------|-------------|
# | Mutable?         | ❌ Immutable| ✅ Mutable  | ❌ Immutable|
# | Indexing?        | ✅ Yes     | ✅ Yes      | ✅ Yes      |
# | Slicing?         | ✅ Yes     | ✅ Yes      | ✅ Yes      |
# | Methods Count    | Many       | Many        | Only 2      |
# | Item Assignment  | ❌ No      | ✅ Yes      | ❌ No       |
# | append()         | ❌ No      | ✅ Yes      | ❌ No       |


# ------------------------ Summary ------------------------

# Tuple = Ordered, Immutable collection.

# Tuple Indexing = String/List jaisi hi hai.

# Tuple Slicing = String/List jaisi hi hai.
#   → Same syntax: tuple[start:end:step]
#   → Same rules: Start include, End include nahi
#   → New tuple return karta hai
#   → Original tuple change nahi hota

# Tuple IMMUTABLE hai:
#   → Create hone ke baad change nahi kar sakte
#   → Item assignment nahi kar sakte → TypeError
#   → append(), remove(), insert() nahi hote

# Tuple Methods sirf DO:
#   → count() — Item ka count batata hai
#   → index() — Item ka index batata hai

# Tuple Unpacking — Items ko variables mein assign karna.

# Tuple vs List:
#   → Tuple = Immutable (Fixed data)
#   → List = Mutable (Changing data)