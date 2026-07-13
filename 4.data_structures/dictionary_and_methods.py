# Dictionaries in Python

# Dictionary kya hoti hai?
#
# Dictionary ek collection hai jisme data KEY-VALUE pairs mein store hota hai.
# Har value ka ek unique key hota hai.
# Dictionary ORDERED hoti hai (Python 3.7+).
# Dictionary MUTABLE hoti hai (items add/update/delete kar sakte hain).

# Real Life Example:
# Jaise aapke phone mein Contacts hote hain:
# Name (Key) → Phone Number (Value)
# "Ibrahim" → "03123456789"
# "Ali"     → "03001234567"


# ------------------------ Creating a Dictionary ------------------------

# Curly Braces {} use karte hain (Bilkul Set ki tarah!)
# Lekin andar Key-Value pairs hote hain.

# ⚠️ IMPORTANT: Empty Dictionary vs Empty Set (CONFUSION!)

# Ye EMPTY DICTIONARY hai!
dictionary1 = {}
print(dictionary1)          # {}
print(type(dictionary1))    # <class 'dict'>

# Ye EMPTY SET hai!
empty_set = set()
print(empty_set)            # set()
print(type(empty_set))      # <class 'set'>

# Summary:
# {}      → Empty Dictionary
# set()   → Empty Set
# {1, 2}  → Set (Sirf values, no key:value)
# {1: "a", 2: "b"} → Dictionary (Key:Value pairs)


# ------------------------ Dictionary Structure ------------------------

# Dictionary = Key : Value pairs

# Syntax:
# {
#     key1 : value1,
#     key2 : value2,
#     key3 : value3
# }

# Key = Unique identifier (Jaise roll number)
# Value = Stored data (Jaise student ka naam)

dictionary2 = {"name": "Ibrahim", "age": 24}
print(dictionary2)          # {'name': 'Ibrahim', 'age': 24}

# Yahan:
# "name" → Key hai
# "Ibrahim" → Value hai

# "age" → Key hai
# 24 → Value hai


# ------------------------ Keys and Values ------------------------

# Keys ke Rules:
# ✅ Keys UNIQUE honi chahiye
# ✅ Keys IMMUTABLE honi chahiye (String, Number, Tuple chalenge)
# ❌ List, Dictionary keys nahi ho sakti (Mutable hain)

# Values ke Rules:
# ✅ Values kuch bhi ho sakti hain
# ✅ Duplicate values allowed hain
# ✅ List, Tuple, Set, Dictionary bhi value ho sakti hai


# ------------------------ Accessing Values ------------------------

# Square Brackets [] use karke key se value access karte hain.

marks = {"Ibrahim": 99, "Ali": 65, "Subhan": 50}
print(marks)                # {'Ibrahim': 99, 'Ali': 65, 'Subhan': 50}

# Key "Ibrahim" ki value:
print(marks["Ibrahim"])     # 99

# Key "Ali" ki value:
print(marks["Ali"])         # 65


# ⚠️ Case Sensitivity!

# Python Case Sensitive hai!
# "Ibrahim" aur "ibrahim" ALAG keys hain!

# print(marks["ibrahim"])
# Output:
# KeyError: 'ibrahim'

# Kyun?
# Kyunke dictionary mein "Ibrahim" key hai (Capital I)
# "ibrahim" key (Small i) EXIST nahi karti!

# Sahi access:
print(marks["Ibrahim"])     # 99 ✅


# ------------------------ get() Method ------------------------

# get() method bhi value access karta hai.
# Fark: Agar key nahi mili to ERROR nahi deta, None return karta hai.

print(marks.get("Ibrahim"))     # 99
print(marks.get("ibrahim"))     # None (Koi error nahi!)
print(marks.get("ibrahim", 0))  # 0 (Default value agar key nahi mili)


# marks["ibrahim"]   → KeyError (Program crash ho sakta hai)
# marks.get("ibrahim") → None (Safe!)


# ------------------------ Adding New Key-Value Pairs ------------------------

# Naya key-value pair add karna:

marks["Rehman"] = 86
print(marks)                # {'Ibrahim': 99, 'Ali': 65, 'Subhan': 50, 'Rehman': 86}

# Syntax:
# dictionary[new_key] = value


# ------------------------ Updating Existing Values ------------------------

# Agar key already exist karti hai, to value UPDATE ho jati hai.

marks["Ibrahim"] = 100
print(marks)                # {'Ibrahim': 100, 'Ali': 65, 'Subhan': 50, 'Rehman': 86}

# Ibrahim ke marks 99 se 100 ho gaye!


# ------------------------ Dictionary Properties ------------------------

# 1. Ordered (Python 3.7+)

# Python 3.7 se dictionaries ORDERED hain.
# Matlab items usi order mein rahenge jis order mein add kiye the.

student = {}
student["name"] = "Ibrahim"
student["age"] = 22
student["city"] = "Karachi"

