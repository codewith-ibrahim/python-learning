# For Loop in Python

# For Loop kya hota hai?
#
# For Loop Python ka ek CONTROL FLOW STATEMENT hai
# jo kisi bhi ITERABLE (collection) ke har element par
# ek-ek karke ITERATE karta hai aur har element ke liye
# code ka ek block execute karta hai.
#
# Simple Words Mein:
# "Jitne items hain, utni baar loop chalega"
# "Har item ko ek baar access karega"
# "Ek-ek karke sabko process karega"

# Technical Definition:
# For Loop ek ITERATION STATEMENT hai jo kisi bhi
# ITERABLE object (list, tuple, string, dictionary,
# set, range, etc.) ke elements ko SEQUENTIALLY
# access karta hai aur har element ke liye defined
# code block ko execute karta hai.

# Real Life Analogy:
# Socho aapke paas 5 apples ki tokri hai.
# Aapko har apple ko check karna hai ke wo fresh hai ya nahi.
#
# For Loop yahi karega:
# 🍎 Pehla apple uthao → Check karo → Rakh do → Agla
# 🍎 Doosra apple uthao → Check karo → Rakh do → Agla
# 🍎 Teesra apple uthao → Check karo → Rakh do → Agla
# ...
# Jab tak apples khatam na ho jayein!


# ------------------------ What is ITERABLE? ------------------------

# Iterable = Koi bhi object jis par loop chalaya ja sakta hai
#
# Python mein ye sab ITERABLE hain:
# ✅ List        : [1, 2, 3]
# ✅ Tuple       : (1, 2, 3)
# ✅ String      : "Hello"
# ✅ Set         : {1, 2, 3}
# ✅ Dictionary  : {"a": 1, "b": 2}
# ✅ range()     : range(5)
# ✅ File objects
# ✅ Aur bhi bahut kuch!


# ------------------------ What is ITERATION? ------------------------

# Iteration = Baar baar ek hi kaam karna (Loop ka ek chakkar)
#
# Har chakkar ko "ITERATION" kehte hain.
#
# Example:
# for i in range(3):
#     print(i)
#
# Is loop mein 3 ITERATIONS hain:
# Iteration 1: i = 0
# Iteration 2: i = 1
# Iteration 3: i = 3


# ------------------------ What is ITERATOR VARIABLE? ------------------------

# Iterator Variable = Wo variable jo har iteration mein
#                    collection ka next element hold karta hai
#
# Common names: i, j, k (programmers ki aadat se)
# Better names: item, element, value, number, student, etc.
#
# Ye variable AUTOMATICALLY update hota hai — aapko manually
# badhane ki zaroorat nahi!


# ------------------------ Basic Syntax ------------------------

# Syntax:
# for <variable> in <iterable>:
#     # Code block (Indentation zaroori!)

# Parts of For Loop:
# 🔹 for        → Python keyword (Loop start)
# 🔹 variable   → Iterator variable (Aapka naam)
# 🔹 in         → Python keyword (Iterable ke andar se)
# 🔹 iterable   → Koi bhi collection (list, range, etc.)
# 🔹 :          → Colon (Block start)
# 🔹 Indentation → Loop body define karta hai


# ------------------------ How For Loop Works (Internal) ------------------------

# Internally For Loop kya karta hai?
#
# 1. Python iterable ka ITERATOR object banata hai
# 2. next() function call karta hai
# 3. Value ko variable mein assign karta hai
# 4. Loop body execute karta hai
# 5. Phir se next() call karta hai
# 6. Jab StopIteration exception aati hai → Loop END


# ------------------------ range() — Deep Explanation ------------------------

# range() Python ka BUILT-IN FUNCTION hai
# Jo numbers ki SEQUENCE generate karta hai
#
# Ye memory-efficient hai — poori list memory mein nahi banata!
# Zaroorat par next number generate karta hai.

# range() ke 3 Forms:

# 📌 Form 1: range(stop)
#    0 se lekar stop-1 tak numbers
#    range(5)    → 0, 1, 2, 3, 4
#    range(3)    → 0, 1, 2

