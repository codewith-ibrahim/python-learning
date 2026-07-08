# Lists in Python

# List kya hoti hai?
#
# List ek collection hai jisme hum multiple items store kar sakte hain.
# List ORDERED hoti hai (har item ka apna index hota hai).
# List MUTABLE hoti hai (items ko add, update, delete kar sakte hain).


# Creating a List

list1 = [3, 5, 7, 10, 15]

print(type(list1))   # <class 'list'>
print(list1)         # [3, 5, 7, 10, 15]


# Different Data Types in List

# List mein different data types bhi store kar sakte hain.

mixed_list = [3, 5, 7, 10, 15, "Ibrahim"]

print(mixed_list)    # [3, 5, 7, 10, 15, 'Ibrahim']

# Yahan Integer aur String dono ek hi list mein hain.
# Python allow karta hai!


# ------------------------ List Slicing ------------------------

# Jaise hum string ko slice karte hain, BILKUL WAISE HI list ko bhi slice kar sakte hain.
# Same syntax, same rules!

# Syntax:
# list[start : end]
# list[start : end : step]

# Rules (Bilkul string jaisi):
# ✅ Start index include hota hai
# ❌ End index include nahi hota


# Example 1: Basic Slicing

numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original List:", numbers)     # [10, 20, 30, 40, 50, 60, 70]

print(numbers[0:3])    # [10, 20, 30]       (Index 0 se 2 tak)
print(numbers[1:4])    # [20, 30, 40]       (Index 1 se 3 tak)
print(numbers[2:5])    # [30, 40, 50]       (Index 2 se 4 tak)


# Example 2: Start ya End Chhodna

print(numbers[3:])     # [40, 50, 60, 70]   (Index 3 se end tak)
print(numbers[:4])     # [10, 20, 30, 40]   (Start se index 3 tak)
print(numbers[:])      # [10, 20, 30, 40, 50, 60, 70]  (Poori list ki copy)


# Example 3: Negative Index Slicing

#        0    1    2    3    4    5    6   ← Positive Index
#      [10,  20,  30,  40,  50,  60,  70]
#       -7   -6   -5   -4   -3   -2   -1   ← Negative Index

print(numbers[-4:-1])  # [40, 50, 60]       (-4 = 40, -1 = 70 include nahi)
print(numbers[-3:])    # [50, 60, 70]       (-3 se end tak)
print(numbers[:-2])    # [10, 20, 30, 40, 50]  (Start se -2 se pehle tak)


# Example 4: Step Slicing

print(numbers[::1])    # [10, 20, 30, 40, 50, 60, 70]   (Har item)
print(numbers[::2])    # [10, 30, 50, 70]               (Har doosra item)
print(numbers[::3])    # [10, 40, 70]                   (Har teesra item)


# Example 5: Reverse List

print(numbers[::-1])   # [70, 60, 50, 40, 30, 20, 10]   (Reverse!)


# ------------------------ Important Difference ------------------------
# String Slicing vs List Slicing

# String Slicing:
# NEW STRING return karta hai
# Original string change nahi hoti

name = "Ibrahim"
sliced = name[1:3]      # 'br' — Nayi string return hui

print(sliced)           # br
print(name)             # Ibrahim — Original string waisi hi hai!


# List Slicing:
# NEW LIST return karta hai
# Original list change nahi hoti

numbers = [10, 20, 30, 40, 50]
sliced_list = numbers[1:4]     # [20, 30, 40] — Nayi list return hui

print(sliced_list)      # [20, 30, 40]
print(numbers)          # [10, 20, 30, 40, 50] — Original list waisi hi hai!


# List Slicing vs List Methods (Farq Samjhein!)

# Slicing → New list return karta hai, Original change nahi hoti
# remove() → Kuch return nahi karta, Original modify hoti hai


# ------------------------ Important Difference ------------------------
# String Slicing vs List Methods

# String Slicing:
# Jab hum string ko slice karte hain to ek NEW STRING return hoti hai.
# Original string change nahi hoti (kyunke strings immutable hain).

name = "Ibrahim"
sliced = name[1:3]      # 'br' — Nayi string return hui

print(sliced)           # br
print(name)             # Ibrahim — Original string waisi hi hai!

# List Methods:
# Lekin list methods ORIGINAL LIST ko hi modify kar dete hain.
# Ye koi nayi list return nahi karte (zyada tar methods).


# ------------------------ Example: remove() Method ------------------------

list1 = [3, 5, 7, 10, 15]
print("Original List:", list1)      # [3, 5, 7, 10, 15]

# remove() method original list se item delete karta hai.

list1.remove(15)                     # 15 ko delete karo

print("After remove:", list1)        # [3, 5, 7, 10]

# ⚠️ Important:
# remove() method KOI VALUE RETURN NAHI KARTA.
# Ye None return karta hai!


