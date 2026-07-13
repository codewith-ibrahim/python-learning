# Match-Case Statement in Python

# Match-Case kya hota hai?
#
# Match-Case Python 3.10 mein introduce hua tha.
# Ye ek PATTERN MATCHING tool hai.
# If-Else ka ZYADA POWERFUL aur CLEAN version!

# Real Life Analogy:
# Jaise aapke phone mein "Settings" menu hota hai:
#   WiFi     → WiFi settings kholo
#   Bluetooth → Bluetooth settings kholo
#   Display  → Display settings kholo
#   Default  → Kuch nahi

# Match-Case bilkul yahi karta hai!
# Value match karo → Matching case execute karo!


# ------------------------ Basic Syntax ------------------------

# Syntax:
# match variable:
#     case pattern1:
#         # Code
#     case pattern2:
#         # Code
#     case _:
#         # Default case (Agar koi match nahi hua)


# ------------------------ Simple Example ------------------------

user_input = int(input("Enter a number (1-5): "))

match user_input:
    case 1:
        print("Case is 1")

    case 2:
        print("Case is 2")

    case 3:
        print("Case is 3")

    case 4:
        print("Case is 4")

    case 5:
        print("Case is 5")

    case _:
        print("No match found!")

# Flow:
# 1. User ne number enter kiya (e.g., 3)
# 2. match user_input → 3 se compare karega
# 3. case 1: → 3 == 1? False → Skip
# 4. case 2: → 3 == 2? False → Skip
# 5. case 3: → 3 == 3? True → Execute!
# 6. Baaki cases SKIP!
# 7. Agar koi match nahi hota → case _: (Default)


# ------------------------ Match vs If-Else ------------------------

# If-Else Way (Purana):
if user_input == 1:
    print("Case is 1")
elif user_input == 2:
    print("Case is 2")
elif user_input == 3:
    print("Case is 3")
elif user_input == 4:
    print("Case is 4")
elif user_input == 5:
    print("Case is 5")
else:
    print("No match found!")

# Match-Case Way (Naya — Better!):
match user_input:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 4:
        print("Case is 4")
    case 5:
        print("Case is 5")
    case _:
        print("No match found!")

# Difference:
# If-Else: Baar baar variable == value likhna padta hai
# Match-Case: Direct value likho, Python automatically compare karega!


# ------------------------ case _ (Default Case) ------------------------

# underscore (_) ka matlab: DEFAULT case
# Agar upar ke kisi bhi case se match nahi hua, to ye chalega.

# Real Life:
# Remote ke buttons:
#   1 → Star Plus
#   2 → Sony
#   3 → Geo
#   _ → "Invalid Channel"

channel = int(input("Enter channel number: "))

match channel:
    case 1:
        print("📺 Ary")
    case 2:
        print("📺 Express News")
    case 3:
        print("📺 Geo News")
    case _:
        print("❌ Invalid Channel!")

# Agar user 1, 2, ya 3 enter kare to respective channel.
# Agar 99 enter kare to "Invalid Channel!"


# ------------------------ case _ Ki Position ------------------------

# ⚠️ IMPORTANT: case _ HAMESHA last mein aana chahiye!

# ❌ GALAT:
# match value:
#     case _:
#         print("Default")
#     case 1:
#         print("One")       # Kabhi execute nahi hoga!
# Kyunke _ sab kuch match kar leta hai!

# ✅ SAHI:
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Default")     # Sirf tab jab upar wale match na ho


# ------------------------ Multiple Values in One Case ------------------------

# Pipe (|) use karke ek case mein MULTIPLE values match kar sakte hain.

