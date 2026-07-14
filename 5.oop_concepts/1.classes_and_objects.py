# Classes and Objects in Python

# Class kya hoti hai?
#
# Class ek BLUEPRINT ya TEMPLATE hai.
# Jaise ghar banane ka naksha (blueprint) hota hai,
# usi tarah class ek design hai objects banane ke liye.
#
# Technical Definition:
# Class ek user-defined data type hai jo data (attributes)
# aur functions (methods) ko ek saath bundle karta hai.


# Object kya hota hai?
#
# Object class ka INSTANCE hai.
# Jaise blueprint se actual ghar banta hai,
# usi tarah class se actual object banta hai.
#
# Real Life Analogy:
# 🏠 Class  = Ghar ka NAKSHA (Blueprint)
# 🏠 Object = ASLI GHAR (Real Instance)
#
# Ek blueprint se KAI ghar ban sakte hain!
# Ek class se KAI objects ban sakte hain!


# ============================================================
# PART 1: SIMPLE CLASS (WITHOUT __init__)
# ============================================================

print("=" * 60)
print("📊 SIMPLE CLASS — BASIC CONCEPT")
print("=" * 60)


class Student:
    """Ye Student class ka blueprint hai."""
    
    # Class Attribute (Sab objects ke liye same)
    school = "Python University"
    
    # Instance Attributes (Har object ke liye alag)
    name = "Unknown"
    age = 0
    grade = "N/A"


# Objects Banana (Instance Create Karna)
print("\n🔍 Creating Objects:")

# Object 1
student1 = Student()
student1.name = "Ibrahim"
student1.age = 22
student1.grade = "A+"

# Object 2
student2 = Student()
student2.name = "Ali"
student2.age = 21
student2.grade = "B"

# Object 3
student3 = Student()
student3.name = "Sara"
student3.age = 23
student3.grade = "A"

