# String Formatting in Python

# String Formatting kya hoti hai?
#
# String Formatting ka matlab:
# String ke andar variables ya values ko DYNAMICALLY insert karna.
#
# Jaise:
# "Mera naam Ibrahim hai aur meri age 22 hai"
# Yahan "Ibrahim" aur "22" dynamic hain — har student ke liye alag honge.


# ------------------------ Why String Formatting? ------------------------

# Bina Formatting ke (Purana Tareeqa — Mushkil):

name = "Ibrahim"
age = 22
city = "Karachi"

# Concatenation se:
print("My name is " + name + ", I am " + str(age) + " years old, from " + city)
# Output: My name is Ibrahim, I am 22 years old, from Karachi

# Problems:
# ❌ Baar baar + lagana padta hai
# ❌ Numbers ko str() se convert karna padta hai
# ❌ Quotes ka chakkar
# ❌ Padhne mein mushkil

# Isi liye String Formatting ka use karte hain!


# ------------------------ 1. f-string (MODERN & BEST) ------------------------

# f-string Python 3.6+ mein aaya.
# Ye SABSE EASY aur SABSE FAST tareeqa hai.
# RECOMMENDED: Hamesha f-string use karo!

# Syntax:
# f"Text {variable} text {variable}"

name = "Ibrahim"
age = 22

print(f"My name is {name} and I am {age} years old.")
# Output: My name is Ibrahim and I am 22 years old.


# f-string ka Simple Rule:
# String ke starting mein 'f' lagao
# Jahan variable chahiye, wahan {curly braces} mein variable ka naam likho
# Python automatically value replace kar dega!


# Example 1: Basic

first_name = "Shaikh"
last_name = "Ibrahim"

print(f"Full Name: {first_name} {last_name}")
# Output: Full Name: Shaikh Ibrahim


# Example 2: Calculations Inside {}

price = 250
quantity = 3

print(f"Total Bill: Rs. {price * quantity}")
# Output: Total Bill: Rs. 750

# Curly braces ke andar EXPRESSION bhi likh sakte hain!


# Example 3: Methods Inside {}

text = "python"

print(f"Uppercase: {text.upper()}")
# Output: Uppercase: PYTHON

print(f"Capitalize: {text.capitalize()}")
# Output: Capitalize: Python


# Example 4: Multiple Variables

student_name = "Ibrahim"
student_marks = 95
student_grade = "A+"
student_city = "Karachi"

print(f"{student_name} from {student_city} got {student_marks} marks ({student_grade} grade)")
# Output: Ibrahim from Karachi got 95 marks (A+ grade)


# Example 5: Dictionary ke saath

student = {"name": "Ali", "age": 21, "course": "BSCS"}

print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
# Output: Name: Ali, Age: 21, Course: BSCS


# Example 6: List ke saath

fruits = ["Apple", "Banana", "Mango"]

print(f"First Fruit: {fruits[0]}, Last Fruit: {fruits[-1]}")
# Output: First Fruit: Apple, Last Fruit: Mango


# ------------------------ 2. .format() Method (PURANA — BUT STILL USED) ------------------------

# f-string se pehle .format() use hota tha.
# Abhi bhi purane code mein milta hai.

# Syntax:
# "Text {} text {}".format(value1, value2)

name = "Ibrahim"
age = 22

print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Ibrahim and I am 22 years old.

# Jahan {} likho, wahan .format() ke arguments SEQUENCE mein replace honge.


# Example 1: Positional Arguments

print("{} loves {}.".format("Ibrahim", "Python"))
# Output: Ibrahim loves Python.
# Pehla {} → Pehla argument ("Ibrahim")
# Doosra {} → Doosra argument ("Python")


# Example 2: Index Numbers (Order Change)

print("{1} loves {0}.".format("Python", "Ibrahim"))
# Output: Ibrahim loves Python.
# {1} → Doosra argument ("Ibrahim")
# {0} → Pehla argument ("Python")


# Example 3: Named Arguments

print("My name is {name} and I am {age} years old.".format(name="Ali", age=25))
# Output: My name is Ali and I am 25 years old.


