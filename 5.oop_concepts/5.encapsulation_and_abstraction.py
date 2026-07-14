# Encapsulation and Abstraction in Python

# Encapsulation kya hota hai?
#
# Encapsulation = Data aur Methods ko ek CLASS mein BUNDLE karna
# aur data ko OUTSIDE ACCESS se PROTECT karna.
#
# Simple Definition:
# Data HIDING — Bahar wala directly data access na kar sake!
# Sirf ALLOWED METHODS se hi data access ho!

# Abstraction kya hota hai?
#
# Abstraction = COMPLEXITY ko HIDE karna
# Sirf ZAROORI FEATURES dikhana, implementation details chhupana.
#
# Simple Definition:
# "Kya karta hai" dikhao, "Kaise karta hai" chhupao!

# Real Life Analogy:
# 📱 Mobile Phone:
#    Encapsulation: Internal circuits COVER mein band (Protected!)
#    Abstraction:   Aapko sirf SCREEN aur BUTTONS dikhte hain
#                    Circuit board kaise kaam karta hai — hidden!


# ============================================================
# PART 1: WITHOUT ENCAPSULATION (THE PROBLEM)
# ============================================================

print("=" * 60)
print("📊 WITHOUT ENCAPSULATION — DATA UNSAFE")
print("=" * 60)


class BankAccountUnsafe:
    """Unsafe bank account — Koi bhi kuch bhi change kar sakta hai!"""
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance  # Directly accessible!


print("\n🔍 Problem — Direct Access:")
acc = BankAccountUnsafe("Ibrahim", 50000)

print(f"   Initial Balance: Rs. {acc.balance}")

# Koi bhi directly balance change kar sakta hai! DANGEROUS!
acc.balance = -100000  # Negative balance? Invalid!
print(f"   After hack: Rs. {acc.balance}")

acc.balance = "HACKED"  # String bhi set kar sakte hain!
print(f"   After string hack: Rs. {acc.balance}")

print("""
❌ PROBLEMS WITHOUT ENCAPSULATION:
   1. Koi bhi data directly change kar sakta hai
   2. Validation nahi ho sakti
   3. Invalid values set ho sakti hain
   4. Data corrupt ho sakta hai
   5. Security risk!
""")


# ============================================================
# PART 2: ACCESS MODIFIERS IN PYTHON
# ============================================================

print("=" * 60)
print("📊 ACCESS MODIFIERS IN PYTHON")
print("=" * 60)

print("""
PYTHON MEIN 3 TYPES:

1️⃣  PUBLIC (No Underscore)
    self.name = "Ibrahim"
    → Kahi bhi access kar sakte hain
    → Sabke liye open!

2️⃣  PROTECTED (Single Underscore _)
    self._salary = 50000
    → CONVENTION: "Ise bahar se access mat karo"
    → Phir bhi access kar sakte hain (Python rokta nahi!)
    → Sirf WARNING hai — "Bhai, ye internal hai!"

3️⃣  PRIVATE (Double Underscore __)
    self.__pin = 1234
    → Name Mangling hota hai
    → Bahar se directly access NAHI kar sakte!
    → Python name change kar deta hai (_ClassName__pin)
    → STRONG protection!


⚠️  IMPORTANT:
Python mein Java/C++ jaisa STRICT private NAHI hai!
Sab kuch CONVENTION based hai.
"We are all consenting adults here" — Python Philosophy
""")


# ============================================================
# PART 3: ENCAPSULATION — COMPLETE EXAMPLE
# ============================================================

print("=" * 60)
print("📊 ENCAPSULATION — SAFE BANK ACCOUNT")
print("=" * 60)


