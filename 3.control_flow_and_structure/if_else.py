# If-Else Statements in Python

# If-Else kya hota hai?
#
# If-Else ek DECISION MAKING tool hai.
# Ye program ko batata hai ke:
# "Agar ye condition true hai to ye karo, warna ye karo."

# Real Life Example:
# Agar barish ho rahi hai → Chhatta le lo
# Warna → Bina chhatte ke jao


# ------------------------ Indentation Ka Faida ------------------------

# Python mein indentation ab kaam aayegi!
# If-Else blocks indentation se hi define hote hain.
# (Yaad hai indentation.py se? Same concept!)

# Indentation batata hai ke kaunsa code kis block ka hissa hai.


# ------------------------ Simple If Statement ------------------------

# Syntax:
# if (condition):
#     # Code jo tab chalega jab condition True ho

if (8 > 10):
    print("8 is greater than 10")

# Ye print KYUN NAHI hua?
# Kyunke condition FALSE thi!
# 8 > 10 = False
# Jab condition False hoti hai, to Python if block ke ANDAR nahi jata.
# Seedha skip kar deta hai!

# Real Life:
# Agar mere paas 100 rupay hain → Movie dekhne jaao
# Agar nahi hain → Kuch nahi (Skip!)

money = 50
if money >= 100:
    print("Movie dekhne jaao!")
# Output: Kuch nahi! (Kyunke money 100 se kam hai)


# ------------------------ Code Outside If Block ------------------------

# Jo code if block ke BAHR hai, wo HAMESHA chalega!

if (8 > 10):
    print("8 is greater than 10")    # ❌ Nahi chalega (False condition)

print("Out of if statement")          # ✅ Hamesha chalega!

# Yahan kya hua?
# if condition False thi → if block skip hua
# Lekin "Out of if statement" if block ke BAHR hai
# Isliye wo HAMESHA print hoga!

# Real Life:
# if (exam_pass_hua):
#     print("Party!")           ← Sirf pass hone par
# print("Ghar jaao")           ← Hamesha (Pass ho ya fail)


# ------------------------ If-Else Statement ------------------------

# Syntax:
# if (condition):
#     # Code jab condition True ho
# else:
#     # Code jab condition False ho

# ⚠️ IMPORTANT: Colon (:) lagana ZAROORI hai!
# Aur indentation sahi honi chahiye!

# ❌ Galat Syntax (Without Colon):
# if (10 > 20)
#     print("Yes")
# else
#     print("No")

# ✅ Sahi Syntax (With Colon):
if (10 > 20):
    print("Yes it is")
else:
    print("No it is not")

# Output: No it is not
# Kyunke 10 > 20 = False

# Real Life:
# Agar paas 100 rupay hain → Movie dekho
# Warna → Ghar par raho

money = 50
if money >= 100:
    print("Movie dekhne jaao! 🎬")
else:
    print("Ghar par raho! 🏠")
# Output: Ghar par raho! 🏠


# ------------------------ Real Life Scenario: Driving License ------------------------

# Scenario 1: Simple Age Check

age = int(input("Enter Your Age: "))

if (age >= 18):
    print("Congrats! Aap driving kar sakte hain. 🚗")
else:
    print("Sorry! Aap abhi chhote hain, driving nahi kar sakte. 👶")

# Yahan:
# age >= 18 → "Congrats! Aap driving kar sakte hain."
# age < 18  → "Sorry! Aap abhi chhote hain..."


# ------------------------ Scenario 2: Grade Calculator ------------------------

# Real Life: Exam ke marks ke hisaab se grade dena

marks = int(input("Enter Your Marks: "))

if marks >= 50:
    print("Pass! 🎉")
else:
    print("Fail! 📚 Mazeed mehnat karo.")


# ------------------------ Elif Statement ------------------------

# Elif = Else + If
# Jab MULTIPLE conditions check karni hon.

