# While Loop in Python

# While Loop kya hota hai?
#
# While Loop ek CONTROL FLOW STATEMENT hai
# jo kisi CONDITION ke TRUE hone tak
# code ke block ko BAR BAR execute karta hai.
#
# Simple Words Mein:
# "Jab tak condition true hai, tab tak loop chalao"
# "Condition false hote hi loop ruk jayega"

# Technical Definition:
# While Loop ek ITERATION STATEMENT hai jo
# specified BOOLEAN CONDITION ko evaluate karta hai.
# Jab tak condition True return karti hai,
# loop body execute hoti rehti hai. Jaise hi
# condition False hoti hai, loop terminate ho jata hai.

# Real Life Analogy:
# Socho aap bartan dho rahe hain:
#
# "Jab tak sink mein bartan hain, tab tak dhoo"
#
# while sink_mein_bartan_hain:
#     bartan_dhoo()
#
# Jaise hi sab bartan dhul gaye → Condition false → Ruk jao!


# ============================================================
# PART 1: WHILE LOOP — BASIC STRUCTURE
# ============================================================

# ------------------------ Syntax ------------------------

# Syntax:
# while (condition):
#     # Loop body (Indentation zaroori!)
#     # Update statement (Condition ko false banane ke liye)

# Parts of While Loop:
# 🔹 while       → Python keyword (Loop start)
# 🔹 condition   → Boolean expression (True/False)
# 🔹 :           → Colon (Block start)
# 🔹 Loop body   → Code jo baar baar chalega
# 🔹 Update      → Condition ko eventually false banana


# ------------------------ Aapka Code — Line by Line ------------------------

print("=" * 60)
print("📊 YOUR CODE — COMPLETE BREAKDOWN")
print("=" * 60)

# LINE 1: i = 1
# Ye INITIALIZATION STATEMENT hai
# Loop start hone se pehle variable ki value set karna
i = 1
print(f"🔹 Initialization: i = {i}")
print(f"   (Loop shuru hone se pehle variable ready kiya)\n")

# LINE 2: while(i < 10):
# Ye CONDITION STATEMENT hai (Entry Control)
# Har iteration se pehle check hota hai
# Agar True → Loop body execute
# Agar False → Loop skip, aage badho
print("🔹 Condition: while(i < 10):")
print("   (Har baar check hoga: kya i chhota hai 10 se?)\n")

# LINE 4: print(i)
# Ye LOOP BODY hai
# Jo kaam baar baar karna hai

# LINE 5: i += 1
# Ye UPDATING STATEMENT hai
# Har iteration mein i ki value badhao
# Iske bina INFINITE LOOP ho jayega!
print("🔹 Update: i += 1")
print("   (Har baar i ki value 1 se badhao)")
print("   (Iske bina loop kabhi rukega nahi!)\n")


# ------------------------ Complete Execution Flow ------------------------

print("=" * 60)
print("📊 STEP-BY-STEP EXECUTION")
print("=" * 60)

i = 1  # Initialization

print("\nLoop Start:")
print("-" * 40)

while i < 10:  # Condition check
    print(f"   Iteration: i = {i} | Condition: {i} < 10 = {i < 10}")
    print(f"   → print({i})")
    i += 1  # Update
    print(f"   → i becomes {i}\n")

print(f"   Loop END: i = {i} | Condition: {i} < 10 = {i < 10}")
print("   (Condition False → Loop terminates)\n")

print("While loop has finished executing...")


# ------------------------ Execution Table ------------------------

print("\n" + "=" * 60)
print("📊 EXECUTION TABLE")
print("=" * 60)

print("""
┌──────────────┬───────────────┬────────────┬──────────────┐
│ Iteration    │ i (Before)    │ i < 10 ?   │ i (After)    │
├──────────────┼───────────────┼────────────┼──────────────┤
│ 1st          │ 1             │ TRUE ✅    │ 2            │
│ 2nd          │ 2             │ TRUE ✅    │ 3            │
│ 3rd          │ 3             │ TRUE ✅    │ 4            │
│ 4th          │ 4             │ TRUE ✅    │ 5            │
│ 5th          │ 5             │ TRUE ✅    │ 6            │
│ 6th          │ 6             │ TRUE ✅    │ 7            │
│ 7th          │ 7             │ TRUE ✅    │ 8            │
│ 8th          │ 8             │ TRUE ✅    │ 9            │
│ 9th          │ 9             │ TRUE ✅    │ 10           │
│ 10th (Check) │ 10            │ FALSE ❌   │ LOOP ENDS    │
└──────────────┴───────────────┴────────────┴──────────────┘

Total Iterations: 9
Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
""")

