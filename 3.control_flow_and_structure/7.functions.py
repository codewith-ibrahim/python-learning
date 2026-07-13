# Functions in Python

# Function kya hota hai?
#
# Function ek REUSABLE code block hai jo kisi SPECIFIC
# task ko perform karta hai. Ek baar function define karo,
# phir jitni baar chahe use karo — dubara code likhne
# ki zaroorat nahi!
#
# Technical Definition:
# Function ek NAMED BLOCK of code hai jo ek specific
# task perform karta hai. Ye INPUT (parameters/arguments)
# leta hai, PROCESSING karta hai, aur OUTPUT return
# kar sakta hai. Functions code REUSABILITY aur
# MODULARITY provide karte hain.

# Real Life Analogy:
# Socho aapke ghar mein ek JUICE MACHINE hai:
#
# Input:  Fruits (Aam, Santra, etc.)
# Process: Machine juice banati hai
# Output: Fresh Juice
#
# Function bilkul juice machine jaisa hai!
# Aap input do, function kaam kare, output de.


# ============================================================
# PART 1: WHY FUNCTIONS?
# ============================================================

print("=" * 60)
print("📊 WHY DO WE NEED FUNCTIONS?")
print("=" * 60)

print("""
❌ WITHOUT FUNCTIONS (Code Repeat Hota Hai):
─────────────────────────────────────────────
# Student 1 ka greeting
print("Hello Ibrahim!")
print("Welcome to Python Class!")

# Student 2 ka greeting
print("Hello Ali!")
print("Welcome to Python Class!")

# Student 3 ka greeting
print("Hello Sara!")
print("Welcome to Python Class!")
# Har baar same code likhna pad raha hai!


✅ WITH FUNCTIONS (Code Reuse Hota Hai):
─────────────────────────────────────────
def greet_student(name):
    print(f"Hello {name}!")
    print("Welcome to Python Class!")

# Ab jitni baar chahe call karo:
greet_student("Ibrahim")
greet_student("Ali")
greet_student("Sara")
# Same kaam, ek line mein!


BENEFITS OF FUNCTIONS:
✅ Code Reusability     — Ek baar likho, baar baar use karo
✅ Modularity          — Code chhote parts mein divide hota hai
✅ Readability         — Code samajhna easy
✅ Maintainability     — Changes ek jagah karo
✅ Testing             — Alag-alag test kar sakte hain
✅ Avoid Repetition    — DRY Principle (Don't Repeat Yourself)
""")


# ============================================================
# PART 2: WHAT IS def? — COMPLETE EXPLANATION
# ============================================================

print("=" * 60)
print("📊 WHAT IS def?")
print("=" * 60)

print("""
def Python ka KEYWORD hai jo FUNCTION DEFINE karne
ke liye use hota hai.

def = "define" ka short form

Jab Python def dekhta hai, to use pata chal jata hai
ke ab ek naya function define ho raha hai.


FUNCTION DEFINITION ke Parts:
┌─────────────────────────────────────────────────────┐
│ def function_name(parameters):                      │
│     \"\"\"Docstring (Optional) — Function ki documentation\"\"\"│
│     # Function body (Code)                          │
│     return value  (Optional)                        │
└─────────────────────────────────────────────────────┘

🔹 def        → Keyword (Function define kar rahe hain)
🔹 Name       → Function ka naam (Meaningful hona chahiye)
🔹 Parameters → Input values (Optional, parentheses mein)
🔹 Colon (:)  → Function body start (Zaroori!)
🔹 Docstring  → Documentation string (Optional, best practice)
🔹 Body       → Actual code jo execute hoga
🔹 return     → Output value (Optional, nahi likhoge to None)
""")


# ============================================================
# PART 3: YOUR CODE — LINE BY LINE BREAKDOWN
# ============================================================

print("=" * 60)
print("📊 YOUR CODE — COMPLETE BREAKDOWN")
print("=" * 60)


# Example 1: Simple Function (No Parameters)
print("\n🔍 EXAMPLE 1: Simple Function")
print("-" * 40)

# LINE BY LINE EXPLANATION:

# Line 1: def greeting():
#   • def → Function define kar rahe hain
#   • greeting → Function ka naam
#   • () → Koi parameters nahi (Koi input nahi lega)
#   • : → Function body start