day = input("Enter day: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("📅 Weekday — Office/School jao!")
    case "saturday" | "sunday":
        print("🎉 Weekend — Enjoy karo!")
    case _:
        print("❌ Invalid day!")

# Yahan ek hi case mein 5 values match ho rahi hain!


# ------------------------ Match-Case with Data Types ------------------------

# Match-Case different data types ke saath bhi kaam karta hai.

# Example 1: Integer
number = 42
match number:
    case 0:
        print("Zero")
    case 42:
        print("Answer to everything! 🌌")
    case _:
        print("Some other number")


# Example 2: String
command = input("Enter command (start/stop/pause): ").lower()

match command:
    case "start":
        print("▶️ Starting...")
    case "stop":
        print("⏹️ Stopping...")
    case "pause":
        print("⏸️ Paused...")
    case _:
        print("❌ Unknown command!")


# Example 3: Boolean
is_logged_in = True

match is_logged_in:
    case True:
        print("✅ Welcome back!")
    case False:
        print("🔐 Please login first")


# ------------------------ Match-Case with Lists ------------------------

# Match-Case lists ke patterns bhi match kar sakta hai!

my_list = [1, 2, 3]

match my_list:
    case [1, 2, 3]:
        print("List exactly [1, 2, 3]")
    case [1, _, _]:
        print("List starts with 1, rest anything")
    case [_, _, _]:
        print("Any list with exactly 3 items")
    case _:
        print("Some other list")

# Underscore (_) ka matlab: "Kuch bhi ho sakta hai"


# ------------------------ Match-Case with Dictionaries ------------------------

# Match-Case dictionaries ke structure bhi match kar sakta hai!

person = {"name": "Ibrahim", "age": 22}

match person:
    case {"name": "Ibrahim", "age": 22}:
        print("Perfect match — Ibrahim, 22")
    case {"name": name, "age": age}:
        print(f"Person: {name}, Age: {age}")
    case _:
        print("Unknown structure")


# ------------------------ Match-Case with Guards (if conditions) ------------------------

# Case ke andar EXTRA CONDITION bhi laga sakte hain!

marks = int(input("Enter marks: "))

match marks:
    case m if m >= 90:
        print("Grade: A+ 🏆")
    case m if m >= 80:
        print("Grade: A ⭐")
    case m if m >= 70:
        print("Grade: B 👍")
    case m if m >= 60:
        print("Grade: C 📝")
    case m if m >= 50:
        print("Grade: D ⚠️")
    case _:
        print("Grade: F ❌")

# "case m if condition" → Guard pattern
# m variable mein marks ki value store hoti hai
# Phir if condition check hoti hai


# ------------------------ Real Life Scenario 1: Calculator ------------------------

print("\n🧮 SIMPLE CALCULATOR")
print("=" * 30)
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("=" * 30)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (1-4): ")

match operation:
    case "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "4":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("❌ Cannot divide by zero!")
    case _:
        print("❌ Invalid operation!")


# ------------------------ Real Life Scenario 2: Restaurant Menu ------------------------

print("\n🍽️ RESTAURANT MENU")
print("=" * 30)

choice = input("Kya khana pasand karein ge? (biryani/burger/pizza/drink): ").lower()

match choice:
    case "biryani":
        print("🍛 Chicken Biryani — Rs. 250")
        print("Thoda wait karna hoga — 20 minutes!")
    case "burger":
        print("🍔 Zinger Burger — Rs. 150")
        print("5 minutes mein ready!")
    case "pizza":
        print("🍕 Large Pizza — Rs. 500")
        print("15 minutes mein bake hoga!")
    case "drink":
        print("🥤 Cold Drink — Rs. 80")
        print("Turant mil jayegi!")
    case _:
        print("❌ Sorry! Ye item available nahi hai.")


# ------------------------ Real Life Scenario 3: Traffic Light ------------------------

print("\n🚦 TRAFFIC LIGHT SYSTEM")
print("=" * 30)

light = input("Enter traffic light color (red/yellow/green): ").lower()

match light:
    case "red":
        print("🔴 RUK JAAO!")
        print("Wait for green light...")
    case "yellow":
        print("🟡 TAIYAAR HO JAO!")
        print("Slow down, light red hone wali hai.")
    case "green":
        print("🟢 CHALTE JAAO!")
        print("Safe journey!")
    case _:
        print("⚠️ Invalid light color!")


# ------------------------ Real Life Scenario 4: User Role System ------------------------

print("\n👤 USER ROLE SYSTEM")
print("=" * 30)

username = input("Enter username: ")
role = input("Enter role (admin/editor/viewer): ").lower()

match role:
    case "admin":
        print(f"✅ Welcome Admin, {username}!")
        print("You can: Create, Read, Update, Delete")
    case "editor":
        print(f"✅ Welcome Editor, {username}!")
        print("You can: Read, Update")
    case "viewer":
        print(f"✅ Welcome Viewer, {username}!")
        print("You can: Read only")
    case _:
        print(f"❌ Unknown role for {username}!")
        print("Default: Read-only access granted.")


# ------------------------ Real Life Scenario 5: Month Seasons ------------------------

print("\n📅 MONTH SEASON CHECKER")
print("=" * 30)

month = input("Enter month name: ").lower()

match month:
    case "december" | "january" | "february":
        print("❄️ WINTER — Garam kapde pehno!")
        print("Temperature: 5-15°C")
    case "march" | "april":
        print("🌸 SPRING — Bahar niklo, weather acha hai!")
        print("Temperature: 15-25°C")
    case "may" | "june" | "july" | "august":
        print("☀️ SUMMER — AC chalao, pani piyo!")
        print("Temperature: 30-45°C")
    case "september" | "october":
        print("🍂 AUTUMN — Halki thand shuru!")
        print("Temperature: 20-30°C")
    case "november":
        print("🍂 LATE AUTUMN — Thand badh rahi hai!")
        print("Temperature: 10-20°C")
    case _:
        print("❌ Invalid month! Please check spelling.")


# ------------------------ Match-Case vs If-Else: When to Use? ------------------------

# ┌─────────────────────┬─────────────────────┬───────────────────────┐
# │ If-Else             │ Match-Case          │ Use Case              │
# ├─────────────────────┼─────────────────────┼───────────────────────┤
# │ Complex conditions  │ Exact value match   │ If-Else: Range check  │
# │ (>, <, !=, and)     │ Simple value match  │ Match: Fixed values   │
# │ Python 2+           │ Python 3.10+        │                       │
# │ More flexible       │ Cleaner for values  │                       │
# └─────────────────────┴─────────────────────┴───────────────────────┘

# Rule of Thumb:
# Agar EXACT VALUES compare kar rahe ho → Match-Case ✅
# Agar CONDITIONS check kar rahe ho (>, <, !=) → If-Else ✅


# ------------------------ Common Mistakes ------------------------

# Mistake 1: case _ ko beech mein rakhna

# ❌ GALAT:
# match value:
#     case _:
#         print("Default")
#     case 1:
#         print("One")    # Kabhi nahi chalega!


# Mistake 2: Colon (:) bhoolna

# ❌ GALAT:
# match value:
#     case 1              # Colon missing!
#         print("One")


# Mistake 3: Python version check karna bhoolna

# Match-Case sirf Python 3.10+ mein kaam karta hai!
# Purane versions mein SyntaxError aayega.


# Mistake 4: case mein assignment (=) use karna

# ❌ GALAT:
# case x = 5:    # Ye kaam nahi karega

# ✅ SAHI:
# case 5:
#     print("Five")


# ------------------------ Advanced: Variable Binding ------------------------

# Match-Case values ko VARIABLES mein capture bhi kar sakta hai!

point = (3, 5)

match point:
    case (0, 0):
        print("Origin point")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at x={x}, y={y}")
    case _:
        print("Not a valid point")

# Yahan x aur y variables mein values capture ho gayin!


# ------------------------ Summary ------------------------

# Match-Case = Pattern Matching (Python 3.10+)

# Syntax:
# match variable:
#     case pattern1:
#         # Code
#     case pattern2 | pattern3:    # Multiple values
#         # Code
#     case pattern if condition:   # Guard (Extra condition)
#         # Code
#     case _:
#         # Default case

# Match-Case vs If-Else:
#   → If-Else: Conditions check karne ke liye (>, <, !=)
#   → Match-Case: Exact values match karne ke liye

# case _ = Default case (Agar koi match nahi hua)
# case _ HAMESHA last mein aana chahiye!

# Features:
#   → Multiple values: case 1 | 2 | 3:
#   → Guards: case m if m > 50:
#   → Variable binding: case (x, y):
#   → Works with: int, str, bool, list, tuple, dict

# Real Life Use:
#   → Menu selection (Calculator, Restaurant)
#   → Traffic light system
#   → User role management
#   → Season/month checker

# Golden Rule:
# Exact values → Match-Case ✅
# Conditions → If-Else ✅