# ⚠️ IMPORTANT:
# Loop 9 baar chala, 10 baar nahi!
# Kyun?
# Jab i = 10 hua, condition 10 < 10 = FALSE
# Isliye 10 print nahi hua!


# ============================================================
# PART 2: PARTS OF WHILE LOOP — DETAILED
# ============================================================

print("=" * 60)
print("📊 3 PARTS OF WHILE LOOP")
print("=" * 60)

print("""
Every While Loop has 3 ESSENTIAL parts:

1️⃣  INITIALIZATION (Shuru karne se pehle)
    • Variable declare karo
    • Starting value set karo
    • Loop ke BAHR likhte hain
    
    Example: i = 1
             count = 0
             running = True


2️⃣  CONDITION (Har baar check)
    • Boolean expression
    • True → Loop chalao
    • False → Loop se bahar jao
    • Har iteration se PEHLE check hota hai
    • ENTRY CONTROLLED LOOP kehlata hai
    
    Example: while i < 10:
             while count <= 5:
             while running:


3️⃣  UPDATE (Condition ko false banana)
    • Variable ki value change karo
    • Loop body ke ANDAR likhte hain
    • Iske bina INFINITE LOOP!
    • Eventually condition false honi chahiye
    
    Example: i += 1
             count -= 1
             running = False
""")


# ============================================================
# PART 3: INFINITE WHILE LOOP
# ============================================================

print("=" * 60)
print("📊 INFINITE WHILE LOOP")
print("=" * 60)

print("""
❌ INFINITE LOOP KYA HOTA HAI?

Wo loop jiski condition KABHI FALSE NAHI hoti.
Loop chalta hi rehta hai, rukta nahi!

Example (DANGEROUS — Run mat karna!):
─────────────────────────────────────
i = 1
while i > 0:        # i hamesha 0 se bada rahega
    print(i)        # Kabhi rukega nahi!
    i += 1          # i badhta rahega, condition hamesha true
─────────────────────────────────────


i = 1
while True:         # True hamesha TRUE hota hai
    print(i)        # Kabhi rukega nahi!
    i += 1
─────────────────────────────────────

# Commented out for safety:
# while(True):
#     print("While loop is running...")


How to Stop Infinite Loop?
→ Keyboard: Ctrl + C (Terminal/VS Code)
→ Force close program
→ BREAK statement (Explained below)
""")


# ============================================================
# PART 4: BREAK STATEMENT
# ============================================================

print("=" * 60)
print("📊 BREAK STATEMENT")
print("=" * 60)

# break kya karta hai?
#
# break loop ko IMMEDIATELY terminate kar deta hai.
# Condition false hone ka wait nahi karta.
# Jahan break likho, loop wahi ruk jayega.

# Aapka Code with break:

print("\n🔍 Your Code with break:")
print("-" * 40)

print("""
while(True):                    ← Infinite loop (True hamesha true)
    num = int(input("Enter a number: "))
    print(num)
    
    if(num == 0):              ← Condition check
        break                  ← Agar num 0 hai to loop TOD DO!
        
print("Loop is finished")       ← Break ke baad yahan aayega
""")

print("\n🎮 Demonstration (Input 0 to stop):")
print("-" * 40)

while True:
    num = int(input("Enter a number: "))
    print(f"   You entered: {num}")
    
    if num == 0:
        print("   → Zero detected! Breaking loop...")
        break

print("\n✅ Loop is finished!")
print("   (Break statement ki wajah se loop ruk gaya)")


# ------------------------ break vs condition ------------------------

print("\n" + "=" * 60)
print("📊 BREAK vs NORMAL EXIT")
print("=" * 60)

print("""
┌────────────────────┬─────────────────────────┬──────────────────────┐
│ Feature            │ Normal Exit             │ Break Exit           │
├────────────────────┼─────────────────────────┼──────────────────────┤
│ Kab rukta hai?     │ Condition False hone par│ Jahan break likho    │
│ Kitni baar check?  │ Har iteration se pehle  │ Kabhi bhi           │
│ Use case           │ Fixed iterations        │ Special condition   │
│ Example            │ while i < 10:           │ if x == 0: break    │
└────────────────────┴─────────────────────────┴──────────────────────┘

Normal Exit Flow:
while condition:     ← Har baar check
    # code
    # update
# condition false → Loop end

Break Exit Flow:
while True:          ← Hamesha true
    # code
    if something:
        break        ← YAHIN RUK JAO!
# break ke baad yahan
""")