class BankAccount:
    """Encapsulated Bank Account — Data Protected!"""
    
    def __init__(self, holder, initial_balance, pin):
        self.holder = holder              # PUBLIC — Sab dekh sakte hain
        self._bank_name = "Python Bank"   # PROTECTED — Internal use
        self.__balance = initial_balance  # PRIVATE — Bahar se access NAHI!
        self.__pin = pin                  # PRIVATE — Secret!
        self._account_type = "Savings"    # PROTECTED
    
    # GETTER — Balance dekhne ke liye (Read access)
    def get_balance(self, pin):
        """Balance check karo — PIN zaroori hai!"""
        if self.__verify_pin(pin):
            return f"💰 Balance: Rs. {self.__balance}"
        return "❌ Wrong PIN! Cannot show balance."
    
    # SETTER — Balance change karne ke liye (Controlled access)
    def deposit(self, amount):
        """Paise jama karo — Validation ke saath!"""
        if amount > 0:
            self.__balance += amount
            return f"✅ Deposited Rs. {amount}. New Balance: Rs. {self.__balance}"
        return "❌ Amount must be positive!"
    
    def withdraw(self, amount, pin):
        """Paise nikalo — PIN aur balance check ke saath!"""
        if not self.__verify_pin(pin):
            return "❌ Wrong PIN! Cannot withdraw."
        if amount <= 0:
            return "❌ Amount must be positive!"
        if amount > self.__balance:
            return f"❌ Insufficient balance! You have Rs. {self.__balance}"
        
        self.__balance -= amount
        return f"✅ Withdrawn Rs. {amount}. Remaining: Rs. {self.__balance}"
    
    # PRIVATE METHOD — Sirf class ke andar use hoga!
    def __verify_pin(self, pin):
        """PIN verify karo — Bahar se call NAHI kar sakte!"""
        return self.__pin == pin
    
    # PROTECTED METHOD — Convention: internal use
    def _calculate_interest(self):
        """Interest calculate karo — Internal method."""
        return self.__balance * 0.05  # 5% interest
    
    def apply_interest(self):
        """Public method jo protected method use karega."""
        interest = self._calculate_interest()
        self.__balance += interest
        return f"✅ Interest applied: Rs. {interest}. New Balance: Rs. {self.__balance}"


print("\n🔍 Safe Bank Account Operations:")

# Account create
acc = BankAccount("Ibrahim", 50000, 1234)

# Public attribute — Direct access OK
print(f"   Holder: {acc.holder}")
print(f"   Bank: {acc._bank_name}")  # Protected — Access kar sakte hain (but avoid!)

# Private attribute — DIRECT ACCESS FAIL!
try:
    print(acc.__balance)  # AttributeError!
except AttributeError as e:
    print(f"   ❌ Cannot access private: {e}")

# Name mangling se access kar sakte hain (BUT DON'T DO THIS!)
print(f"   ⚠️  Name mangled: {acc._BankAccount__balance}")  # Possible but WRONG!

# Proper way — Getters/Setters
print(f"\n   {acc.get_balance(1234)}")       # Sahi PIN
print(f"   {acc.get_balance(0000)}")         # Galat PIN

print(f"\n   {acc.deposit(10000)}")
print(f"   {acc.deposit(-5000)}")            # Invalid!

print(f"\n   {acc.withdraw(20000, 1234)}")   # Sahi PIN
print(f"   {acc.withdraw(5000, 0000)}")      # Galat PIN

print(f"\n   {acc.apply_interest()}")


# ============================================================
# PART 4: PROPERTY DECORATOR (@property)
# ============================================================

print("\n" + "=" * 60)
print("📊 @property DECORATOR — PYTHONIC WAY")
print("=" * 60)

print("""
@property = Getter/Setter/Deleter ko CLEAN tarah se define karna.
Method ki tarah call nahi, ATTRIBUTE ki tarah access karo!

BINA @property:
    obj.get_name()     ← Method call jaisa
    obj.set_name("X")  ← Method call jaisa

@property KE SAATH:
    obj.name           ← Attribute jaisa (Clean!)
    obj.name = "X"     ← Attribute jaisa (Clean!)
""")


class Student:
    """Student class with @property."""
    
    def __init__(self, name, age, marks):
        self.__name = name
        self.__age = age
        self.__marks = marks
    
    # GETTER — @property
    @property
    def name(self):
        """Name get karo."""
        return self.__name
    
    # SETTER — @name.setter
    @name.setter
    def name(self, value):
        """Name set karo — validation ke saath!"""
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters!")
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150!")
        self.__age = value
    
    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100!")
        self.__marks = value
    
    @property
    def grade(self):
        """Read-only property — Calculated, no setter!"""
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "F"
    
    @property
    def info(self):
        """Computed property."""
        return f"{self.__name} (Age: {self.__age}) — Marks: {self.__marks}, Grade: {self.grade}"