# Example 4: Repeated Use

print("{0} is learning {1}. {0} loves {1}!".format("Ibrahim", "Python"))
# Output: Ibrahim is learning Python. Ibrahim loves Python!


# ------------------------ 3. % Formatting (OLDEST — NOT RECOMMENDED) ------------------------

# Ye C language style hai.
# Python 2 mein use hota tha.
# Ab use nahi karte, lekin purane code mein mil sakta hai.

# %s → String
# %d → Integer
# %f → Float

name = "Ibrahim"
age = 22

print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Ibrahim and I am 22 years old.


# ------------------------ f-string Advanced Features ------------------------

# 1. Number Formatting

price = 49.99999

# Decimal places limit karna
print(f"Price: {price:.2f}")      # 2 decimal tak
# Output: Price: 50.00

print(f"Price: {price:.1f}")      # 1 decimal tak
# Output: Price: 50.0


# 2. Comma in Large Numbers

population = 245209815

print(f"Pakistan Population: {population:,}")
# Output: Pakistan Population: 245,209,815


# 3. Percentage

success_rate = 0.857

print(f"Success Rate: {success_rate:.1%}")
# Output: Success Rate: 85.7%


# 4. Padding (Spaces Add Karna)

name = "Ali"

# Left pad (Right aligned)
print(f"Name: {name:>10}")      # 10 characters ki jagah, name right side
# Output: Name:        Ali

# Right pad (Left aligned)
print(f"Name: {name:<10}")      # 10 characters ki jagah, name left side
# Output: Name: Ali

# Center pad
print(f"Name: {name:^10}")      # 10 characters ki jagah, name center mein
# Output: Name:    Ali


# 5. Binary, Hex, Octal

number = 255

print(f"Decimal: {number}")         # 255
print(f"Binary:  {number:b}")       # 11111111
print(f"Hex:    {number:x}")        # ff
print(f"Octal:  {number:o}")        # 377


# 6. Date and Time Formatting

from datetime import datetime

now = datetime.now()

print(f"Today: {now:%d-%m-%Y}")           # 09-07-2026
print(f"Time: {now:%H:%M:%S}")            # 14:30:45
print(f"Full: {now:%d %B, %Y %I:%M %p}") # 09 July, 2026 02:30 PM


# ------------------------ Real Life Examples ------------------------

# Example 1: Bill Receipt (Restaurant)

item = "Biryani"
price = 250
quantity = 2
total = price * quantity

print("\n" + "=" * 30)
print("🧾 BILL RECEIPT")
print("=" * 30)
print(f"Item:     {item}")
print(f"Price:    Rs. {price}")
print(f"Quantity: {quantity}")
print(f"Total:    Rs. {total}")
print("=" * 30 + "\n")


# Example 2: Student Report Card

student = {
    "name": "Shaikh Ibrahim",
    "roll": 101,
    "marks": 487,
    "total": 500,
    "grade": "A+"
}

percentage = (student["marks"] / student["total"]) * 100

print("=" * 35)
print("📊 STUDENT REPORT CARD")
print("=" * 35)
print(f"Name:       {student['name']}")
print(f"Roll No:    {student['roll']}")
print(f"Marks:      {student['marks']}/{student['total']}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:      {student['grade']}")
print("=" * 35)


# Example 3: Progress Bar

total = 100
completed = 67

print(f"Progress: [{completed}/{total}] {completed/total:.0%}")
# Output: Progress: [67/100] 67%


# Example 4: Table Formatting

print("\n📋 STUDENT LIST")
print("-" * 40)
print(f"{'Name':<15} {'Age':<8} {'City':<12}")
print("-" * 40)
print(f"{'Ibrahim':<15} {22:<8} {'Karachi':<12}")
print(f"{'Ali':<15} {21:<8} {'Lahore':<12}")
print(f"{'Sara':<15} {23:<8} {'Islamabad':<12}")
print("-" * 40)
# Proper table columns!


# Example 5: Personalized Message