# Syntax:
# if (condition1):
#     # Code
# elif (condition2):
#     # Code
# elif (condition3):
#     # Code
# else:
#     # Code (Agar upar ki koi condition true nahi hui)


# ------------------------ Scenario 3: Age Categories ------------------------

age = int(input("Enter Your Age: "))

if (age >= 18):
    print("Congrats! Aap driving kar sakte hain. 🚗")
elif (age == 10):
    print("Aap abhi bachche hain, study karo jaa kar! 📚")
else:
    print("Sorry! Aap abhi chhote hain, driving nahi kar sakte. 👶")

print("Program End")  # Ye HAMESHA chalega (Bahir hai)

# Flow samjho:
# 1. Pehle if condition check hogi (age >= 18)
# 2. Agar True → if block chalega, BAAKI SAB SKIP!
# 3. Agar False → elif condition check hogi (age == 10)
# 4. Agar True → elif block chalega, BAAKI SAB SKIP!
# 5. Agar dono False → else block chalega
# 6. "Program End" hamesha chalega (Bahir hai)

# ⚠️ IMPORTANT:
# Jaise hi KOI EK condition True hoti hai,
# Uska block execute hota hai aur BAAKI SARI CONDITIONS SKIP ho jati hain!


# ------------------------ Scenario 4: Grade System ------------------------

# Real Life: Proper grading system

marks = int(input("Enter Your Marks (0-100): "))

if marks >= 90:
    print("Grade: A+ 🏆")
elif marks >= 80:
    print("Grade: A ⭐")
elif marks >= 70:
    print("Grade: B 👍")
elif marks >= 60:
    print("Grade: C 📝")
elif marks >= 50:
    print("Grade: D ⚠️")
else:
    print("Grade: F (Fail) ❌")

# Order IMPORTANT hai!
# Agar marks >= 90 top par na likho to kabhi A+ grade nahi milega!
# Kyunke pehle marks >= 80 true ho jayega!


# ------------------------ Scenario 5: Restaurant Ordering ------------------------

# Real Life: Restaurant menu system

print("=== Restaurant Menu ===")
print("1. Biryani     - Rs. 250")
print("2. Burger      - Rs. 150")
print("3. Pizza       - Rs. 500")
print("4. Cold Drink  - Rs. 80")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Aapne Biryani order ki! 🍛")
    print("Bill: Rs. 250")
elif choice == 2:
    print("Aapne Burger order kiya! 🍔")
    print("Bill: Rs. 150")
elif choice == 3:
    print("Aapne Pizza order kiya! 🍕")
    print("Bill: Rs. 500")
elif choice == 4:
    print("Aapne Cold Drink order ki! 🥤")
    print("Bill: Rs. 80")
else:
    print("Invalid choice! 1-4 ke beech mein choose karein. ❌")


# ------------------------ Scenario 6: Weather Advisory ------------------------

# Real Life: Weather ke hisaab se advice

temperature = int(input("Enter temperature in Celsius: "))

if temperature > 40:
    print("Bahut garmi hai! Ghar mein raho, AC chalao. 🥵")
elif temperature > 30:
    print("Garmi hai. Halka kapda pehno, pani zyada piyo. ☀️")
elif temperature > 20:
    print("Weather pleasant hai. Ghoomne jao! 🌤️")
elif temperature > 10:
    print("Thodi thand hai. Jacket pehn lo. 🧥")
else:
    print("Bahut thand hai! Heater chalao, garam kapde pehno. ❄️")


# ------------------------ Scenario 7: Login System ------------------------

# Real Life: Simple login check

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "12345":
    print("Login Successful! ✅")
    print("Welcome back, Admin!")
else:
    print("Login Failed! ❌")
    print("Wrong username or password.")


# ------------------------ Only If (Without Else) ------------------------

# Sirf if bhi chal sakta hai — else zaroori nahi!

if (2 < 10):
    print("Yes, 2 is less than 10")

# Output: Yes, 2 is less than 10

# Real Life:
# Agar barish ho rahi hai → Chhatta le lo
# (Agar nahi ho rahi to kuch mat karo)