print("\n🔍 Student with @property:")

student = Student("Ibrahim", 22, 95)

# Attribute ki tarah access! (Method call nahi!)
print(f"   Name: {student.name}")       # Getter
print(f"   Age: {student.age}")          # Getter
print(f"   Marks: {student.marks}")      # Getter
print(f"   Grade: {student.grade}")      # Read-only
print(f"   Info: {student.info}")

# Attribute ki tarah SET bhi! (Method call nahi!)
student.name = "Shaikh Ibrahim"  # Setter with validation
student.age = 23
student.marks = 98

print(f"\n   After Update:")
print(f"   {student.info}")

# Validation check
try:
    student.age = -5  # Invalid!
except ValueError as e:
    print(f"   ❌ Error: {e}")


# ============================================================
# PART 5: ABSTRACTION — HIDE COMPLEXITY
# ============================================================

print("\n" + "=" * 60)
print("📊 ABSTRACTION — COMPLEXITY HIDE KARO")
print("=" * 60)

print("""
ABSTRACTION KA RULE:
"WHAT it does" dikhao, "HOW it does" chhupao!

Simple words:
User ko sirf BUTTONS dikhao, internal wiring mat dikhao!
""")


from abc import ABC, abstractmethod

# Abstract Class — Ye instantiate nahi ho sakti!
class Vehicle(ABC):
    """Abstract Vehicle Class — Sirf template!"""
    
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        """Ye method har child mein HONA HI HOGA!"""
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def info(self):
        """Concrete method — Sab children use kar sakte hain."""
        return f"🚗 {self.brand}"
    
    def fuel_up(self):
        """Concrete method."""
        return "⛽ Fueling up..."


class Car(Vehicle):
    """Car MUST implement start() and stop()!"""
    
    def start(self):
        return f"🚗 {self.brand}: Insert key → Turn → Engine ON!"
    
    def stop(self):
        return f"🛑 {self.brand}: Turn key → Engine OFF!"


class Tesla(Vehicle):
    """Tesla MUST implement start() and stop()!"""
    
    def start(self):
        return f"🔌 {self.brand}: Press brake → Push button → Silent start!"
    
    def stop(self):
        return f"🔋 {self.brand}: Push button → Auto park!"


class Bike(Vehicle):
    """Bike MUST implement start() and stop()!"""
    
    def start(self):
        return f"🏍️  {self.brand}: Kick start → Brap Brap!"
    
    def stop(self):
        return f"🛑 {self.brand}: Kill switch → Engine OFF!"


# Cannot instantiate abstract class!
# vehicle = Vehicle("Generic")  # TypeError!

print("\n🔍 Vehicles — Abstraction in Action:")
vehicles = [Car("Toyota"), Tesla("Tesla"), Bike("Honda")]

for v in vehicles:
    print(f"   {v.info()}")
    print(f"   {v.start()}")
    print(f"   {v.stop()}")
    print(f"   {v.fuel_up()}")  # Common method from abstract class
    print()


# ============================================================
# PART 6: REAL LIFE EXAMPLE — ATM MACHINE
# ============================================================

print("=" * 60)
print("📊 REAL LIFE: ATM MACHINE")
print("=" * 60)


class ATM:
    """ATM Machine — Encapsulation + Abstraction together!"""
    
    def __init__(self):
        self.__accounts = {  # Private database (Encapsulated!)
            "1234": {"name": "Ibrahim", "balance": 50000},
            "5678": {"name": "Ali", "balance": 30000},
        }
        self.__current_user = None
    
    # PUBLIC methods (Abstraction — Simple interface!)
    def insert_card(self, pin):
        """Card insert karo."""
        if pin in self.__accounts:
            self.__current_user = pin
            return f"✅ Welcome, {self.__accounts[pin]['name']}!"
        return "❌ Invalid PIN!"
    
    def check_balance(self):
        """Balance check karo."""
        if self.__current_user:
            balance = self.__accounts[self.__current_user]['balance']
            return f"💰 Balance: Rs. {balance}"
        return "❌ Please insert card first!"
    
    def withdraw(self, amount):
        """Paise nikalo."""
        if not self.__current_user:
            return "❌ Please insert card first!"
        
        if amount > self.__accounts[self.__current_user]['balance']:
            return "❌ Insufficient balance!"
        
        self.__accounts[self.__current_user]['balance'] -= amount
        return f"✅ Withdrawn Rs. {amount}. Remaining: Rs. {self.__accounts[self.__current_user]['balance']}"
    
    def deposit(self, amount):
        """Paise jama karo."""
        if not self.__current_user:
            return "❌ Please insert card first!"
        
        self.__accounts[self.__current_user]['balance'] += amount
        return f"✅ Deposited Rs. {amount}. New Balance: Rs. {self.__accounts[self.__current_user]['balance']}"
    
    def eject_card(self):
        """Card nikalo."""
        if self.__current_user:
            name = self.__accounts[self.__current_user]['name']
            self.__current_user = None
            return f"👋 Goodbye, {name}! Card ejected."
        return "No card inserted."