# ============================================================
# PART 5: WHILE LOOP — PRACTICAL EXAMPLES
# ============================================================

print("=" * 60)
print("📊 PRACTICAL EXAMPLES")
print("=" * 60)


# Example 1: Countdown Timer
print("\n1️⃣  COUNTDOWN TIMER:")
count = 5
while count > 0:
    print(f"   ⏰ {count}...")
    count -= 1
print("   🚀 Liftoff!")


# Example 2: Sum of Numbers (1 to n)
print("\n2️⃣  SUM CALCULATOR:")
n = 5
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(f"   Sum of 1 to {n} = {total}")


# Example 3: Factorial Calculator
print("\n3️⃣  FACTORIAL CALCULATOR:")
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"   {num}! = {factorial}")


# Example 4: Reverse a Number
print("\n4️⃣  REVERSE A NUMBER:")
number = 12345
reverse = 0
temp = number

while temp > 0:
    last_digit = temp % 10
    reverse = (reverse * 10) + last_digit
    temp //= 10

print(f"   Original: {number}")
print(f"   Reversed: {reverse}")


# Example 5: Password Check (3 Attempts)
print("\n5️⃣  PASSWORD CHECK:")
correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input(f"   Enter password ({attempts} attempts left): ")
    
    if password == correct_password:
        print("   ✅ Access Granted!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"   ❌ Wrong password! Try again.")
        else:
            print("   🔒 Account Locked! No more attempts.")


# Example 6: Menu Driven Program
print("\n6️⃣  MENU DRIVEN PROGRAM:")
while True:
    print("\n   📋 MENU:")
    print("   1. Say Hello")
    print("   2. Show Time")
    print("   3. Exit")
    
    choice = input("   Enter choice (1-3): ")
    
    if choice == "1":
        print("   👋 Hello! Welcome!")
    elif choice == "2":
        from datetime import datetime
        print(f"   🕐 {datetime.now().strftime('%H:%M:%S')}")
    elif choice == "3":
        print("   👋 Goodbye!")
        break
    else:
        print("   ❌ Invalid choice!")


# ============================================================
# PART 6: FOR LOOP vs WHILE LOOP
# ============================================================

print("\n" + "=" * 60)
print("📊 FOR LOOP vs WHILE LOOP — FULL COMPARISON")
print("=" * 60)

print("""
┌────────────────────┬──────────────────────┬──────────────────────┐
│ Feature            │ For Loop             │ While Loop           │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Use When           │ Iterations KNOWN     │ Iterations UNKNOWN   │
│ Condition          │ Automatic            │ Manual (explicit)    │
│ Variable Update    │ Automatic            │ Manual               │
│ Best For           │ Lists, range, etc.   │ User input, waiting  │
│ Infinite Loop Risk │ Very Low             │ High                 │
│ Syntax             │ for x in y:          │ while condition:     │
│ Initialization     │ Built-in             │ Manual               │
│ Readability        │ Cleaner for fixed    │ Better for dynamic   │
└────────────────────┴──────────────────────┴──────────────────────┘

FOR LOOP — Best Use Cases:
✅ Fixed number of iterations
✅ List/Tuple/String processing
✅ range() ke saath
✅ Sab items process karna
✅ "Har student ke liye" type problems

WHILE LOOP — Best Use Cases:
✅ Unknown number of iterations
✅ User input (jab tak quit na kare)
✅ Game loops (jab tak game over na ho)
✅ Waiting for events
✅ "Jab tak user sahi input na de" type problems
""")


# ============================================================
# PART 7: CONTINUE STATEMENT
# ============================================================

print("=" * 60)
print("📊 CONTINUE STATEMENT")
print("=" * 60)

# continue kya karta hai?
# Current iteration SKIP karo, next iteration JAAO
# break ki tarah loop end nahi karta, sirf current skip

print("\nExample: Print odd numbers only (1-10):")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:    # Even number mila
        continue      # Skip karo, agla number lo
    print(f"   {i} (Odd)")
# Output: 1, 3, 5, 7, 9

print("\nbreak vs continue:")
print("""
   break    → "Loop SE BAHAR JAAO" (Terminate)
   continue → "YE ITERATION SKIP KARO" (Next iteration)

   while condition:
       if x == 0:
           break      ← Loop end
       if x == 5:
           continue   ← Is iteration ko skip, agla lo
       print(x)
""")


# ============================================================
# PART 8: WHILE-ELSE
# ============================================================

print("=" * 60)
print("📊 WHILE-ELSE (Unique Python Feature)")
print("=" * 60)

# while-else:
# else block tab chalta hai jab loop NORMALLY terminate ho
# Agar break se exit hua to else NAHI chalega!

print("\nExample 1: Normal Exit (Else chalega):")
i = 1
while i <= 3:
    print(f"   i = {i}")
    i += 1
else:
    print("   ✅ Loop completed normally! (Else executed)")

print("\nExample 2: Break Exit (Else NAHI chalega):")
i = 1
while i <= 5:
    print(f"   i = {i}")
    if i == 3:
        print("   → Breaking at 3!")
        break
    i += 1
else:
    print("   ❌ This will NOT execute (break se exit hua)")

print("   (Else block skip ho gaya kyunke break hua tha)")


# ============================================================
# PART 9: COMMON MISTAKES
# ============================================================

print("\n" + "=" * 60)
print("📊 COMMON MISTAKES & SOLUTIONS")
print("=" * 60)

print("""
❌ MISTAKE 1: Update statement bhoolna (Infinite Loop!)
   i = 1
   while i < 10:
       print(i)        # i kabhi badhega nahi!
   # Loop FOREVER!
   
✅ SOLUTION: Update statement lagao
   i = 1
   while i < 10:
       print(i)
       i += 1          # Update!


❌ MISTAKE 2: Colon (:) bhoolna
   while i < 10        # SyntaxError!
       print(i)
       
✅ SOLUTION:
   while i < 10:       # Colon lagao
       print(i)


❌ MISTAKE 3: Indentation galat
   while i < 10:
   print(i)             # IndentationError!
   
✅ SOLUTION:
   while i < 10:
       print(i)         # 4 spaces


❌ MISTAKE 4: Condition kabhi false nahi hogi
   i = 10
   while i > 0:
       print(i)
       i += 1           # i badh raha hai, 0 se aur door!
   # Infinite loop!
   
✅ SOLUTION: Condition false hone ka rasta do
   i = 10
   while i > 0:
       print(i)
       i -= 1           # Ghat raha hai, eventually 0


❌ MISTAKE 5: = vs ==
   i = 1
   while i = 5:         # Assignment! SyntaxError!
       print(i)
       
✅ SOLUTION:
   while i == 5:        # Comparison!
       print(i)
""")


# ============================================================
# PART 10: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — WHILE LOOP")
print("=" * 60)

print("""
✅ DEFINITION:
   While Loop ek CONTROL FLOW STATEMENT hai jo kisi
   CONDITION ke TRUE hone tak code block ko BAR BAR
   execute karta hai. Jaise hi condition FALSE hoti hai,
   loop TERMINATE ho jata hai.

✅ SYNTAX:
   while (condition):
       # loop body
       # update statement

✅ 3 ESSENTIAL PARTS:
   1. Initialization  (Loop se pehle, variable ready)
   2. Condition       (Har baar check, True/False)
   3. Update          (Variable change, eventually false)

✅ YOUR CODE EXPLAINED:
   • i = 1                  → Initialization
   • while(i < 10):         → Condition (Entry Control)
   • print(i)               → Loop Body
   • i += 1                 → Update Statement
   • Loop 9 baar chala (i=1 se i=9 tak)

✅ INFINITE LOOP:
   • Condition kabhi false nahi hoti
   • Ctrl+C se stop karo
   • while True: → Hamesha chalta hai

✅ BREAK STATEMENT:
   • Loop IMMEDIATELY terminate karta hai
   • Jahan break likho, wahi ruk jayega
   • while True + break = Controlled infinite loop

✅ CONTINUE STATEMENT:
   • Current iteration SKIP
   • Agli iteration continue
   • Loop end nahi karta

✅ WHILE-ELSE:
   • else tab chalta hai jab NORMAL exit ho
   • break se exit → else SKIP

✅ FOR vs WHILE:
   • For  → Fixed iterations (Known count)
   • While → Unknown iterations (Dynamic condition)

✅ GOLDEN RULES:
   • Colon (:) mat bhoolna
   • Update statement zaroor lagao
   • Indentation (4 spaces) sahi rakho
   • Condition eventually false honi chahiye
   • while True ke saath break use karo
""")