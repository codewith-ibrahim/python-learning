# Escape Characters in Python

# Escape Characters kya hote hain?
#
# Escape Characters wo special characters hain jo
# string ke andar SPECIAL FORMATTING provide karte hain.
#
# Ye hamesha BACKSLASH (\) se start hote hain.
# Isi liye inhe "Escape Sequence" bhi kehte hain.


# ------------------------ \n — New Line ------------------------

# \n ka matlab: NEW LINE
# \n jahan bhi likho, cursor NEXT LINE par chala jata hai.

# Real Life Example:
# Jaise aap WhatsApp mein message likhte ho:
# "Hello"
# "Kaise ho?"
# Enter press karke nayi line mein likhte ho.
# \n wahi kaam karta hai — Enter press karne jaisa!


# Without \n (Sab ek line mein):

print("Hello World! Kaise ho? Kya kar rahe ho?")
# Output:
# Hello World! Kaise ho? Kya kar rahe ho?
# (Sab ek hi line mein aaya)


# With \n (Nayi line mein):

print("Hello World!\nKaise ho?\nKya kar rahe ho?")
# Output:
# Hello World!
# Kaise ho?
# Kya kar rahe ho?
# (Teen alag lines mein aaya!)


# \n ka simple rule:
# Jahan \n likho, wahan se nayi line start ho jati hai.


# Example 2: Poem Print Karna

print("Twinkle twinkle little star\nHow I wonder what you are\nUp above the world so high\nLike a diamond in the sky")
# Output:
# Twinkle twinkle little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky


# Example 3: Aapke Code Mein Use (driving_license.py se)

print("Checking eligibility...\n")
# Iska matlab:
# "Checking eligibility..." print karo
# Phir \n se nayi line
# Phir ek aur \n??
# Wait... \n ke baad kuch nahi hai??

# Important samjho:
# print("Checking eligibility...\n")

# \n ke baad jo next line hai wo KHALI hai
# Isliye output mein EK KHAALI LINE bhi aayegi!

# Output:
# Checking eligibility...
#                          ← Ye khali line \n ki wajah se aayi!
# (Phir agla print statement)

# Visual Representation:
# print("Checking eligibility...\n")
#        |                      |
#        |                      └→ New line + Nothing = Khali line!
#        └→ "Checking eligibility..." print hua


# Example 4: \n with Different Positions

# 1. \n at the END (Jaise aapne use kiya)
print("Checking eligibility...\n")
print("Next line")
# Output:
# Checking eligibility...
#                          ← Khali line
# Next line

# 2. \n at the START
print("\nHello World")
# Output:
#                          ← Khali line (pehle new line)
# Hello World

# 3. \n in the MIDDLE
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

# 4. Multiple \n
print("Start\n\n\nEnd")
# Output:
# Start
#                          ← Khali line
#                          ← Khali line
# End
# (Do khali lines aayin, kyunke do \n continuously hain!)


# ------------------------ \t — Tab Space ------------------------

# \t ka matlab: TAB SPACE
# \t jahan likho, wahan 4 spaces ke barabar GAP aa jata hai.

# Real Life Example:
# Jaise aap keyboard par TAB key press karte ho,
# cursor thoda aage chala jata hai.
# \t wahi kaam karta hai!


# Without \t (Sab aage peeche chipka hua):

print("Name Age City")
print("Ibrahim 22 Karachi")
print("Ali 21 Lahore")
# Output:
# Name Age City
# Ibrahim 22 Karachi
# Ali 21 Lahore
# (Format sahi nahi hai)


# With \t (Proper gap):

print("Name\tAge\tCity")
print("Ibrahim\t22\tKarachi")
print("Ali\t21\tLahore")
# Output:
# Name    Age     City
# Ibrahim 22      Karachi
# Ali     21      Lahore
# (Ab proper table jaisa lag raha hai!)