# Line 2:     print("Hello!")
#   • Function body (4 spaces indentation)
#   • Ye code execute hoga jab function call hoga

print("Step 1: Function define kiya")
def greeting():
    print("Hello!")

print("Step 2: Abhi tak kuch print nahi hua!")
print("         (Function define hone se execute nahi hota)")

print("\nStep 3: Function CALL kar rahe hain...")
greeting()  # ← YAHAN function execute hoga!

print("Step 4: Function execute ho gaya, aage badhe...")
print("Function executing completed")


# KEY POINT:
# Function DEFINE hone se EXECUTE nahi hota!
# Function CALL karne par EXECUTE hota hai!
# greeting() → Ye function CALL hai


# Example 2: Function with Parameters (Aapka Code)
print("\n\n🔍 EXAMPLE 2: Function with Parameters")
print("-" * 40)

print("Step 1: Function define with parameters")
def greeting(name, ending):
    print("Hello " + name)
    print(ending)

print("Step 2: Function call with ARGUMENTS")
print("         Arguments pass ho rahe hain: 'Ibrahim', 'Thank You!'\n")

greeting("Ibrahim", "Thank You!")

print("\nFunction executing completed")

# Kya hua?
# 1. greeting() function call hua
# 2. "Ibrahim" → name parameter mein gaya
# 3. "Thank You!" → ending parameter mein gaya
# 4. print("Hello " + name) → print("Hello " + "Ibrahim") → "Hello Ibrahim"
# 5. print(ending) → print("Thank You!")
# 6. Function end


# Example 3: Aapka Template (Leave Generator)
print("\n\n🔍 EXAMPLE 3: Leave Generator")
print("-" * 40)

def leaveGenerator(name, date):
    msg = f"Assalam u alaikum Sir,\n This is {name} and i will not come to the office on {date} \n Thanks!"
    print(msg)

print("Generating leave applications...\n")

# Call 1
print("─" * 40)
leaveGenerator("Ibrahim", "15th July")

# Call 2
print("─" * 40)
leaveGenerator("Ali", "18th July")

# Call 3
print("─" * 40)
leaveGenerator("Huzaifa", "20th July")

# Kitna easy! Ek function, teen alag-alag logon ke liye use hua!


# ============================================================
# PART 4: PARAMETERS vs ARGUMENTS — IMPORTANT DIFFERENCE!
# ============================================================

print("\n" + "=" * 60)
print("📊 PARAMETERS vs ARGUMENTS")
print("=" * 60)

print("""
⚠️  BOHOT IMPORTANT DIFFERENCE — EXAM MEIN POOCHTE HAIN!

PARAMETER:
→ Function DEFINITION mein jo variables likhte hain
→ Ye PLACEHOLDER hote hain
→ Function define karte waqt parentheses () mein

Example:
def greeting(name, ending):    ← name aur ending PARAMETERS hain
    print("Hello " + name)


ARGUMENT:
→ Function CALL karte waqt jo ACTUAL VALUES pass karte hain
→ Ye REAL VALUES hote hain
→ Function call karte waqt parentheses () mein

Example:
greeting("Ibrahim", "Thank You!")  ← "Ibrahim" aur "Thank You!" ARGUMENTS hain


VISUAL DIFFERENCE:
┌─────────────────────────────────────────────────────┐
│ def greeting(name, ending):    ← PARAMETERS         │
│     print("Hello " + name)                          │
│     print(ending)                                   │
│                                                     │
│ greeting("Ibrahim", "Thank You!")  ← ARGUMENTS      │
└─────────────────────────────────────────────────────┘

Simple Yaad Rakho:
Parameter = Function DEFINITION mein (Variable)
Argument  = Function CALL mein (Actual Value)
""")


# ============================================================
# PART 5: TYPES OF FUNCTIONS
# ============================================================

print("=" * 60)
print("📊 TYPES OF FUNCTIONS IN PYTHON")
print("=" * 60)

print("""
Python mein functions do types ke hote hain:

1️⃣  BUILT-IN FUNCTIONS (Python ke saath aate hain)
    • Python already provide karta hai
    • Install karte hi available
    • Examples: print(), input(), len(), type(), range(), etc.

2️⃣  USER-DEFINED FUNCTIONS (Hum khud banate hain)
    • def keyword se define karte hain
    • Apni zaroorat ke mutabiq
    • Examples: greeting(), leaveGenerator(), etc.
""")


