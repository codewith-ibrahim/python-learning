# Constructors and self in Python

# Constructor kya hota hai?
#
# Constructor ek SPECIAL METHOD hai jo OBJECT CREATE hote
# hi AUTOMATICALLY call hota hai. Iska kaam hai object ke
# attributes ko INITIALIZE karna (shuru ki values set karna).
#
# Python mein constructor ka naam __init__ hai.
# (Double underscore = "dunder" methods)

# self kya hai?
#
# self OBJECT KA REFERENCE hota hai.
# Jis object ke liye method call ho raha hai,
# self usi object ko point karta hai.
# self = "Is object ka" ya "Apna"


# ============================================================
# PART 1: WITHOUT CONSTRUCTOR (PROBLEM)
# ============================================================

print("=" * 60)
print("📊 WITHOUT CONSTRUCTOR — THE PROBLEM")
print("=" * 60)

class EmployeeOld:
    pass

# Object banana aur alag-alag attributes set karna
emp1 = EmployeeOld()
emp1.name = "Ibrahim"
emp1.salary = 25000
emp1.id = "EMP-001"

emp2 = EmployeeOld()
emp2.name = "Ali"
emp2.salary = 30000
emp2.id = "EMP-002"

print(f"\n   Employee 1: {emp1.name}, Salary: {emp1.salary}, ID: {emp1.id}")
print(f"   Employee 2: {emp2.name}, Salary: {emp2.salary}, ID: {emp2.id}")

print("""
❌ PROBLEMS WITHOUT CONSTRUCTOR:
   1. Har baar manually attributes set karne padte hain
   2. Koi guarantee nahi ke sab attributes set hue hain
   3. Code repeat hota hai (Boilerplate)
   4. Bhool sakte hain koi attribute set karna
""")


# ============================================================
# PART 2: WITH CONSTRUCTOR (AUR AUR SELF SAMJHO)
# ============================================================

print("=" * 60)
print("📊 WITH CONSTRUCTOR — __init__ AUR SELF")
print("=" * 60)

# Aapka Code (Same structure):
class Employee:
    
    # __init__ = Constructor (Object create hote hi chalta hai)
    # self = "Is object ka" reference
    # name, salary, id = Parameters (Object create karte waqt denge)
    
    def __init__(self, name, salary, id):
        # self.name = "IS object ke name" mein parameter wali value daalo
        self.name = name
        # self.salary = "IS object ki salary" mein parameter wali value daalo
        self.salary = salary
        # self.id = "IS object ki ID" mein parameter wali value daalo
        self.id = id
        print(f"   🔨 Constructor called for {self.name}!")  # Proof ke constructor chala
    
    # Method — self automatically pass hota hai
    def getSalary(self):
        # self.salary = "IS object ki salary" return karo
        return self.salary
    
    def getInfo(self):
        # Poori information return karo
        return f"ID: {self.id} | Name: {self.name} | Salary: Rs. {self.salary}"


# Objects Banana (Constructor automatically call hoga!)
print("\n🔍 Creating Employees...")

# Yahan teen arguments pass ho rahe hain: name, salary, id
# self automatically pass hota hai — likhne ki zaroorat nahi!
emp1 = Employee("Ibrahim", "25000", "Sr.fe-1234567")
emp2 = Employee("Ali", "30000", "Jr.fe-7654321")
emp3 = Employee("Sara", "28000", "Md.fe-1122334")

# Aapka original print statement
print(f"\n   Employee ID is {emp1.id} \n   Name: {emp1.name} \n   Your current month salary is Rs. {emp1.salary}")

print(f"\n   {emp2.getInfo()}")
print(f"   {emp3.getInfo()}")


# ============================================================
# PART 3: SELF — DEEP EXPLANATION
# ============================================================

print("\n" + "=" * 60)
print("📊 SELF — POORA SAMJHO")
print("=" * 60)