username = "Ibrahim"
score = 95
rank = 3

print(f"\n🎉 Congratulations, {username}!")
print(f"You scored {score} marks and secured Rank #{rank}!")
print(f"Keep up the great work, {username}!\n")


# ------------------------ Comparison Table ------------------------

print("\n" + "=" * 50)
print("FORMATTING METHODS COMPARISON")
print("=" * 50)

name = "Ibrahim"
age = 22

# f-string (Best ✅)
print(f"f-string:  My name is {name} and I am {age} years old.")

# .format() (OK ⚠️)
print(".format(): My name is {} and I am {} years old.".format(name, age))

# % formatting (Old ❌)
print("% style:  My name is %s and I am %d years old." % (name, age))

# Concatenation (Avoid ❌)
print("Concat:    My name is " + name + " and I am " + str(age) + " years old.")


# ------------------------ Which One to Use? ------------------------

# ┌───────────────────┬──────────┬────────────────────┬─────────────┐
# │ Method            │ Example  │ Recommendation     │ Speed       │
# ├───────────────────┼──────────┼────────────────────┼─────────────┤
# │ f-string          │ f"{x}"   │ ✅ BEST (Use This) │ Fastest     │
# │ .format()         │ "{}".f() │ ⚠️ OK (Old Code)   │ Medium      │
# │ % formatting      │ "%s" % x │ ❌ Avoid            │ Slow        │
# │ Concatenation     │ "a" + b  │ ❌ Avoid            │ Slowest     │
# └───────────────────┴──────────┴────────────────────┴─────────────┘


# ------------------------ Common Mistakes ------------------------

# Mistake 1: f-string mein 'f' bhoolna

name = "Ibrahim"
# print("{name}")          # Output: {name} (Variable replace nahi hua!)
print(f"{name}")            # Output: Ibrahim ✅


# Mistake 2: Curly braces ke andar quotes

# print(f"{'name'}")        # Confusing! 'name' string treat hoga
print(f"{name}")             # Sahi! Variable name use karo


# Mistake 3: .format() mein index mismatch

# print("{0} {2}".format("A", "B"))   # IndexError! {2} exist nahi karta
print("{0} {1}".format("A", "B"))     # Sahi! ✅


# Mistake 4: f-string with dictionary (wrong quotes)

student = {"name": "Ali"}

# print(f"{student['name']}")    # ERROR! Single quotes conflict
print(f"{student['name']}")      # Sahi! Double quotes bahar, single andar


# ------------------------ Best Practices ------------------------

# ✅ f-string use karo (Python 3.6+)
# ✅ Numbers format karo (.2f, :,)
# ✅ Table data ko align karo (<, >, ^)
# ✅ Expressions directly {} mein likho
# ✅ Multi-line ke liye triple quotes + f""" """

# Multi-line f-string Example:

name = "Ibrahim"
age = 22
city = "Karachi"

bio = f"""
╔══════════════════╗
║   USER PROFILE   ║
╠══════════════════╣
║ Name: {name:<10} ║
║ Age:  {age:<10} ║
║ City: {city:<9} ║
╚══════════════════╝
"""
print(bio)


# ------------------------ Summary ------------------------

# String Formatting = String mein variables insert karna

# 3 Methods:
#   1. f-string:    f"Hello {name}"           ← BEST ✅
#   2. .format():   "Hello {}".format(name)   ← OK ⚠️
#   3. % style:     "Hello %s" % name         ← AVOID ❌

# f-string Features:
#   → {variable}         — Variable insert
#   → {expression}       — Calculation (a + b)
#   → {method}           — .upper(), .lower()
#   → {value:.2f}        — Decimal places
#   → {value:,}          — Comma in numbers
#   → {value:.1%}        — Percentage
#   → {value:>10}        — Right align
#   → {value:<10}        — Left align
#   → {value:^10}        — Center align

# Real Life Use:
#   → Bill receipts
#   → Report cards
#   → Table formatting
#   → Personalized messages
#   → Progress bars

# Golden Rule:
# HAMESHA f-string use karo! 🏆