# ------------------------ Common Confusion ------------------------

# Agar hum likhein:

# print(list1.remove(15))

# To kya hoga?

# Pehle remove(15) chalega → 15 delete ho jayega.
# Phir print karega remove() ka return value.
# remove() ka return value → None

# Isliye output mein None aayega, list nahi!

# Example:

list2 = [1, 2, 3, 4, 5]
print("Before:", list2)              # [1, 2, 3, 4, 5]

result = list2.remove(3)             # 3 delete karo
print("Return Value:", result)       # None
print("After:", list2)               # [1, 2, 4, 5]

# Sahi tareeqa:

list3 = [10, 20, 30, 40]
list3.remove(30)                     # Pehle remove karo
print(list3)                         # Phir print karo → [10, 20, 40]


# ------------------------ count() Method ------------------------

# count() method batata hai ke list mein koi item kitni baar aaya hai.

list4 = [1, 2, 2, 3, 2, 4, 2, 5]

print(list4.count(2))   # 4 (2 kitni baar aaya?)
print(list4.count(5))   # 1
print(list4.count(10))  # 0 (10 list mein nahi hai)

# ⚠️ Important:
# count() VALUE RETURN karta hai (integer).
# count() original list ko MODIFY nahi karta.

list5 = [10, 20, 30, 20, 20]
count_20 = list5.count(20)

print("Count of 20:", count_20)      # 3
print("Original List:", list5)       # [10, 20, 30, 20, 20] — No change!


# Aapke code ki galti:

# list1.count(0)
# print(list1)

# Yahan count(0) ne return value 0 di, lekin aapne use store nahi kiya.
# Isliye list1 print karne par original list hi dikhi.

# Sahi tareeqa:

list6 = [3, 5, 7, 10, 15]
count_result = list6.count(0)        # 0 return karega (0 list mein nahi hai)
print("Count Result:", count_result) # 0
print("List:", list6)                # [3, 5, 7, 10, 15] — No change


# ------------------------ Key Differences Table ------------------------

# | Operation         | Returns New? | Modifies Original? | Example                        |
# |-------------------|--------------|--------------------|--------------------------------|
# | String Slicing    | ✅ New String| ❌ No              | name[1:3] → New string         |
# | List Slicing      | ✅ New List  | ❌ No              | numbers[1:4] → New list        |
# | list.remove()     | ❌ None      | ✅ Yes             | Original list se item delete   |
# | list.count()      | ✅ Integer   | ❌ No              | Batata hai kitni baar aaya     |
# | list.append()     | ❌ None      | ✅ Yes             | Original mein item add         |
# | list.pop()        | ✅ Item      | ✅ Yes             | Item return + Original modify  |


# ------------------------ More List Methods ------------------------

# append() — List ke end mein item add karta hai

fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)           # ['Apple', 'Banana', 'Mango']


# insert() — Specific index par item add karta hai

fruits.insert(1, "Orange")
print(fruits)           # ['Apple', 'Orange', 'Banana', 'Mango']


# pop() — Last item delete karta hai aur return karta hai

last_item = fruits.pop()
print("Deleted:", last_item)   # Mango
print("List:", fruits)          # ['Apple', 'Orange', 'Banana']


# pop(index) — Specific index ka item delete + return

item = fruits.pop(0)
print("Deleted:", item)         # Apple
print("List:", fruits)          # ['Orange', 'Banana']


# sort() — List ko sort karta hai (Original modify)

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)          # [1, 2, 3, 5, 8]


# reverse() — List ko reverse karta hai (Original modify)

numbers.reverse()
print(numbers)          # [8, 5, 3, 2, 1]


# index() — Item ka index batata hai

nums = [10, 20, 30, 40, 50]
print(nums.index(30))   # 2


# copy() — List ki copy banata hai (New list return)

original = [1, 2, 3]
duplicate = original.copy()
print(duplicate)        # [1, 2, 3]


# clear() — Poori list khali kar deta hai

temp = [1, 2, 3]
temp.clear()
print(temp)             # []


# ------------------------ Summary ------------------------

# List = Ordered, Mutable collection.

# List Slicing = String Slicing jaisa hi hai!
#   → Same syntax: list[start:end:step]
#   → Same rules: Start include, End include nahi
#   → New list return karta hai
#   → Original list change nahi hoti

# String slicing → NEW string return karta hai.
# List slicing → NEW list return karta hai.
# List methods → Mostly ORIGINAL list modify karte hain.

# remove() → Item delete karta hai, None return karta hai.
# count() → Item ka count batata hai, Integer return karta hai.
# append() → End mein item add, None return.
# pop() → Item delete + Return karta hai.
# sort() / reverse() → Original modify karte hain.

# ⚠️ Golden Rule:
# Jiska return value None hota hai, use DIRECT print nahi karna chahiye.
# Pehle method chalao, phir list print karo.