print("""
self ka matlab: "ISS OBJECT KA"

Jab aap likhte hain:
emp1 = Employee("Ibrahim", "25000", "Sr.fe-1234567")

Python internally kya karta hai:
Employee.__init__(emp1, "Ibrahim", "25000", "Sr.fe-1234567")
                  ^^^^
                  self = emp1 (Automatically!)

To:
self.name = name  →  emp1.name = "Ibrahim"
self.salary = salary  →  emp1.salary = "25000"
self.id = id  →  emp1.id = "Sr.fe-1234567"


SIMPLE ANALOGY:
Socho aap form bhar rahe hain:

class Form:
    def __init__(self, name, age):
        self.name = name    # "IS form" mein name likho
        self.age = age      # "IS form" mein age likho

form1 = Form("Ibrahim", 22)   # self = form1
form2 = Form("Ali", 21)       # self = form2

form1 aur form2 DONO Form class ke hain
Lekin ALAG objects hain — ALAG self!
form1 ka self ≠ form2 ka self
""")


# ============================================================
# PART 4: CONSTRUCTOR — AUR KYA KAR SAKTA HAI?
# ============================================================

print("=" * 60)
print("📊 CONSTRUCTOR — DIFFERENT USE CASES")
print("=" * 60)


# Use Case 1: Default Values
class Student:
    def __init__(self, name, age, grade="Not Assigned"):
        self.name = name
        self.age = age
        self.grade = grade  # Agar grade na do to "Not Assigned"
        self.is_enrolled = True  # Default True
        print(f"   ✅ Student {self.name} created!")

print("\n1️⃣  Default Values:")
s1 = Student("Ibrahim", 22, "A+")
s2 = Student("Ali", 21)  # Grade nahi diya — default use hoga
print(f"   {s1.name}: Grade {s1.grade}")
print(f"   {s2.name}: Grade {s2.grade}")


# Use Case 2: Validation in Constructor
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        
        # Validation — balance negative nahi ho sakta!
        if balance < 0:
            print(f"   ❌ Error: Balance cannot be negative! Setting to 0.")
            self.balance = 0
        else:
            self.balance = balance
        
        print(f"   🏦 Account created for {self.holder} — Balance: Rs. {self.balance}")

print("\n2️⃣  Validation in Constructor:")
acc1 = BankAccount("Ibrahim", 50000)
acc2 = BankAccount("Ali", -5000)  # Negative balance — reject!


# Use Case 3: Auto-generate values
class User:
    count = 0  # Class attribute — sab objects share karenge
    
    def __init__(self, name):
        User.count += 1  # Har naye user par count badhao
        self.name = name
        self.user_id = f"USER-{User.count:03d}"  # Auto-generate ID
        self.created_at = "Today"  # Real mein datetime use karte
        print(f"   👤 {self.user_id}: {self.name}")

print("\n3️⃣  Auto-generated Values:")
u1 = User("Ibrahim")
u2 = User("Ali")
u3 = User("Sara")
print(f"   Total Users: {User.count}")


# ============================================================
# PART 5: YOUR CODE — LINE BY LINE
# ============================================================

print("\n" + "=" * 60)
print("📊 AAPKA CODE — LINE BY LINE BREAKDOWN")
print("=" * 60)

print("""
AAPKA CODE:
────────────────────────────────────────────────────────
class Employee:
    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id

    def getSalary(self):
        return self.salary
        
emp1 = Employee("Ali", "25000", "Sr.fe-1234567")

print(f"Employe ID is {emp1.id}")
print(f"Name {emp1.name}")
print(f"Your current month salary is {emp1.salary}")
────────────────────────────────────────────────────────

LINE BY LINE:
🔹 class Employee: → "Employee" naam ki class banao
🔹 def __init__(self, name, salary, id): → Constructor
   • self → Object ka reference (automatic)
   • name, salary, id → Ye values object create karte waqt denge
🔹 self.name = name → Object ke 'name' attribute mein value store karo
🔹 self.salary = salary → Object ke 'salary' attribute mein value store karo
🔹 self.id = id → Object ke 'id' attribute mein value store karo
🔹 def getSalary(self): → Method jo salary return karega
🔹 emp1 = Employee("Ali", "25000", "Sr.fe-1234567") → Object create
   • __init__ automatically call hoga
   • self = emp1
   • emp1.name = "Ali"
   • emp1.salary = "25000"
   • emp1.id = "Sr.fe-1234567"
🔹 print(f"...{emp1.id}...") → emp1 ke id attribute ko access karo
""")


# ============================================================
# PART 6: REAL LIFE EXAMPLES WITH CONSTRUCTOR
# ============================================================

