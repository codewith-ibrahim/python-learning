# Sets in Python


# Pehle yeh parhlein Taaky Understanding hon about set!
# Agar aapko Mathematics ka Set Theory nahi aata,
# To pehle `set_theory.txt` file padhein.
# Uske baad ye file aapko BOHOT EASY lagegi!
# Sets ka Mathematical Concept
# (Recap from set_theory.txt)
# Set = Unique elements ka collection
# Unordered hota hai
# Duplicates allow nahi hote
# Operations: Union, Intersection, Difference, Symmetric Difference



# ------------------------ Start Set ------------------------


# Set kya hota hai?
#
# Set ek collection hai jisme hum multiple items store kar sakte hain.
# Set UNORDERED hota hai (items ka koi index nahi hota).
# Set MUTABLE hota hai (items add/delete kar sakte hain).
# Set DUPLICATE VALUES allow nahi karta!


# Sets ka Mathematical Concept

# Set ka concept Mathematics se aaya hai.
# Mathematics mein Set = Unique elements ka collection.

# Jaise:
# A = {1, 2, 3, 4, 5}
# B = {2, 4, 6, 8}

# Python ka set bilkul mathematical set ki tarah kaam karta hai!


# ------------------------ Creating a Set ------------------------

# Curly Braces {} use karte hain

set1 = {3, 5, 10, 20, 30}

print(type(set1))      # <class 'set'>
print(set1)            # {10, 3, 20, 5, 30}

# ⚠️ Output order different ho sakta hai!
# Kyun?
# Set unordered hota hai — items ka koi fixed order nahi hota.


# ------------------------ Duplicate Values ------------------------

# Ye set ka SABSE IMPORTANT feature hai!
# Set duplicate values ko IGNORE kar deta hai.

set2 = {3, 5, 10, 10, 10, 20, 30}

print(set2)            # {10, 3, 20, 5, 30}

# Yahan 10 teen baar likha gaya, lekin set mein sirf EK BAAR aayega!
# Matlab: Set automatically duplicates remove kar deta hai.


# Another Example:

set3 = {1, 1, 1, 2, 2, 3, 3, 3, 3}
print(set3)            # {1, 2, 3}


# ------------------------ Why Use Sets? (Real Life Example) ------------------------

# Socho tumhare paas students ki list hai, aur tumhe pata karna hai
# ke TOTAL KITNE UNIQUE students hain.

students = ["Ibrahim", "Ahmed", "Ibrahim", "Ali", "Ahmed", "Sara", "Ali"]
print("Total Students List:", len(students))      # 7

unique_students = set(students)
print("Unique Students:", unique_students)         # {'Ibrahim', 'Ali', 'Ahmed', 'Sara'}
print("Total Unique Students:", len(unique_students))  # 4

# Bahut kaam ki cheez hai! ❤️


# ------------------------ Empty Set ------------------------

# ⚠️ IMPORTANT: Empty set banane ka tareeqa!

# Ye EMPTY SET nahi hai — Ye EMPTY DICTIONARY hai!
empty_dict = {}
print(type(empty_dict))    # <class 'dict'>

# Sahi tareeqa — Empty Set:
empty_set = set()
print(type(empty_set))     # <class 'set'>


# ------------------------ Set Properties ------------------------

# 1. Unordered — Items ka koi index nahi hota

my_set = {10, 20, 30, 40, 50}

# print(my_set[0])    # ❌ TypeError: 'set' object is not subscriptable

# Matlab:
# String, List, Tuple ki tarah Indexing KAAM NAHI KARTI.
# Kyunke set unordered hai — "pehla item" ka concept hi nahi hai!


# 2. Mutable — Items add/delete kar sakte hain

fruits = {"Apple", "Banana"}
fruits.add("Mango")              # Add item
print(fruits)                    # {'Apple', 'Mango', 'Banana'}

fruits.remove("Banana")          # Remove item
print(fruits)                    # {'Apple', 'Mango'}


# 3. No Duplicates — Har item unique hota hai

numbers = {1, 2, 2, 3, 3, 3}
print(numbers)                   # {1, 2, 3}


# ------------------------ Set Methods ------------------------

# --- Adding Items ---

# add() — Ek item add karta hai

colors = {"Red", "Green"}
colors.add("Blue")
print(colors)                    # {'Red', 'Blue', 'Green'}

# Agar duplicate add karo to kuch nahi hoga!

colors.add("Red")
print(colors)                    # {'Red', 'Blue', 'Green'} — Red already hai


# update() — Multiple items add karta hai (List, Tuple, Set se)

colors.update(["Yellow", "Purple"])
print(colors)                    # {'Red', 'Blue', 'Green', 'Yellow', 'Purple'}


# --- Removing Items ---

# remove() — Item delete karta hai (Agar nahi mila to ERROR)

fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)                    # {'Apple', 'Mango'}

# fruits.remove("Orange")
# Output:
# KeyError: 'Orange'    ← Kyunke Orange set mein nahi hai!


# discard() — Item delete karta hai (Agar nahi mila to KOI ERROR NAHI)

fruits = {"Apple", "Banana", "Mango"}
fruits.discard("Banana")
print(fruits)                    # {'Apple', 'Mango'}

fruits.discard("Orange")         # ✅ Koi error nahi aayega!
print(fruits)                    # {'Apple', 'Mango'}