# \t ka simple rule:
# Jahan \t likho, wahan TAB space aa jata hai.
# Tab space = 4 ya 8 spaces ke barabar hota hai.


# Example: Bill Receipt

print("=" * 30)
print("ITEM\t\tPRICE")
print("-" * 30)
print("Biryani\t\tRs. 250")
print("Cold Drink\tRs. 80")
print("Ice Cream\tRs. 100")
print("=" * 30)
# Output:
# ==============================
# ITEM            PRICE
# ------------------------------
# Biryani         Rs. 250
# Cold Drink      Rs. 80
# Ice Cream       Rs. 100
# ==============================


# ------------------------ \\ — Backslash ------------------------

# \\ ka matlab: EK Backslash (\) print karna

# Problem:
# Agar hum print("C:\Users\Ibrahim") likhein
# To \U aur \I escape sequences ki tarah treat honge!

# Solution: \\ use karo

print("C:\\Users\\Ibrahim\\Documents")
# Output:
# C:\Users\Ibrahim\Documents


# ------------------------ \" — Double Quotes ------------------------

# \" ka matlab: String ke andar Double Quotes (") print karna

# Problem:
# print("He said "Hello" to me")
# Ye Error dega! Kyunke "Hello" ke quotes string end kar rahe hain.

# Solution: \" use karo

print("He said \"Hello\" to me")
# Output:
# He said "Hello" to me


# ------------------------ \' — Single Quote ------------------------

# \' ka matlab: String ke andar Single Quote (') print karna

print('It\'s a beautiful day')
# Output:
# It's a beautiful day

# Ya double quotes mein single quote bina escape ke chalega:
print("It's a beautiful day")
# Output:
# It's a beautiful day


# ------------------------ All Escape Characters Table ------------------------

# ┌─────────────────┬──────────────────────────────┬──────────────────────┐
# │ Escape Sequence │ Meaning                      │ Example              │
# ├─────────────────┼──────────────────────────────┼──────────────────────┤
# │ \n              │ New Line                     │ "Hello\nWorld"       │
# │ \t              │ Tab Space                    │ "Name\tAge"          │
# │ \\              │ Backslash                    │ "C:\\Users"          │
# │ \"              │ Double Quote                 │ "He said \"Hi\""     │
# │ \'              │ Single Quote                 │ 'It\'s Python'       │
# └─────────────────┴──────────────────────────────┴──────────────────────┘


# ------------------------ \n in Detail (Most Important) ------------------------

# \n ka Pura Concept Samjho:

# Pehla Print:
print("Checking eligibility...\n")
# Breakdown:
# "Checking eligibility..." → Ye text print hua
# \n                        → Cursor nayi line mein gaya
#                            (aur kuch nahi likha to khali line)
# Output ke baad cursor next line par ready hai

# Visual:
# Terminal Screen:
# ┌──────────────────────────────┐
# │ Checking eligibility...      │ ← Text print hua
# │                              │ ← \n ki wajah se yahan khali line
# │ █                            │ ← Cursor yahan hai (agla print yahan se)
# └──────────────────────────────┘

# Doosra Print:
print("You are eligible!")
# Output (Continuation from above):
# Checking eligibility...
#                              ← Khali line (\n ki wajah se)
# You are eligible!


# Without Extra \n:
print("Checking eligibility...")
print("You are eligible!")
# Output:
# Checking eligibility...
# You are eligible!
# (No khali line in between)


# ------------------------ Practical Examples ------------------------

# Example 1: Menu Display (Restaurant Style)

print("\n" + "=" * 30)        # Pehle nayi line, phir border
print("🍽️  MENU")
print("=" * 30)
print("1. Biryani\n2. Burger\n3. Pizza\n4. Cold Drink")
print("=" * 30 + "\n")         # Border ke baad nayi line + khali line