print(student)              # {'name': 'Ibrahim', 'age': 22, 'city': 'Karachi'}
# Order preserved hai!


# 2. Mutable

# Dictionary mutable hai — items add/update/delete kar sakte hain.

info = {"name": "Ahmed", "age": 25}
info["age"] = 26            # Update
info["city"] = "Lahore"     # Add
print(info)                 # {'name': 'Ahmed', 'age': 26, 'city': 'Lahore'}


# 3. Keys are Unique

# Agar same key do baar likho, to last wali value overwrite ho jayegi.

test = {"a": 1, "b": 2, "a": 100}
print(test)                 # {'a': 100, 'b': 2}
# Pehli "a" ki value 1 overwrite ho gayi 100 se!


# 4. Keys must be Immutable

# Valid Keys:
dict1 = {1: "Number"}               # ✅ Integer
dict2 = {3.14: "Pi"}                # ✅ Float
dict3 = {"name": "Ibrahim"}         # ✅ String
dict4 = {(1, 2): "Tuple Key"}       # ✅ Tuple (Immutable)

# Invalid Keys:
# dict5 = {[1, 2]: "List Key"}      # ❌ List (Mutable) — TypeError
# dict6 = {{1: 2}: "Dict Key"}      # ❌ Dictionary (Mutable) — TypeError


# ------------------------ Dictionary Methods ------------------------

student = {
    "name": "Ibrahim",
    "age": 22,
    "course": "BSCS",
    "city": "Karachi"
}


# --- Access Methods ---

# keys() — Saari keys return karta hai

print(student.keys())       # dict_keys(['name', 'age', 'course', 'city'])

# Loop ke saath useful:
for key in student.keys():
    print(key)
# Output:
# name
# age
# course
# city


# values() — Saari values return karta hai

print(student.values())     # dict_values(['Ibrahim', 22, 'BSCS', 'Karachi'])

for value in student.values():
    print(value)
# Output:
# Ibrahim
# 22
# BSCS
# Karachi


# items() — Key-Value pairs return karta hai

print(student.items())
# dict_items([('name', 'Ibrahim'), ('age', 22), ('course', 'BSCS'), ('city', 'Karachi')])

# Loop ke saath:
for key, value in student.items():
    print(f"{key} = {value}")
# Output:
# name = Ibrahim
# age = 22
# course = BSCS
# city = Karachi


# --- Update Methods ---

# update() — Ek dictionary se doosri dictionary update karna

info1 = {"name": "Ibrahim", "age": 22}
info2 = {"city": "Karachi", "age": 23}    # age overwrite hogi!

info1.update(info2)
print(info1)                # {'name': 'Ibrahim', 'age': 23, 'city': 'Karachi'}

# info2 ki saari key-values info1 mein add/update ho gayin!


# --- Remove Methods ---

# pop(key) — Key delete karta hai aur value return karta hai

marks = {"Ibrahim": 99, "Ali": 65, "Subhan": 50}

removed_value = marks.pop("Ali")
print("Removed:", removed_value)    # 65
print("Dictionary:", marks)         # {'Ibrahim': 99, 'Subhan': 50}

# Agar key nahi mili to ERROR:
# marks.pop("Rehman")    # KeyError: 'Rehman'


# popitem() — Last added key-value pair delete + return karta hai

marks = {"Ibrahim": 99, "Ali": 65, "Subhan": 50}

last_item = marks.popitem()
print("Removed:", last_item)        # ('Subhan', 50)
print("Dictionary:", marks)         # {'Ibrahim': 99, 'Ali': 65}


# del — Specific key delete karta hai

marks = {"Ibrahim": 99, "Ali": 65, "Subhan": 50}

del marks["Ali"]
print(marks)                # {'Ibrahim': 99, 'Subhan': 50}


# clear() — Poori dictionary khali kar deta hai

marks.clear()
print(marks)                # {}


# --- Check Methods ---

# len() — Dictionary ki length (Kitne key-value pairs hain)

student = {"name": "Ibrahim", "age": 22, "city": "Karachi"}
print(len(student))         # 3


# in / not in — Key exist karti hai ya nahi

print("name" in student)        # True
print("email" in student)       # False
print("email" not in student)   # True

# ⚠️ 'in' sirf KEYS check karta hai, VALUES nahi!

print("Ibrahim" in student)         # False (Value hai, key nahi)
print("Ibrahim" in student.values()) # True (Values check karne ke liye)


# copy() — Dictionary ki copy banata hai

original = {"a": 1, "b": 2}
duplicate = original.copy()
print(duplicate)            # {'a': 1, 'b': 2}


# setdefault() — Agar key nahi hai to default value set karta hai

data = {"name": "Ibrahim"}

# Agar "age" key nahi hai, to 22 set karo
age = data.setdefault("age", 22)
print(age)                  # 22
print(data)                 # {'name': 'Ibrahim', 'age': 22}