print("=" * 60)
print("📊 REAL LIFE CONSTRUCTOR EXAMPLES")
print("=" * 60)


# Example 1: Laptop
class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False
        self.battery = 100
        print(f"   💻 {self.brand} {self.model} ready! (Rs. {self.price:,})")
    
    def info(self):
        return f"{self.brand} {self.model} — Rs. {self.price:,}"

print("\n1️⃣  Laptop:")
l1 = Laptop("Dell", "XPS 15", 250000)
l2 = Laptop("Apple", "MacBook Pro", 450000)
print(f"   {l1.info()}")
print(f"   {l2.info()}")


# Example 2: Student Registration
class StudentReg:
    def __init__(self, name, course, fee):
        self.name = name
        self.course = course
        self.fee = fee
        self.is_paid = fee > 0
        self.roll_no = f"PY-{hash(name) % 1000:03d}"
        status = "✅ Paid" if self.is_paid else "❌ Pending"
        print(f"   📝 {self.roll_no}: {name} — {course} ({status})")

print("\n2️⃣  Student Registration:")
st1 = StudentReg("Ibrahim", "Python", 5000)
st2 = StudentReg("Ali", "Python", 0)


# Example 3: Pizza Order
class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        self.price = self.calculate_price()
        print(f"   🍕 {size} Pizza with {', '.join(toppings)} — Rs. {self.price}")
    
    def calculate_price(self):
        base = {"Small": 500, "Medium": 800, "Large": 1200}
        topping_price = len(self.toppings) * 50
        return base.get(self.size, 800) + topping_price

print("\n3️⃣  Pizza Order:")
p1 = Pizza("Large", ["Cheese", "Pepperoni", "Olives"])
p2 = Pizza("Medium", ["Cheese"])


# ============================================================
# PART 7: COMMON MISTAKES
# ============================================================

print("\n" + "=" * 60)
print("📊 COMMON MISTAKES")
print("=" * 60)

print("""
❌ MISTAKE 1: __init__ mein self bhoolna
   class Student:
       def __init__(name, age):    ← self missing!
           self.name = name
   
✅ CORRECT:
   class Student:
       def __init__(self, name, age):
           self.name = name


❌ MISTAKE 2: self.attribute ke bajaye local variable
   class Student:
       def __init__(self, name):
           name = name    ← Local variable! Object ka attribute nahi!
   
   s = Student("Ibrahim")
   print(s.name)   ← AttributeError!
   
✅ CORRECT:
   class Student:
       def __init__(self, name):
           self.name = name    ← self. zaroori hai!


❌ MISTAKE 3: Object create karte waqt arguments bhoolna
   class Employee:
       def __init__(self, name, salary):
           self.name = name
           self.salary = salary
   
   emp = Employee()   ← TypeError! name, salary missing!
   
✅ CORRECT:
   emp = Employee("Ibrahim", 25000)


❌ MISTAKE 4: Constructor ko manually call karna
   emp = Employee("Ibrahim", 25000)
   emp.__init__("Ali", 30000)    ← Don't do this!
   
✅ Constructor automatically call hota hai, manually nahi!
""")


# ============================================================
# PART 8: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — CONSTRUCTORS & SELF")
print("=" * 60)

print("""
✅ CONSTRUCTOR (__init__):
   • Special method, auto-call on object creation
   • def __init__(self, parameters):
   • Object ke attributes initialize karta hai
   • Har object ke liye ek baar chalta hai

✅ SELF:
   • Object ka reference
   • Method ka pehla parameter (automatic)
   • self.attribute = value
   • "Is object ka" attribute

✅ AAPKA CODE SAMJHO:
   class Employee:
       def __init__(self, name, salary, id):
           self.name = name      ← self = object reference
           self.salary = salary   ← name = parameter value
           self.id = id           ← id = parameter value

   emp1 = Employee("Ali", "25000", "Sr.fe-1234567")
   # __init__ automatically call hua
   # emp1.name = "Ali", emp1.salary = "25000", emp1.id = "Sr.fe-1234567"

✅ GOLDEN RULES:
   • __init__ ka pehla parameter hamesha self
   • self.attribute se hi object ka data store hota hai
   • Object create karte waqt self mat do (automatic hai)
   • Constructor validation ke liye best jagah hai
""")