# 📌 Form 2: range(start, stop)
#    start se lekar stop-1 tak numbers
#    range(2, 6) → 2, 3, 4, 5
#    range(5, 8) → 5, 6, 7

# 📌 Form 3: range(start, stop, step)
#    start se lekar stop-1 tak, step ke gap se
#    range(1, 10, 2)  → 1, 3, 5, 7, 9
#    range(10, 0, -1) → 10, 9, 8, ..., 1

# ⚠️ GOLDEN RULE (Bilkul Slicing Jaisa):
# START → Include hota hai ✅
# STOP  → Include NAHI hota ❌


# ------------------------ i (Iterator Variable) — Full Explanation ------------------------

# i kya hai?
#
# i sirf ek VARIABLE NAME hai. Kuch khaas nahi.
# i ka matlab: "iterator" ya "index" (programmers ki convention)
#
# Aap kuch bhi naam de sakte ho:
# i, j, k          → Convention (Math/Programming)
# index, count     → Jab numbers se kaam ho
# item, element    → Jab list/tuple ke items se kaam ho
# student, fruit   → Descriptive (Meaningful)


# ------------------------ Aapka Original Code — Step by Step ------------------------

print("=" * 50)
print("📊 YOUR ORIGINAL CODE — STEP BY STEP BREAKDOWN")
print("=" * 50)

# Aapka Code:
# for i in range(10):
#     print(i+1)

print("\n🔍 Code Analysis:")
print("-" * 40)
print("Code: for i in range(10):")
print("           print(i+1)")
print()

print("Execution Steps:")
print("-" * 40)

for i in range(10):
    print(f"   Step {i+1:2}: range(10) gives i = {i} → print({i}+1) = {i+1}")

print("\n" + "-" * 40)
print("Total Iterations: 10")

# Kya hua?
# range(10) → 10 numbers generate kiye: 0 se 9 tak
# Har number ke liye:
#   1. i mein value assign hui
#   2. print(i+1) execute hua
#   3. Agla number

# Output: 1, 2, 3, ..., 10 (kyunke i+1 print kiya)


# ------------------------ Better Way ------------------------

print("\n\n📊 BETTER WAY (Direct 1 to 10)")
print("=" * 40)

for num in range(1, 11):
    print(f"   {num}", end=" ")
print()

# range(1, 11) → 1, 2, 3, ..., 10
# Ab num directly 1 se 10 tak hai
# i+1 karne ki zaroorat nahi!


# ------------------------ List with For Loop — Deep Dive ------------------------

print("\n\n" + "=" * 50)
print("📊 FOR LOOP WITH LIST — DEEP DIVE")
print("=" * 50)

list1 = [2, 4, 6, 8, 10]

print(f"\nList: {list1}")
print(f"List Length: {len(list1)} items")
print(f"List Type: {type(list1)}")

print("\n🔍 Loop Analysis:")
print("-" * 40)

# Loop
iteration = 1
for item in list1:
    print(f"   Iteration {iteration}: item = {item}")
    iteration += 1

print(f"\n   Total Iterations: {len(list1)}")
print(f"   (List mein jitne items, utni baar loop chala)")

# Kya hua?
# list1 = [2, 4, 6, 8, 10]  → 5 items
# Loop 5 baar chala
# Har iteration mein item = next element

# Visual Representation:
#
# list1:  [ 2,   4,   6,   8,   10 ]
#           ↓    ↓    ↓    ↓    ↓
# item:     2    4    6    8    10
#           ↓    ↓    ↓    ↓    ↓
# print:    2    4    6    8    10


# ------------------------ For Loop Working — Internal Mechanism ------------------------

print("\n\n" + "=" * 50)
print("📊 HOW FOR LOOP WORKS (INTERNAL)")
print("=" * 50)

# Python internally for loop ko aise execute karta hai:

print("\n🔍 Internal Working:")
print("-" * 40)

print("""
Behind the Scenes:
1. iter(list1) → Iterator object create hota hai
2. next(iterator) → Pehla element milta hai (2)
3. item = 2 → Variable mein assign
4. Loop body execute → print(2)
5. next(iterator) → Agla element (4)
6. item = 4 → Variable mein assign
7. Loop body execute → print(4)
... 
8. Jab StopIteration exception → Loop END
""")

