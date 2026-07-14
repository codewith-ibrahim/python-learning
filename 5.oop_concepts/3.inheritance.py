# Inheritance in Python

# Inheritance kya hota hai?
#
# Inheritance ek MECHANISM hai jisme ek CLASS doosri class
# ki PROPERTIES aur METHODS ko INHERIT (virsa) kar leti hai.
# Matlab: Parent class ka sab kuch child class ko mil jata hai!
#
# Technical Definition:
# Inheritance OOP ka ek pillar hai jo CODE REUSABILITY
# provide karta hai. Child class parent class ke attributes
# aur methods ko use kar sakti hai, unhe modify kar sakti hai,
# aur naye features add kar sakti hai.

# Real Life Analogy:
# 👨‍👦 Baap ka business → Beta inherit karta hai
# 🏠 Parent ki property → Children ko milti hai
#
# Programming mein:
# Parent Class (Base) → Child Class (Derived) ko sab kuch milta hai!
# Phir child apne hisaab se naye features add kar sakta hai.


# ============================================================
# PART 1: WITHOUT INHERITANCE (THE PROBLEM)
# ============================================================

print("=" * 60)
print("📊 WITHOUT INHERITANCE — CODE REPEAT")
print("=" * 60)

# Teen alag-alag classes — same code baar baar!

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"   Hi, I am {self.name}, {self.age} years old")

class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    
    def introduce(self):
        print(f"   Hi, I am {self.name}, {self.age} years old")

class Staff:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    
    def introduce(self):
        print(f"   Hi, I am {self.name}, {self.age} years old")

print("\n   ❌ PROBLEMS:")
print("   1. name aur age har class mein repeat ho rahe hain")
print("   2. introduce() method teeno mein same hai")
print("   3. Agar koi change karna ho to teeno jagah karna padega!")
print("   4. DRY Principle (Don't Repeat Yourself) violate ho raha hai")


# ============================================================
# PART 2: WITH INHERITANCE (THE SOLUTION)
# ============================================================

print("\n" + "=" * 60)
print("📊 WITH INHERITANCE — CODE REUSE")
print("=" * 60)

# Base/Parent Class — Common code yahan ek baar likho!
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"   👤 Person created: {self.name}")
    
    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old"
    
    def celebrate_birthday(self):
        self.age += 1
        return f"🎂 Happy Birthday {self.name}! Now {self.age} years old!"


# Child Class — Person se inherit karega!
class Student(Person):  # ← () mein Parent class ka naam!
    def __init__(self, name, age, course):
        # super() = Parent class ko call karo
        super().__init__(name, age)  # Parent ka constructor chalao
        self.course = course
        print(f"   📚 Student created: {self.name} — {self.course}")
    
    def study(self):
        return f"📖 {self.name} is studying {self.course}"


# Another Child Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        print(f"   🏫 Teacher created: {self.name} — {self.subject}")
    
    def teach(self):
        return f"📝 {self.name} is teaching {self.subject}"


# Another Child Class
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
        print(f"   💼 Staff created: {self.name} — {self.department}")
    
    def work(self):
        return f"💻 {self.name} is working in {self.department}"


# Objects Banana
print("\n🔍 Creating Objects:")
print("-" * 40)

student1 = Student("Ibrahim", 22, "Python")
teacher1 = Teacher("Dr. Ahmed", 45, "Computer Science")
staff1 = Staff("Mr. Khan", 35, "Administration")

# Sabhi parent class ke methods use kar sakte hain!
print(f"\n   📢 Introductions:")
print(f"   {student1.introduce()}")    # Parent method
print(f"   {teacher1.introduce()}")    # Parent method
print(f"   {staff1.introduce()}")      # Parent method

# Apne khud ke methods
print(f"\n   🎯 Specific Methods:")
print(f"   {student1.study()}")
print(f"   {teacher1.teach()}")
print(f"   {staff1.work()}")

# Parent method sab use kar sakte hain
print(f"\n   🎂 Birthday:")
print(f"   {student1.celebrate_birthday()}")
print(f"   {student1.celebrate_birthday()}")


# ============================================================
# PART 3: TYPES OF INHERITANCE
# ============================================================

print("\n" + "=" * 60)
print("📊 TYPES OF INHERITANCE")
print("=" * 60)