# ============================================================
# PART 6: BUILT-IN FUNCTIONS — COMPLETE GUIDE
# ============================================================

print("=" * 60)
print("📊 BUILT-IN FUNCTIONS — COMPLETE EXPLANATION")
print("=" * 60)

print("""
Built-in Functions wo hain jo Python mein PEHLE SE
mojood hain. Inhe import nahi karna padta, direct use
kar sakte hain.

Python 3 mein 68 Built-in Functions hain.
Yahan sabse ZAROORI functions samjhte hain:
""")


# Category 1: Input/Output Functions
print("━" * 50)
print("📌 1. INPUT/OUTPUT FUNCTIONS")
print("━" * 50)

# print() — Output dikhana
print("\n🔹 print() — Screen par output dikhana:")
print("   print('Hello') → Hello")
print("   print(1, 2, 3) → 1 2 3")

# input() — User se input lena
print("\n🔹 input() — User se data lena (Hamesha String return karta hai):")
name = input("   Enter your name: ")
print(f"   Hello, {name}!")
print(f"   Type: {type(name)}  (Hamesha str!)")


# Category 2: Type Functions
print("\n\n" + "━" * 50)
print("📌 2. TYPE FUNCTIONS")
print("━" * 50)

print("\n🔹 type() — Variable ka data type batana:")
print(f"   type(5) = {type(5)}")
print(f"   type('Hello') = {type('Hello')}")
print(f"   type(3.14) = {type(3.14)}")
print(f"   type(True) = {type(True)}")
print(f"   type([1,2,3]) = {type([1, 2, 3])}")
print(f"   type(None) = {type(None)}")

print("\n🔹 isinstance() — Check karna ke kisi specific type ka hai ya nahi:")
print(f"   isinstance(5, int) = {isinstance(5, int)}")
print(f"   isinstance('Hello', str) = {isinstance('Hello', str)}")
print(f"   isinstance(5, str) = {isinstance(5, str)}")


# Category 3: Numeric Functions
print("\n\n" + "━" * 50)
print("📌 3. NUMERIC FUNCTIONS")
print("━" * 50)

print("\n🔹 abs() — Absolute value (Negative ko positive):")
print(f"   abs(-10) = {abs(-10)}")
print(f"   abs(5) = {abs(5)}")
print(f"   abs(-3.14) = {abs(-3.14)}")

print("\n🔹 round() — Number ko round karna:")
print(f"   round(3.14159, 2) = {round(3.14159, 2)}")
print(f"   round(3.14159) = {round(3.14159)}")
print(f"   round(3.5) = {round(3.5)}")

print("\n🔹 pow() — Power calculate karna:")
print(f"   pow(2, 3) = {pow(2, 3)}     (2³ = 2×2×2)")
print(f"   pow(5, 2) = {pow(5, 2)}     (5² = 25)")

print("\n🔹 min() & max() — Sabse chhota aur sabse bada:")
numbers = [5, 2, 9, 1, 7]
print(f"   List: {numbers}")
print(f"   min() = {min(numbers)}")
print(f"   max() = {max(numbers)}")

print("\n🔹 sum() — Saare numbers ka total:")
print(f"   sum({numbers}) = {sum(numbers)}")

print("\n🔹 divmod() — Division aur remainder ek saath:")
quotient, remainder = divmod(17, 5)
print(f"   divmod(17, 5) = ({quotient}, {remainder})")
print(f"   (17 ÷ 5 = {quotient} remainder {remainder})")


# Category 4: Sequence/Collection Functions
print("\n\n" + "━" * 50)
print("📌 4. COLLECTION FUNCTIONS")
print("━" * 50)

print("\n🔹 len() — Length batana:")
my_list = [10, 20, 30, 40, 50]
my_string = "Python"
print(f"   len({my_list}) = {len(my_list)}")
print(f"   len('{my_string}') = {len(my_string)}")

print("\n🔹 range() — Numbers ki sequence generate karna:")
print(f"   list(range(5)) = {list(range(5))}")
print(f"   list(range(2, 8)) = {list(range(2, 8))}")
print(f"   list(range(1, 10, 2)) = {list(range(1, 10, 2))}")