# remove() vs discard():
#   remove() → Item nahi mila to ERROR
#   discard() → Item nahi mila to CHUP CHAP ignore


# pop() — Kisi BHI ek item ko delete karta hai aur return karta hai

nums = {10, 20, 30, 40}
deleted = nums.pop()
print("Deleted:", deleted)       # Koi bhi item delete ho sakta hai
print("Remaining:", nums)        # Baaki items

# ⚠️ Kyunke set unordered hai, pata nahi kaunsa item delete hoga!


# clear() — Poora set khali kar deta hai

temp = {1, 2, 3}
temp.clear()
print(temp)                      # set()


# --- Checking Items ---

# len() — Set ki length

my_set = {10, 20, 30, 40, 50}
print(len(my_set))               # 5


# Membership Operator (in / not in)

print(10 in my_set)              # True
print(100 in my_set)             # False
print(100 not in my_set)         # True


# ------------------------ Mathematical Set Operations ------------------------

# Ye sets ka SABSE POWERFUL feature hai!
# Mathematics ke set operations Python mein available hain.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)               # {1, 2, 3, 4, 5}
print("Set B:", B)               # {4, 5, 6, 7, 8}


# 1. Union (|) — Dono sets ke saare items (No duplicates)

union_set = A | B
# Ya: A.union(B)

print("A ∪ B (Union):", union_set)         # {1, 2, 3, 4, 5, 6, 7, 8}

# Matlab: Dono sets ke sab unique items.


# 2. Intersection (&) — Sirf common items

intersection_set = A & B
# Ya: A.intersection(B)

print("A ∩ B (Intersection):", intersection_set)  # {4, 5}

# Matlab: Jo items DONO sets mein hon.


# 3. Difference (-) — Pehle set mein hain lekin doosre mein nahi

diff_A_B = A - B
# Ya: A.difference(B)

print("A - B (Difference):", diff_A_B)    # {1, 2, 3}

# Matlab: A mein hain, B mein nahi hain.


diff_B_A = B - A
print("B - A (Difference):", diff_B_A)    # {8, 6, 7}

# Matlab: B mein hain, A mein nahi hain.


# 4. Symmetric Difference (^) — Jo DONO mein COMMON NAHI hain

sym_diff = A ^ B
# Ya: A.symmetric_difference(B)

print("A △ B (Symmetric Diff):", sym_diff)  # {1, 2, 3, 6, 7, 8}

# Matlab: Jo sirf kisi EK set mein ho, dono mein na ho.


# ------------------------ Real Life Examples ------------------------

# Example 1: Common Friends (Intersection)

my_friends = {"Ahmed", "Ali", "Sara", "Zain"}
your_friends = {"Ali", "Zain", "Omar", "Fatima"}

common_friends = my_friends & your_friends
print("Common Friends:", common_friends)     # {'Ali', 'Zain'}


# Example 2: All Friends (Union)

all_friends = my_friends | your_friends
print("All Friends:", all_friends)
# {'Ahmed', 'Ali', 'Sara', 'Zain', 'Omar', 'Fatima'}


# Example 3: Remove Duplicates from List (Quick Trick!)

numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_with_duplicates))
print("Unique Numbers:", unique_numbers)     # [1, 2, 3, 4, 5]


# ------------------------ Set vs List vs Tuple ------------------------

# | Property      | List        | Tuple       | Set          |
# |---------------|-------------|-------------|--------------|
# | Ordered?      | ✅ Yes      | ✅ Yes      | ❌ No        |
# | Mutable?      | ✅ Yes      | ❌ No       | ✅ Yes       |
# | Duplicates?   | ✅ Allowed  | ✅ Allowed  | ❌ Not Allowed|
# | Indexing?     | ✅ [0]      | ✅ [0]      | ❌ No        |
# | Slicing?      | ✅ [0:3]    | ✅ [0:3]    | ❌ No        |
# | Math Ops?     | ❌ No       | ❌ No       | ✅ Union, Intersection, etc. |


# ------------------------ Frozen Set ------------------------

# Frozen Set = IMMUTABLE version of Set
# Create hone ke baad change nahi kar sakte.

normal_set = {1, 2, 3}
normal_set.add(4)              # ✅ Ho gaya

frozen = frozenset({1, 2, 3})
# frozen.add(4)                # ❌ AttributeError: 'frozenset' object has no attribute 'add'

print(type(frozen))            # <class 'frozenset'>


# ------------------------ Summary ------------------------

# Set = Unordered, Mutable, No Duplicates.

# Set ka mathematical concept:
#   → Unique elements ka collection

# Set ki Properties:
#   → Unordered (Indexing kaam nahi karti)
#   → Mutable (Items add/delete kar sakte hain)
#   → No Duplicates (Har item unique hota hai)

# Empty Set: set()  ← {} empty dictionary hota hai!

# Important Methods:
#   → add()        — Ek item add
#   → update()     — Multiple items add
#   → remove()     — Delete (Error agar nahi mila)
#   → discard()    — Delete (No error)
#   → pop()        — Random item delete + return
#   → clear()      — Poora set khali

# Mathematical Operations:
#   → Union (|)              — Sab items
#   → Intersection (&)       — Common items
#   → Difference (-)         — Sirf pehle set ke items
#   → Symmetric Diff (^)     — Non-common items

# Real Life Use:
#   → Remove duplicates from list
#   → Find common elements
#   → Unique collections