print("""
PYTHON MEIN 5 TYPES:

1️⃣  SINGLE INHERITANCE
    One Parent → One Child
    
    class A:
        pass
    class B(A):    ← B inherits from A
        pass


2️⃣  MULTIPLE INHERITANCE
    Multiple Parents → One Child
    
    class A:
        pass
    class B:
        pass
    class C(A, B):    ← C inherits from both A and B
        pass


3️⃣  MULTILEVEL INHERITANCE
    Parent → Child → Grandchild
    
    class A:
        pass
    class B(A):    ← B inherits from A
        pass
    class C(B):    ← C inherits from B (which inherits from A)
        pass


4️⃣  HIERARCHICAL INHERITANCE
    One Parent → Multiple Children
    
    class A:
        pass
    class B(A):    ← Both inherit from A
        pass
    class C(A):    ← Both inherit from A
        pass


5️⃣  HYBRID INHERITANCE
    Mix of two or more types
""")


# ============================================================
# PART 4: SINGLE INHERITANCE EXAMPLE
# ============================================================

print("=" * 60)
print("📊 SINGLE INHERITANCE — DETAILED EXAMPLE")
print("=" * 60)


class Animal:
    """Parent Class — Animal"""
    
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        return f"🍽️  {self.name} is eating"
    
    def sleep(self):
        return f"😴 {self.name} is sleeping"
    
    def breathe(self):
        return f"🫁 {self.name} is breathing"


class Dog(Animal):
    """Child Class — Dog inherits from Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name)  # Parent constructor call
        self.breed = breed
        self.legs = 4
    
    def bark(self):
        return f"🐕 {self.name} says: Woof Woof!"
    
    def info(self):
        return f"{self.name} is a {self.breed} with {self.legs} legs"


class Cat(Animal):
    """Child Class — Cat inherits from Animal"""
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def meow(self):
        return f"🐱 {self.name} says: Meow Meow!"
    
    def info(self):
        return f"{self.name} is a {self.color} cat"


print("\n🔍 Animal Kingdom:")
dog = Dog("Tommy", "German Shepherd")
cat = Cat("Whiskers", "Orange")

# Parent class methods (Inherited!)
print(f"   {dog.eat()}")
print(f"   {dog.sleep()}")
print(f"   {dog.bark()}")       # Apna method
print(f"   {dog.info()}")

print()
print(f"   {cat.eat()}")
print(f"   {cat.sleep()}")
print(f"   {cat.meow()}")       # Apna method
print(f"   {cat.info()}")


# ============================================================
# PART 5: MULTIPLE INHERITANCE EXAMPLE
# ============================================================

print("\n" + "=" * 60)
print("📊 MULTIPLE INHERITANCE — EXAMPLE")
print("=" * 60)


class Flyer:
    """Udne wala."""
    def fly(self):
        return f"✈️  Flying high!"


class Swimmer:
    """Tairne wala."""
    def swim(self):
        return f"🏊 Swimming deep!"


class Duck(Flyer, Swimmer):
    """Duck — Dono parents se inherit karega!"""
    
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"🦆 {self.name} says: Quack Quack!"
    
    def info(self):
        return f"{self.name} can fly AND swim!"


print("\n🔍 Duck — Multiple Abilities:")
duck = Duck("Donald")
print(f"   {duck.info()}")
print(f"   {duck.fly()}")       # Flyer se aaya
print(f"   {duck.swim()}")      # Swimmer se aaya
print(f"   {duck.quack()}")     # Apna method


# ============================================================
# PART 6: METHOD OVERRIDING
# ============================================================

print("\n" + "=" * 60)
print("📊 METHOD OVERRIDING")
print("=" * 60)

print("""
Method Overriding = Child class parent ke method ko
APNE HISAB SE CHANGE kare!

Parent ka method = Default behavior
Child ka method = Custom behavior (Override!)
""")


class Shape:
    """Parent Class."""
    def area(self):
        return "Area not defined (Generic Shape)"
    
    def perimeter(self):
        return "Perimeter not defined"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Parent ke method ko OVERRIDE kar rahe hain!
    def area(self):
        return f"⭕ Circle Area: {3.14 * self.radius ** 2:.2f}"
    
    def perimeter(self):
        return f"⭕ Circle Perimeter: {2 * 3.14 * self.radius:.2f}"


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return f"⬜ Rectangle Area: {self.length * self.width}"
    
    def perimeter(self):
        return f"⬜ Rectangle Perimeter: {2 * (self.length + self.width)}"


print("\n🔍 Shapes:")
circle = Circle(5)
rect = Rectangle(10, 5)

print(f"   {circle.area()}")
print(f"   {circle.perimeter()}")
print()
print(f"   {rect.area()}")
print(f"   {rect.perimeter()}")


# ============================================================
# PART 7: super() — DETAILED EXPLANATION
# ============================================================

print("\n" + "=" * 60)
print("📊 super() — PARENT KO CALL KARO")
print("=" * 60)

print("""
super() kya karta hai?
Parent class ke methods ko CALL karta hai.