# Manual demonstration:
print("Manual Iterator Demo:")
numbers = [10, 20, 30]
iterator_obj = iter(numbers)  # Iterator object

print(f"   next() → {next(iterator_obj)}")  # 10
print(f"   next() → {next(iterator_obj)}")  # 20
print(f"   next() → {next(iterator_obj)}")  # 30
# print(f"   next() → {next(iterator_obj)}")  # StopIteration Error!


# ------------------------ For Loop with ALL Data Types ------------------------

print("\n\n" + "=" * 50)
print("📊 FOR LOOP WITH ALL COLLECTIONS")
print("=" * 50)

# 1. List
print("\n1️⃣  LIST:")
my_list = ["Python", "Java", "C++"]
for lang in my_list:
    print(f"   Language: {lang}")

# 2. Tuple
print("\n2️⃣  TUPLE:")
my_tuple = (10, 20, 30)
for num in my_tuple:
    print(f"   Number: {num}")

# 3. String (Character by character)
print("\n3️⃣  STRING:")
my_string = "Hello"
for char in my_string:
    print(f"   Character: {char}")

# 4. Set (Unordered — Order guaranteed nahi!)
print("\n4️⃣  SET:")
my_set = {"Apple", "Banana", "Mango"}
for fruit in my_set:
    print(f"   Fruit: {fruit}")

# 5. Dictionary
print("\n5️⃣  DICTIONARY:")
student = {"name": "Ibrahim", "age": 22, "grade": "A"}

# Keys only
print("   Keys:")
for key in student:
    print(f"      {key}")

# Values only
print("   Values:")
for value in student.values():
    print(f"      {value}")

# Both Keys and Values
print("   Key-Value Pairs:")
for key, value in student.items():
    print(f"      {key} = {value}")


# ------------------------ Real Life Practical Examples ------------------------