print("\n🔹 enumerate() — Index ke saath items:")
fruits = ["Apple", "Banana", "Mango"]
print(f"   Fruits: {fruits}")
for index, fruit in enumerate(fruits, start=1):
    print(f"      {index}. {fruit}")

print("\n🔹 zip() — Do lists ko pair karna:")
names = ["Ibrahim", "Ali", "Sara"]
ages = [22, 21, 23]
print(f"   Names: {names}")
print(f"   Ages:  {ages}")
print("   Zipped:", list(zip(names, ages)))

print("\n🔹 sorted() — Sort karna (Nayi list return):")
unsorted = [3, 1, 4, 1, 5, 9, 2]
print(f"   Original: {unsorted}")
print(f"   Sorted:   {sorted(unsorted)}")
print(f"   Reverse:  {sorted(unsorted, reverse=True)}")

print("\n🔹 reversed() — Reverse karna:")
print(f"   Original: {unsorted}")
print(f"   Reversed: {list(reversed(unsorted))}")

print("\n🔹 filter() — Condition ke hisaab se filter:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"   Numbers: {numbers}")
print(f"   Even only: {evens}")

print("\n🔹 map() — Har item par function apply:")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"   Numbers: {numbers}")
print(f"   Squared: {squared}")

print("\n🔹 any() & all() — Boolean checks:")
print(f"   any([False, False, True]) = {any([False, False, True])}")
print(f"   all([True, True, True]) = {all([True, True, True])}")
print(f"   all([True, False, True]) = {all([True, False, True])}")


# Category 5: Type Conversion Functions
print("\n\n" + "━" * 50)
print("📌 5. TYPE CONVERSION FUNCTIONS")
print("━" * 50)

print("\n🔹 int() — Integer mein convert:")
print(f"   int('42') = {int('42')}")
print(f"   int(3.14) = {int(3.14)}")
print(f"   int(True) = {int(True)}")

print("\n🔹 float() — Float mein convert:")
print(f"   float('3.14') = {float('3.14')}")
print(f"   float(5) = {float(5)}")

print("\n🔹 str() — String mein convert:")
print(f"   str(100) = '{str(100)}'")
print(f"   str(3.14) = '{str(3.14)}'")
print(f"   str(True) = '{str(True)}'")

print("\n🔹 bool() — Boolean mein convert:")
print(f"   bool(1) = {bool(1)}")
print(f"   bool(0) = {bool(0)}")
print(f"   bool('') = {bool('')}")
print(f"   bool('Hello') = {bool('Hello')}")

print("\n🔹 list() — List mein convert:")
print(f"   list('Hello') = {list('Hello')}")
print(f"   list(range(5)) = {list(range(5))}")

print("\n🔹 tuple() — Tuple mein convert:")
print(f"   tuple([1, 2, 3]) = {tuple([1, 2, 3])}")

print("\n🔹 set() — Set mein convert (Duplicates remove):")
print(f"   set([1, 2, 2, 3, 3, 3]) = {set([1, 2, 2, 3, 3, 3])}")

print("\n🔹 dict() — Dictionary mein convert:")
print(f"   dict(name='Ibrahim', age=22) = {dict(name='Ibrahim', age=22)}")


# Category 6: Object/Help Functions
print("\n\n" + "━" * 50)
print("📌 6. HELP & INFORMATION FUNCTIONS")
print("━" * 50)

print("\n🔹 help() — Kisi bhi function ki documentation dekho:")
print("   help(print)  # print() ki poori documentation!")
# help(print)  # Uncomment to see full documentation

print("\n🔹 dir() — Kisi object ke saare methods/attributes dekho:")
print("   dir(str)  # String ke saare methods!")
# print(dir(str))  # Uncomment to see all string methods

print("\n🔹 id() — Object ka memory address:")
x = 42
print(f"   id(42) = {id(x)}")

print("\n🔹 hash() — Object ka hash value (Dictionary keys ke liye):")
print(f"   hash('Python') = {hash('Python')}")
print(f"   hash(42) = {hash(42)}")


# Category 7: String Related Functions
print("\n\n" + "━" * 50)
print("📌 7. STRING FUNCTIONS (Built-in)")
print("━" * 50)