is_raining = True
if is_raining:
    print("Chhatta le lo! ☔")


# ------------------------ Common Mistakes ------------------------

# Mistake 1: Elif se start karna (GALAT!)

# elif (10 > 5):
#     print("Yes")
# Output: SyntaxError
# Elif sirf if ke BAAD aata hai!


# Mistake 2: Colon (:) bhoolna

# if (5 > 3)
#     print("Yes")
# Output: SyntaxError


# Mistake 3: Indentation galat karna

# if (5 > 3):
# print("Yes")      ← Indentation nahi hai!
# Output: IndentationError


# Mistake 4: Assignment (=) vs Comparison (==)

# age = 18    ← Assignment (Value set karna)
# age == 18   ← Comparison (Check karna)

# if (age = 18):    ← GALAT! Ye assignment hai
# if (age == 18):   ← SAHI! Ye comparison hai


# ------------------------ Nested If-Else ------------------------

# If ke andar if!

age = int(input("Enter Your Age: "))

if age >= 18:
    print("Aap adult hain.")

    # Nested if (Andar ka if)
    if age >= 60:
        print("Aap senior citizen hain. 👴")
    else:
        print("Aap young adult hain. 🧑")
else:
    print("Aap minor hain.")

# Real Life: Shopping Discount
# Agar membership hai:
#     Agar 1 saal se zyada purani hai → 20% discount
#     Warna → 10% discount
# Warna → No discount


# ------------------------ Logical Operators ke saath ------------------------

# and, or, not ke saath if-else

age = 22
has_license = True

if age >= 18 and has_license:
    print("Aap driving kar sakte hain! 🚗")
else:
    print("Aap driving nahi kar sakte! ❌")

# Real Life: Job Application
experience = 3
has_degree = True

if experience >= 2 and has_degree:
    print("Aap job ke liye eligible hain! 💼")
elif experience >= 2 or has_degree:
    print("Aap partially eligible hain. Interview de sakte hain. 📋")
else:
    print("Sorry, aap eligible nahi hain. ❌")


# ------------------------ One-Liner If-Else (Ternary Operator) ------------------------

# Chhoti if-else ek line mein bhi likh sakte hain.

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# Syntax:
# value = true_value if condition else false_value


# ------------------------ Truthy and Falsy Values ------------------------

# Python mein kuch values automatically True/False treat hoti hain.

# Falsy Values (False jaisi):
# 0, "", [], {}, (), None, False

# Truthy Values (True jaisi):
# Baaki sab kuch!

if 0:
    print("Yes")     # Nahi chalega (0 Falsy hai)
if "Hello":
    print("Yes")     # Chalega (Non-empty string Truthy hai)
if []:
    print("Yes")     # Nahi chalega (Empty list Falsy hai)
if [1, 2]:
    print("Yes")     # Chalega (Non-empty list Truthy hai)


# ------------------------ Multiple Conditions in One Line ------------------------

# if statement mein multiple conditions ek saath.

age = 25
income = 50000

if age > 18 and age < 30 and income > 30000:
    print("Aap young professional hain! 🎯")


# ------------------------ Summary ------------------------

# If-Else = Decision Making Tool

# Syntax:
# if (condition):
#     # Code
# elif (condition):
#     # Code
# else:
#     # Code

# Rules:
# ✅ Colon (:) lagana zaroori hai
# ✅ Indentation sahi honi chahiye
# ✅ Elif sirf if ke baad aata hai
# ✅ Else optional hai
# ✅ Jaise hi koi condition True hoti hai, baaki skip!
# ✅ Comparison ke liye == use karo, = nahi!

# Real Life Applications:
# 🚗 Driving License Check
# 📊 Grade System
# 🍽️ Restaurant Ordering
# 🌤️ Weather Advisory
# 🔐 Login System
# 💼 Job Eligibility
# 🛒 Shopping Discount

# If-Else ke bina programming SOCH bhi nahi sakte!