# Agar "name" key already hai, to existing value return karega
name = data.setdefault("name", "Unknown")
print(name)                 # Ibrahim (Existing value)
print(data)                 # {'name': 'Ibrahim', 'age': 22} (No change)


# fromkeys() — Multiple keys ke saath dictionary banana (Same value)

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)             # {'a': 0, 'b': 0, 'c': 0}

keys2 = ["name", "age", "city"]
default_dict = dict.fromkeys(keys2, "N/A")
print(default_dict)         # {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}


# ------------------------ Nested Dictionary ------------------------

# Dictionary ke andar dictionary!

students = {
    "student1": {
        "name": "Ibrahim",
        "age": 22,
        "marks": 99
    },
    "student2": {
        "name": "Ali",
        "age": 21,
        "marks": 65
    }
}

# Access:
print(students["student1"]["name"])     # Ibrahim
print(students["student2"]["marks"])    # 65


# ------------------------ Real Life Examples ------------------------

# Example 1: Contact Book

contacts = {
    "Ibrahim": "03123456789",
    "Ali": "03001234567",
    "Sara": "03339876543"
}

# Find Ali's number:
print(contacts.get("Ali", "Not Found"))

# Add new contact:
contacts["Ahmed"] = "03451234567"


# Example 2: Word Counter

# Kaunsa word kitni baar aaya? (Dictionary se easy!)

text = "apple banana apple mango banana apple"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# {'apple': 3, 'banana': 2, 'mango': 1}


# Example 3: Student Record

student = {
    "name": "Ibrahim",
    "age": 22,
    "courses": ["Python", "JavaScript", "HTML"],
    "address": {
        "city": "Karachi",
        "area": "Gulshan"
    }
}

print(student["courses"][0])           # Python
print(student["address"]["city"])      # Karachi


# ------------------------ Dictionary vs List vs Set ------------------------

# ┌──────────────────┬───────────┬───────────┬──────────────┬──────────────┐
# │ Property         │ List      │ Tuple     │ Set          │ Dictionary   │
# ├──────────────────┼───────────┼───────────┼──────────────┼──────────────┤
# │ Ordered?         │ ✅ Yes    │ ✅ Yes    │ ❌ No        │ ✅ Yes (3.7+)│
# │ Mutable?         │ ✅ Yes    │ ❌ No     │ ✅ Yes       │ ✅ Yes       │
# │ Duplicates?      │ ✅ Yes    │ ✅ Yes    │ ❌ No        │ ❌ Keys No   │
# │ Indexing?        │ ✅ [0]    │ ✅ [0]    │ ❌ No        │ ✅ [key]     │
# │ Structure        │ [v1, v2]  │ (v1, v2)  │ {v1, v2}     │ {k1:v1, k2:v2}│
# │ Empty            │ []        │ ()        │ set()        │ {}           │
# └──────────────────┴───────────┴───────────┴──────────────┴──────────────┘


# ------------------------ Common Confusions ------------------------

# Confusion 1: {} — Empty Set ya Empty Dictionary?

# {}      → Dictionary
# set()   → Set
# {1, 2}  → Set (No key:value)
# {1: "a"} → Dictionary (Key:Value)


# Confusion 2: Access — [] vs get()

# marks["key"]       → Key nahi mili to KeyError
# marks.get("key")   → Key nahi mili to None (Safe!)


# Confusion 3: Case Sensitivity

# Keys case sensitive hain!
# "Name" aur "name" ALAG keys hain.


# ------------------------ Summary ------------------------

# Dictionary = Key-Value pairs ka collection.

# Creating:
#   → {} se empty dictionary
#   → set() se empty set (Confusion clear!)
#   → {"key": "value", "key2": "value2"}

# Access:
#   → dict["key"]          — Error agar key nahi mili
#   → dict.get("key")      — None agar key nahi mili (Safe!)
#   → dict.get("key", 0)   — Default value

# Adding/Updating:
#   → dict["new_key"] = value    — Add new
#   → dict["existing_key"] = value — Update
#   → dict.update({...})         — Multiple add/update

# Removing:
#   → dict.pop("key")      — Delete + return value (Error if not found)
#   → dict.popitem()       — Delete + return last item
#   → del dict["key"]      — Delete key
#   → dict.clear()         — Empty dictionary

# Methods:
#   → keys()     — Saari keys
#   → values()   — Saari values
#   → items()    — Key-Value pairs
#   → get()      — Safe access
#   → update()   — Add/Update multiple
#   → copy()     — Duplicate dictionary

# Properties:
#   → Keys UNIQUE hain
#   → Keys IMMUTABLE honi chahiye (String, Number, Tuple)
#   → Values kuch bhi ho sakti hain
#   → Mutable (Add/Update/Delete)
#   → Ordered (Python 3.7+)
#   → Case sensitive keys!