USE CASES:
1. Parent ka constructor call karna
2. Parent ka method call karke usme kuch add karna
3. Multiple inheritance mein proper order maintain karna
""")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"   👔 Employee.__init__ called for {name}")
    
    def get_details(self):
        return f"Name: {self.name}, Salary: Rs. {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        # super() se parent ka constructor call
        super().__init__(name, salary)
        self.department = department
        print(f"   📊 Manager.__init__ called — {department}")
    
    def get_details(self):
        # Parent ka method call karke usme kuch add karna
        basic = super().get_details()
        return f"{basic}, Department: {self.department}"


class SeniorManager(Manager):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size
        print(f"   🏆 SeniorManager.__init__ called — Team: {team_size}")
    
    def get_details(self):
        basic = super().get_details()
        return f"{basic}, Team Size: {self.team_size}"


print("\n🔍 Manager Hierarchy:")
sm = SeniorManager("Ibrahim", 150000, "AI Department", 10)
print(f"\n   📋 Details: {sm.get_details()}")


# ============================================================
# PART 8: isinstance() AND issubclass()
# ============================================================

print("\n" + "=" * 60)
print("📊 CHECKING RELATIONSHIPS")
print("=" * 60)

print("\n🔍 Type Checking:")
print(f"   Is dog a Dog? {isinstance(dog, Dog)}")           # True
print(f"   Is dog an Animal? {isinstance(dog, Animal)}")    # True (Inherited!)
print(f"   Is dog a Cat? {isinstance(dog, Cat)}")           # False
print(f"   Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")  # True
print(f"   Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")  # False


# ============================================================
# PART 9: REAL LIFE EXAMPLE
# ============================================================

print("\n" + "=" * 60)
print("📊 REAL LIFE: PAYMENT SYSTEM")
print("=" * 60)


class Payment:
    """Base Payment Class."""
    def __init__(self, amount):
        self.amount = amount
    
    def process_payment(self):
        return f"💳 Processing payment of Rs. {self.amount}"
    
    def receipt(self):
        return f"🧾 Receipt: Rs. {self.amount} paid"


class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number[-4:]  # Last 4 digits
    
    def process_payment(self):
        return f"💳 Credit Card (****{self.card_number}): Rs. {self.amount} — Processing..."
    
    def validate(self):
        return f"✅ Card ****{self.card_number} validated!"


class JazzCash(Payment):
    def __init__(self, amount, phone):
        super().__init__(amount)
        self.phone = phone
    
    def process_payment(self):
        return f"📱 JazzCash ({self.phone}): Rs. {self.amount} — Processing..."
    
    def send_otp(self):
        return f"📩 OTP sent to {self.phone}"


class BankTransfer(Payment):
    def __init__(self, amount, account):
        super().__init__(amount)
        self.account = account
    
    def process_payment(self):
        return f"🏦 Bank Transfer (ACC:{self.account}): Rs. {self.amount} — Processing..."
    
    def verify_account(self):
        return f"✅ Account {self.account} verified!"


print("\n🔍 Processing Payments:")
payments = [
    CreditCard(5000, "1234567890123456"),
    JazzCash(3000, "03123456789"),
    BankTransfer(10000, "PK1234567"),
]

for payment in payments:
    print(f"   {payment.process_payment()}")
    print(f"   {payment.receipt()}")  # Common method from parent
    print()


# ============================================================
# PART 10: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — INHERITANCE")
print("=" * 60)

print("""
✅ INHERITANCE:
   • Child class parent se sab kuch inherit karti hai
   • Code reusability provide karta hai
   • DRY Principle follow hota hai

✅ SYNTAX:
   class Parent:
       pass
   
   class Child(Parent):    ← Parent class brackets mein!
       pass

✅ TYPES:
   • Single: One Parent → One Child
   • Multiple: Multiple Parents → One Child
   • Multilevel: Parent → Child → Grandchild
   • Hierarchical: One Parent → Multiple Children

✅ super():
   • Parent class ke methods call karta hai
   • super().__init__() — Parent constructor
   • super().method() — Parent method

✅ METHOD OVERRIDING:
   • Child parent ke method ko change kar sakta hai
   • Same naam, different implementation

✅ isinstance() & issubclass():
   • isinstance(obj, Class) — Object us class ka hai?
   • issubclass(Child, Parent) — Child parent se derived hai?

✅ GOLDEN RULES:
   • super() se parent constructor zaroor call karo
   • Method overriding mein same signature rakho
   • Deep inheritance avoid karo (Max 3-4 levels)
   • Composition over Inheritance (when possible)
""")