print("\n🔹 ord() — Character ka Unicode/ASCII code:")
print(f"   ord('A') = {ord('A')}")
print(f"   ord('a') = {ord('a')}")
print(f"   ord('0') = {ord('0')}")

print("\n🔹 chr() — Unicode code se character:")
print(f"   chr(65) = '{chr(65)}'")
print(f"   chr(97) = '{chr(97)}'")

print("\n🔹 format() — String formatting (Purana tareeqa):")
print(f"   format(255, 'b') = '{format(255, 'b')}'  (Binary)")
print(f"   format(255, 'x') = '{format(255, 'x')}'  (Hex)")

print("\n🔹 repr() — Object ki official string representation:")
print(f"   repr('Hello\\nWorld') = {repr('Hello\\nWorld')}")


# ============================================================
# PART 7: COMPLETE BUILT-IN FUNCTIONS LIST
# ============================================================

print("\n\n" + "=" * 60)
print("📊 ALL 68 BUILT-IN FUNCTIONS (Quick Reference)")
print("=" * 60)

print("""
┌─────────────────────────────────────────────────────────────┐
│ CATEGORY               │ FUNCTIONS                          │
├────────────────────────┼────────────────────────────────────┤
│ Input/Output           │ print(), input(), open()           │
│ Type Checking          │ type(), isinstance(), issubclass() │
│ Numeric                │ abs(), round(), pow(), sum()       │
│                        │ min(), max(), divmod(), complex()  │
│ Sequence/Collection    │ len(), range(), enumerate(), zip() │
│                        │ sorted(), reversed(), filter()     │
│                        │ map(), any(), all(), slice()       │
│ Type Conversion        │ int(), float(), str(), bool()      │
│                        │ list(), tuple(), set(), dict()     │
│                        │ frozenset(), bytes(), bytearray()  │
│ Object/Info            │ help(), dir(), id(), hash()        │
│                        │ type(), isinstance(), callable()   │
│ String Related         │ ord(), chr(), format(), repr()     │
│                        │ ascii(), bin(), hex(), oct()       │
│ Advanced               │ eval(), exec(), compile()          │
│                        │ globals(), locals(), vars()        │
│ Class Related          │ classmethod(), staticmethod()      │
│                        │ property(), super(), object()      │
│ Other                  │ iter(), next(), enumerate()        │
│                        │ zip(), filter(), map(), memoryview()│
└────────────────────────┴────────────────────────────────────┘
""")


# ============================================================
# PART 8: FUNCTION EXECUTION — BEHIND THE SCENES
# ============================================================

print("=" * 60)
print("📊 HOW FUNCTION EXECUTION WORKS (INTERNAL)")
print("=" * 60)

print("""
When you CALL a function, Python:

1️⃣  CALL STACK mein function push hota hai
2️⃣  Parameters ko arguments se initialize karta hai
3️⃣  Function body execute karta hai (Line by line)
4️⃣  Return value (ya None) ke saath function pop hota hai
5️⃣  Calling code se continue karta hai

VISUAL EXECUTION FLOW:

def leaveGenerator(name, date):
    msg = f"...{name}...{date}..."          ← Step 3
    print(msg)                                ← Step 4
    
# Main program
print("Start")                                ← Step 1
leaveGenerator("Ibrahim", "15th July")        ← Step 2
#             └─ name="Ibrahim", date="15th July"
print("End")                                  ← Step 5 (After function returns)

OUTPUT:
Start                                         (Step 1)
Assalam u alaikum Sir,                        (Step 4)
 This is Ibrahim and i will not come...
 Thanks!
End                                           (Step 5)
""")


# ============================================================
# PART 9: COMMON MISTAKES
# ============================================================

print("=" * 60)
print("📊 COMMON MISTAKES IN FUNCTIONS")
print("=" * 60)