print(f"   Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
print(f"   Student 2: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")
print(f"   Student 3: {student3.name}, Age: {student3.age}, Grade: {student3.grade}")
print(f"   All study at: {student1.school}")


# ============================================================
# PART 2: CLASS WITH METHODS
# ============================================================

print("\n" + "=" * 60)
print("📊 CLASS WITH METHODS")
print("=" * 60)


class Car:
    """Car class — Blueprint for car objects."""
    
    # Class Attribute
    wheels = 4  # Sab cars ke 4 wheels hote hain
    
    def __init__(self, brand, model, color):
        # Instance Attributes (Har car ke liye alag)
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False
    
    def start(self):
        """Car start karo."""
        self.is_running = True
        return f"🚗 {self.brand} {self.model} started!"
    
    def stop(self):
        """Car stop karo."""
        self.is_running = False
        return f"🛑 {self.brand} {self.model} stopped!"
    
    def honk(self):
        """Horn bajao."""
        return f"📢 {self.brand} says: Beep Beep!"
    
    def info(self):
        """Car ki information dikhao."""
        return f"{self.color} {self.brand} {self.model} ({self.wheels} wheels)"


# Objects Banana
car1 = Car("Toyota", "Corolla", "White")
car2 = Car("Honda", "Civic", "Black")
car3 = Car("Suzuki", "Mehran", "Silver")

print("\n🔍 Car Objects:")
print(f"   {car1.info()}")
print(f"   {car2.info()}")
print(f"   {car3.info()}")

print(f"\n   {car1.start()}")
print(f"   {car1.honk()}")
print(f"   {car1.stop()}")


# ============================================================
# PART 3: CLASS vs OBJECT (IMPORTANT DIFFERENCE)
# ============================================================

print("\n" + "=" * 60)
print("📊 CLASS vs OBJECT")
print("=" * 60)

print("""
┌──────────────┬────────────────────────┬──────────────────────┐
│ CLASS        │ OBJECT                 │ Analogy              │
├──────────────┼────────────────────────┼──────────────────────┤
│ Blueprint    │ Real Instance          │ Naksha vs Ghar       │
│ Template     │ Actual Thing           │ Form vs Filled Form  │
│ Design       │ Implementation         │ Recipe vs Dish       │
│ One          │ Many                   │ 1 Recipe → Many Dishes│
│ No Memory*   │ Memory Leta Hai        │                      │
└──────────────┴────────────────────────┴──────────────────────┘

class Car:        ← Ye CLASS hai (Blueprint)
    pass

car1 = Car()      ← Ye OBJECT hai (Real Instance)
car2 = Car()      ← Ye bhi OBJECT hai (Another Instance)

car1 aur car2 DONO Car class ke objects hain.
Lekin DONO ALAG hain — memory mein alag jagah!
""")


# ============================================================
# PART 4: CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# ============================================================

print("=" * 60)
print("📊 CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES")
print("=" * 60)


class BankAccount:
    """Bank Account class."""
    
    # Class Attribute (Sab accounts ke liye same)
    bank_name = "Python National Bank"
    interest_rate = 5.0  # 5%
    
    def __init__(self, holder_name, account_number, balance):
        # Instance Attributes (Har account ke liye alag)
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance


# Objects
acc1 = BankAccount("Ibrahim", "ACC001", 50000)
acc2 = BankAccount("Ali", "ACC002", 30000)

print("\n🔍 Account Details:")
print(f"   Account 1: {acc1.holder_name} — Rs. {acc1.balance}")
print(f"   Account 2: {acc2.holder_name} — Rs. {acc2.balance}")
print(f"   Bank: {BankAccount.bank_name}")

# Class attribute sab objects ke liye SAME
print(f"\n   {acc1.holder_name}'s Bank: {acc1.bank_name}")
print(f"   {acc2.holder_name}'s Bank: {acc2.bank_name}")


# ============================================================
# PART 5: SELF — WHAT IS IT?
# ============================================================

print("\n" + "=" * 60)
print("📊 SELF — COMPLETE EXPLANATION")
print("=" * 60)

print("""
self kya hai?

self OBJECT KA REFERENCE hai.
Jis object ke liye method call ho raha hai,
self usi object ko point karta hai.

SIMPLE ANALOGY:
Socho aap form bhar rahe hain:

class Student:
    def fill_form(self, name, age):
        self.name = name    # "IS form" mein name likho
        self.age = age      # "IS form" mein age likho

student1 = Student()
student1.fill_form("Ibrahim", 22)
# Yahan self = student1
# self.name = "Ibrahim" → student1.name = "Ibrahim"

student2 = Student()
student2.fill_form("Ali", 21)
# Yahan self = student2
# self.name = "Ali" → student2.name = "Ali"


self KA MATLAB:
"Iss object ka" ya "Apna"
• self.name = "Apna naam"
• self.age = "Apni age"
""")


# ============================================================
# PART 6: METHODS (FUNCTIONS INSIDE CLASS)
# ============================================================

print("=" * 60)
print("📊 METHODS IN CLASS")
print("=" * 60)


class Calculator:
    """Simple Calculator Class."""
    
    def __init__(self, name):
        self.name = name
        self.history = []
    
    def add(self, a, b):
        """Addition."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication."""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division."""
        if b != 0:
            result = a / b
            self.history.append(f"{a} ÷ {b} = {result}")
            return result
        return "Cannot divide by zero!"
    
    def show_history(self):
        """Calculation history dikhao."""
        print(f"\n   📜 {self.name}'s Calculation History:")
        if self.history:
            for calc in self.history:
                print(f"   {calc}")
        else:
            print("   (Empty)")


# Object create
my_calc = Calculator("Ibrahim")

print("\n🔍 Calculator Operations:")
print(f"   Add: {my_calc.add(10, 5)}")
print(f"   Subtract: {my_calc.subtract(20, 8)}")
print(f"   Multiply: {my_calc.multiply(6, 7)}")
print(f"   Divide: {my_calc.divide(100, 4)}")

my_calc.show_history()


# ============================================================
# PART 7: REAL LIFE CLASS EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("📊 REAL LIFE CLASS EXAMPLES")
print("=" * 60)


# Example 1: Mobile Phone
class Mobile:
    """Mobile Phone class."""
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_on = False
        self.battery = 100
    
    def power_on(self):
        self.is_on = True
        return f"📱 {self.brand} {self.model} ON!"
    
    def power_off(self):
        self.is_on = False
        return f"📱 {self.brand} {self.model} OFF!"
    
    def make_call(self, number):
        if self.is_on and self.battery > 0:
            self.battery -= 5
            return f"📞 Calling {number}... (Battery: {self.battery}%)"
        return "❌ Phone is OFF or battery dead!"

phone = Mobile("Samsung", "S24", 250000)
print(f"\n   Phone: {phone.brand} {phone.model}")
print(f"   {phone.power_on()}")
print(f"   {phone.make_call('0312-3456789')}")


# Example 2: Book
class Book:
    """Book class."""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
    
    def read(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        return f"📖 Reading '{self.title}'... Page {self.current_page}/{self.pages}"
    
    def bookmark(self):
        return f"🔖 Bookmarked at page {self.current_page}"

book = Book("Python Programming", "Guido van Rossum", 500)
print(f"\n   Book: {book.title} by {book.author}")
print(f"   {book.read(50)}")
print(f"   {book.read(30)}")
print(f"   {book.bookmark()}")


# ============================================================
# PART 8: COMMON MISTAKES
# ============================================================

print("\n" + "=" * 60)
print("📊 COMMON MISTAKES")
print("=" * 60)

print("""
❌ MISTAKE 1: self parameter bhoolna
   class Student:
       def __init__(name, age):     ← self missing!
           self.name = name
   
✅ CORRECT:
   class Student:
       def __init__(self, name, age):
           self.name = name


❌ MISTAKE 2: Class aur object mein confuse hona
   class Car:
       pass
   
   print(Car.brand)    ← Car class hai, object nahi!
   
✅ CORRECT:
   my_car = Car()
   my_car.brand = "Toyota"
   print(my_car.brand)


❌ MISTAKE 3: self.attribute ko method ke bahar use karna
   self.name = "Ibrahim"    ← self sirf method ke andar!

✅ CORRECT:
   def set_name(self):
       self.name = "Ibrahim"


❌ MISTAKE 4: Class name Capital Letter se start na karna
   class student:     ← Convention: Capital letter!
   
✅ CORRECT:
   class Student:     ← PascalCase for classes
""")


# ============================================================
# PART 9: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — CLASSES & OBJECTS")
print("=" * 60)

print("""
✅ CLASS:
   • Blueprint ya Template
   • class ClassName: (PascalCase)
   • Attributes + Methods bundle
   • Ek class → Kai objects

✅ OBJECT:
   • Class ka Instance (Real thing)
   • Memory leta hai
   • object = ClassName()
   • Apne attributes rakhta hai

✅ SELF:
   • Object ka reference
   • Method ka pehla parameter
   • self.attribute = value
   • Automatically pass hota hai

✅ ATTRIBUTES:
   • Class Attribute: Sab objects ke liye same
   • Instance Attribute: Har object ke liye alag (self. se define)

✅ METHODS:
   • Functions inside class
   • Pehla parameter: self
   • Object.method() se call

✅ GOLDEN RULES:
   • Class name: PascalCase (Student, BankAccount)
   • Method name: snake_case (get_name, set_age)
   • self hamesha pehla parameter
   • __init__ = Constructor (Auto call)
""")