# Output:
# 
# ==============================
# 🍽️  MENU
# ==============================
# 1. Biryani
# 2. Burger
# 3. Pizza
# 4. Cold Drink
# ==============================
#                               ← Khali line (end wale \n se)


# Example 2: Student Report Card

name = "Ibrahim"
grade = "A+"
marks = 95

print("\n" + "=" * 30)
print("📊 REPORT CARD")
print("=" * 30)
print(f"Name:\t{name}")
print(f"Grade:\t{grade}")
print(f"Marks:\t{marks}%")
print("=" * 30 + "\n")

# Output:
# 
# ==============================
# 📊 REPORT CARD
# ==============================
# Name:   Ibrahim
# Grade:  A+
# Marks:  95%
# ==============================
#                               ← Khali line


# Example 3: Loading Screen Jaisa Feel

print("Loading...\n")
print("Please wait...\n")
print("Complete!")
# Output:
# Loading...
#                               ← Khali
# Please wait...
#                               ← Khali
# Complete!


# ------------------------ \n ke Bina vs \n ke Saath ------------------------

# Bina \n (Less Readable):

print("Welcome to Python Learning!")
print("Today's Topic: Escape Characters")
print("Let's start!")
# Output:
# Welcome to Python Learning!
# Today's Topic: Escape Characters
# Let's start!
# (Sab chipka hua lagta hai)


# With \n (More Readable):

print("\nWelcome to Python Learning!\n")
print("Today's Topic: Escape Characters\n")
print("Let's start!\n")
# Output:
#                               ← Khali line (space)
# Welcome to Python Learning!
#                               ← Khali line (space)
# Today's Topic: Escape Characters
#                               ← Khali line (space)
# Let's start!
#                               ← Khali line (space)
# (Proper spacing ke saath, padhne mein easy!)


# ------------------------ Common Mistakes ------------------------

# Mistake 1: /n likhna (Forward slash) — GALAT!

# print("Hello/nWorld")
# Output: Hello/nWorld
# /n escape sequence nahi hai! Backslash (\) chahiye.


# Mistake 2: \n ko string ke andar alag se likhna

# print("Hello", \n, "World")   ← GALAT!
# SyntaxError aayega.

# Sahi:
print("Hello\nWorld")


# Mistake 3: Raw String vs Escape Sequence

# Agar \n ko as a TEXT print karna hai (escape nahi):
print(r"Hello\nWorld")
# Output: Hello\nWorld
# r"" ka matlab: Raw String — escape sequences ignore!


# ------------------------ Best Practices ------------------------

# 1. Start mein \n — Space do program ke output ko
print("\n--- Program Start ---")

# 2. End mein \n — Agli line ready rakho
print("--- Program End ---\n")

# 3. \n\n — Sections ke beech gap do
print("Section 1 Complete!\n\nStarting Section 2...")

# 4. \t — Data format karo table jaisa
print("Name\t\tScore\nIbrahim\t\t95\nAli\t\t80")


# ------------------------ Summary ------------------------

# Escape Characters = \ se start hone wale special characters

# Important Escape Sequences:
#   → \n  = New Line (Enter press jaisa)
#   → \t  = Tab Space (4-8 spaces ka gap)
#   → \\  = Backslash (\) print karna
#   → \"  = Double Quote (") print karna
#   → \'  = Single Quote (') print karna

# \n — Sabse Zyada Use:
#   → \n at end = Agli line mein jao + khali line
#   → \n at start = Pehle nayi line
#   → \n\n = Do khali lines / Section gap
#   → \n in middle = Text ko break karo

# \t — Formatting ke Liye:
#   → Table jaisa data dikhana
#   → Bill / Receipt format karna

# Real Life Analogy:
#   → \n = WhatsApp mein Enter press karna
#   → \t = Keyboard ki TAB key press karna
#   → \" = Quote ke andar quote likhna

# Yaad Rakho:
#   → /n ❌ (Forward slash — Galat!)
#   → \n ✅ (Backslash — Sahi!)