print("\n🔍 ATM Operations:")
atm = ATM()

print(f"   {atm.insert_card('1234')}")
print(f"   {atm.check_balance()}")
print(f"   {atm.withdraw(10000)}")
print(f"   {atm.deposit(5000)}")
print(f"   {atm.check_balance()}")
print(f"   {atm.eject_card()}")

# User ko pata bhi nahi ke andar kya ho raha hai!
# Sirf simple methods use kar raha hai — ABSTRACTION!
# Internal data safe hai — ENCAPSULATION!


# ============================================================
# PART 7: ENCAPSULATION vs ABSTRACTION
# ============================================================

print("\n" + "=" * 60)
print("📊 ENCAPSULATION vs ABSTRACTION")
print("=" * 60)

print("""
┌──────────────────┬─────────────────────────┬──────────────────────────┐
│ Feature          │ Encapsulation           │ Abstraction              │
├──────────────────┼─────────────────────────┼──────────────────────────┤
│ Focus            │ HOW to hide             │ WHAT to show             │
│ Goal             │ Data Protection         │ Complexity Reduction     │
│ Method           │ Private attributes      │ Abstract classes/methods │
│ Access Modifiers │ Public, Protected,      │ ABC, @abstractmethod     │
│                  │ Private                  │                          │
│ Real Life        │ ATM ke andar ka safe    │ ATM ke buttons           │
│                  │ (Data locked!)           │ (Simple interface!)      │
└──────────────────┴─────────────────────────┴──────────────────────────┘

SIMPLE YAAD RAKHO:
🔒 Encapsulation = DATA ko lock karo (Private, Protected)
🎭 Abstraction  = COMPLEXITY chhupao (Simple interface dikhao)
""")


# ============================================================
# PART 8: COMPLETE SUMMARY
# ============================================================

print("=" * 60)
print("📊 COMPLETE SUMMARY — ENCAPSULATION & ABSTRACTION")
print("=" * 60)

print("""
✅ ENCAPSULATION:
   • Data hiding — Bahar se direct access NAHI!
   • Getters/Setters se controlled access
   • Validation possible (Invalid data block)
   • Python: Convention based (Public, _Protected, __Private)

✅ ACCESS MODIFIERS:
   • self.name        → PUBLIC (Open)
   • self._name       → PROTECTED (Warning: Internal)
   • self.__name      → PRIVATE (Name mangling)

✅ @property DECORATOR:
   • Clean getter/setter syntax
   • Attribute ki tarah access (obj.name, not obj.get_name())
   • Read-only properties possible
   • Validation easy

✅ ABSTRACTION:
   • Complexity hide karna
   • Sirf zaroori features dikhana
   • Abstract Base Class (ABC)
   • @abstractmethod decorator

✅ ABC (Abstract Base Class):
   • from abc import ABC, abstractmethod
   • Abstract class instantiate NAHI ho sakti!
   • Child MUST implement abstract methods
   • Template for other classes

✅ REAL LIFE USE:
   • ATM Machine (Encapsulation + Abstraction)
   • Bank Account (Private balance)
   • Car Dashboard (Complexity hidden)
   • Payment Gateway (Simple interface)

✅ GOLDEN RULES:
   • Private attributes: __ use karo (Name mangling)
   • Protected attributes: _ use karo (Convention)
   • Getters/Setters se data validate karo
   • @property pythonic way hai
   • Abstract class = Template, instantiate nahi!
""")