print("""
❌ MISTAKE 1: Function call karte waqt parentheses () bhoolna
   def greet():
       print("Hello")
   
   greet        ← Function execute nahi hoga! (Object reference)
   greet()      ← Sahi! Function execute hoga


❌ MISTAKE 2: Parameters aur Arguments mein mismatch
   def greet(name, age):
       print(f"{name} is {age} years old")
   
   greet("Ibrahim")           ← ERROR! age argument missing
   greet("Ibrahim", 22)       ← Sahi!


❌ MISTAKE 3: Indentation galat
   def greet():
   print("Hello")             ← IndentationError!
   
   def greet():
       print("Hello")         ← Sahi! 4 spaces


❌ MISTAKE 4: Function define karne se pehle call karna
   greet()                    ← NameError! Abhi define nahi hua
   
   def greet():
       print("Hello")
   
   greet()                    ← Sahi! Pehle define, phir call


❌ MISTAKE 5: Built-in function names ko variable ke liye use karna
   print = "Hello"            ← print() function overwrite!
   print("World")             ← ERROR! str object not callable
   
   my_print = "Hello"         ← Sahi! Built-in names avoid karo
""")


# ============================================================
# PART 10: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — FUNCTIONS")
print("=" * 60)

print("""
✅ WHAT IS A FUNCTION?
   Reusable code block jo specific task perform karta hai.
   Input leta hai, process karta hai, output de sakta hai.

✅ WHAT IS def?
   Python keyword to DEFINE a function.
   def function_name(parameters):
       # function body

✅ PARAMETER vs ARGUMENT:
   Parameter → Function DEFINITION mein variable
   Argument  → Function CALL mein actual value

✅ TYPES OF FUNCTIONS:
   1. Built-in Functions    (Python ke saath aate hain)
   2. User-Defined Functions (Hum khud banate hain)

✅ BUILT-IN FUNCTIONS (Most Used):
   print(), input(), len(), type(), range()
   int(), str(), float(), bool(), list(), tuple(), set(), dict()
   max(), min(), sum(), abs(), round(), pow()
   sorted(), reversed(), enumerate(), zip(), filter(), map()
   help(), dir(), id(), ord(), chr(), format()

✅ FUNCTION EXECUTION:
   Define hone se execute nahi hota
   CALL karne par execute hota hai
   Har call ke liye alag execution context

✅ GOLDEN RULES:
   • def se define, () se call
   • Parameters aur arguments ka match hona zaroori
   • Indentation (4 spaces) compulsory
   • Function names meaningful rakho (snake_case)
   • Built-in names avoid karo
   • Pehle define, phir call
""")


# ============================================================
# QUIZ SECTION
# ============================================================

print("\n\n" + "=" * 60)
print("📝 QUICK QUIZ — FUNCTIONS")
print("=" * 60)

print("""
QUIZ 1: Function Definition
─────────────────────────────
Q: Function define karne ke liye kaunsa keyword use hota hai?
A: def

Q: Function call karne ke liye kya use karte hain?
A: Parentheses () — e.g., function_name()

Q: def greeting(): ke baad colon (:) bhool jayein to kya hoga?
A: SyntaxError


QUIZ 2: Parameters vs Arguments
─────────────────────────────────
Q: def add(a, b): — yahan a aur b kya hain?
A: PARAMETERS

Q: add(5, 3) — yahan 5 aur 3 kya hain?
A: ARGUMENTS

Q: Kya parameter aur argument ka naam same hona zaroori hai?
A: Nahi! Argument actual value hai, parameter variable.


QUIZ 3: Built-in Functions
─────────────────────────────
Q: User se input lene ke liye kaunsa function?
A: input()

Q: List ki length check karne ke liye?
A: len()

Q: String ko integer mein convert karne ke liye?
A: int()

Q: Negative number ko positive banane ke liye?
A: abs()

Q: List ke saare items ka sum karne ke liye?
A: sum()


QUIZ 4: Code Output
─────────────────────
Q: Iska output kya hoga?
   def greet():
       print("Hello")
   greet()
   greet()
   
A: Hello
   Hello
   (Do baar call hua, do baar print hua)


Q: Iska output kya hoga?
   def add(a, b):
       print(a + b)
   add(5, 3)
   add(10, 20)
   
A: 8
   30


QUIZ 5: True or False
───────────────────────
1. Function define hote hi execute ho jata hai.        (FALSE)
2. print() ek built-in function hai.                   (TRUE)
3. def ek keyword hai.                                 (TRUE)
4. Function bina parameters ke ho sakta hai.           (TRUE)
5. Har function ko return statement ki zaroorat hai.   (FALSE)
""")