print("\n\n" + "=" * 50)
print("📊 PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Sum of all numbers
print("\n1️⃣  Sum Calculator:")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num  # total = total + num
print(f"   List: {numbers}")
print(f"   Sum: {total}")

# Example 2: Find Maximum
print("\n2️⃣  Find Maximum:")
marks = [65, 89, 45, 92, 78]
highest = marks[0]  # Assume pehla sabse bada
for mark in marks:
    if mark > highest:
        highest = mark
print(f"   Marks: {marks}")
print(f"   Highest: {highest}")

# Example 3: Filter Even Numbers
print("\n3️⃣  Even Number Filter:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"   All Numbers: {numbers}")
print(f"   Even Only: {evens}")

# Example 4: Count Occurrences
print("\n4️⃣  Word Counter:")
words = ["apple", "banana", "apple", "mango", "apple"]
count = 0
for word in words:
    if word == "apple":
        count += 1
print(f"   Words: {words}")
print(f"   'apple' appears: {count} times")

# Example 5: Multiplication Table
print("\n5️⃣  Table Generator:")
number = 5
print(f"   Table of {number}:")
for i in range(1, 11):
    print(f"      {number} x {i:2} = {number * i:2}")


# ------------------------ For Loop vs Other Loops ------------------------

print("\n\n" + "=" * 50)
print("📊 FOR LOOP vs WHILE LOOP")
print("=" * 50)

print("""
┌────────────────────┬──────────────────────┬─────────────────────┐
│ Feature            │ For Loop             │ While Loop          │
├────────────────────┼──────────────────────┼─────────────────────┤
│ Use When           │ Iterations known     │ Iterations unknown  │
│ Condition          │ Automatic (items)    │ Manual (condition)  │
│ Best For           │ Collections, range   │ User input, waiting │
│ Syntax             │ for x in y:          │ while condition:    │
│ Infinite Loop Risk │ Low                  │ High                │
│ Variable Update    │ Automatic            │ Manual              │
└────────────────────┴──────────────────────┴─────────────────────┘

For Loop Best Use Cases:
✅ List ke sab items process karna
✅ Fixed range mein kaam karna
✅ String ke characters count karna
✅ Dictionary iterate karna
✅ File line by line padhna

While Loop Best Use Cases:
✅ User input lena (jab tak quit na kare)
✅ Game loop (jab tak game over na ho)
✅ Waiting for condition
✅ Unknown number of iterations
""")


# ------------------------ Common Mistakes ------------------------

print("\n\n" + "=" * 50)
print("📊 COMMON MISTAKES")
print("=" * 50)

print("""
❌ Mistake 1: Colon (:) bhoolna
   for i in range(5)        # SyntaxError!
       print(i)

✅ Correct:
   for i in range(5):        # Colon lagao
       print(i)


❌ Mistake 2: Indentation galat
   for i in range(3):
   print(i)                  # IndentationError!

✅ Correct:
   for i in range(3):
       print(i)              # 4 spaces


❌ Mistake 3: range() mein stop include samajhna
   range(5) → 0,1,2,3,4     (5 include NAHI!)

✅ Yad rakho: stop include nahi hota


❌ Mistake 4: Loop ke andar list modify karna
   for item in my_list:
       my_list.remove(item)  # Unexpected behavior!

✅ Pehle copy banao, phir modify karo


❌ Mistake 5: Infinite loop banana (For loop mein mushkil hai)
   for i in range(1000000000000000):  # Bahut zyada iterations
       print(i)                        # Time waste!

✅ Sahi range use karo
""")


# ------------------------ Advanced: enumerate() ------------------------

print("\n\n" + "=" * 50)
print("📊 ADVANCED: enumerate()")
print("=" * 50)

# enumerate() — Index + Value ek saath!

fruits = ["Apple", "Banana", "Mango"]

print("\nWithout enumerate():")
index = 0
for fruit in fruits:
    print(f"   {index}: {fruit}")
    index += 1

print("\nWith enumerate() — Better:")
for index, fruit in enumerate(fruits):
    print(f"   {index}: {fruit}")

# enumerate(iterable, start=0)
print("\nWith enumerate(start=1):")
for sr, fruit in enumerate(fruits, start=1):
    print(f"   {sr}. {fruit}")


# ------------------------ Advanced: zip() ------------------------

print("\n📊 ADVANCED: zip()")
print("=" * 40)

# zip() — Multiple lists ek saath loop karna

names = ["Ibrahim", "Ali", "Sara"]
ages = [22, 21, 23]
cities = ["Karachi", "Lahore", "Islamabad"]

print("\nMultiple lists together:")
for name, age, city in zip(names, ages, cities):
    print(f"   {name} is {age} years old, from {city}")


# ------------------------ Summary ------------------------

print("\n\n" + "=" * 50)
print("📊 COMPLETE SUMMARY")
print("=" * 50)

print("""
✅ FOR LOOP DEFINITION:
   For Loop ek iteration control flow statement hai
   jo kisi iterable ke har element par ek-ek karke
   iterate karta hai aur har element ke liye code
   block execute karta hai.

✅ KEY TERMS:
   • Iterable  = Object jis par loop chal sake
   • Iteration = Loop ka ek complete chakkar
   • Iterator Variable = Har baar next element hold karta hai

✅ SYNTAX:
   for variable in iterable:
       # code block

✅ range() FUNCTION:
   • range(stop)         → 0, 1, 2, ..., stop-1
   • range(start, stop)  → start, ..., stop-1
   • range(start, stop, step) → start, start+step, ...

✅ WHAT IS i?
   i sirf ek variable name hai (convention)
   Koi bhi meaningful naam de sakte hain
   Har iteration mein automatically update hota hai

✅ ITERABLES YOU CAN LOOP:
   • List, Tuple, String, Set, Dictionary
   • range(), enumerate(), zip()
   • File objects, aur bahut kuch!

✅ GOLDEN RULES:
   • Colon (:) lagana kabhi mat bhoolna
   • Indentation (4 spaces) zaroori hai
   • range() mein stop include nahi hota
   • Loop body mein list modify na karein (unless copy banayi)
""")