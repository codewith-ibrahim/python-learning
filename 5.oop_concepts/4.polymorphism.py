# Polymorphism in Python

# Polymorphism kya hota hai?
#
# Poly = Many (Bahut saare)
# Morph = Forms (Roop)
# Polymorphism = Many Forms (Ek cheez ke kai roop)
#
# Simple Definition:
# Ek hi METHOD ya OPERATOR different objects ke liye
# DIFFERENT tarah se kaam karta hai.
#
# Real Life Analogy:
# 🏏 Ek aadmi:
#    Ghar mein → Baap hai
#    Office mein → Boss hai
#    School mein → Teacher hai
#    Wife ke saamne → Husband hai
#
# Same person, DIFFERENT roles = POLYMORPHISM!


# ============================================================
# PART 1: TYPES OF POLYMORPHISM
# ============================================================

print("=" * 60)
print("📊 TYPES OF POLYMORPHISM IN PYTHON")
print("=" * 60)

print("""
PYTHON MEIN 4 TYPES:

1️⃣  DUCK TYPING
    "If it walks like a duck and quacks like a duck,
     it must be a duck!"
    Agar object ke paas required method hai, to use karo!

2️⃣  METHOD OVERRIDING
    Child class parent ke method ko apne hisaab se
    change kare (Inheritance mein dekha tha)

3️⃣  METHOD OVERLOADING (Python mein DIFFERENT hai!)
    Same method name, DIFFERENT parameters
    Python directly support NAHI karta!

4️⃣  OPERATOR OVERLOADING
    Operators (+, -, *, etc.) ko apne hisaab se
    kaam karne dena (Dunder methods se)
""")


# ============================================================
# PART 2: DUCK TYPING
# ============================================================

print("=" * 60)
print("📊 DUCK TYPING — SABSE IMPORTANT")
print("=" * 60)

print("""
DUCK TYPING KA RULE:
"Type matter nahi karta, BEHAVIOR matter karta hai!"

Agar ek object ke paas required METHOD hai,
to wo object us kaam ke liye USE ho sakta hai,
chahe wo kis bhi class ka kyun na ho!

Simple words mein:
Agar wo鸭子 ki tarah chalta hai aur鸭子 ki tarah bolta hai,
to wo鸭子 hi hai! (Chahe wo鸭子 na bhi ho!)
""")


class Duck:
    def speak(self):
        return "🦆 Quack Quack!"
    
    def move(self):
        return "🦆 Waddling..."


class Dog:
    def speak(self):
        return "🐕 Woof Woof!"
    
    def move(self):
        return "🐕 Running..."


class Cat:
    def speak(self):
        return "🐱 Meow Meow!"
    
    def move(self):
        return "🐱 Sneaking..."


class Human:
    def speak(self):
        return "👤 Hello! Assalam O Alaikum!"
    
    def move(self):
        return "👤 Walking on two legs..."
    
    def code(self):  # Extra method sirf Human ke paas
        return "💻 Writing Python code..."


# Polymorphic Function — Kisi bhi object ke saath kaam karega!
def animal_show(animal):
    """Ye function kisi bhi animal object ke saath kaam karega!"""
    print(f"   {animal.speak():30} | {animal.move()}")


print("\n🔍 Animal Show — Sab ek hi function se chalenge:")
print("-" * 60)

animals = [Duck(), Dog(), Cat(), Human()]

for animal in animals:
    animal_show(animal)
    # Dekho! Ek hi function sab objects ke liye kaam kar raha hai!
    # Yeh POLYMORPHISM hai!


# ============================================================
# PART 3: METHOD OVERRIDING
# ============================================================

print("\n" + "=" * 60)
print("📊 METHOD OVERRIDING")
print("=" * 60)

print("""
Method Overriding = Child class parent ke method ko
APNE HISAB SE badal de!

Parent ka method = Default
Child ka method = Custom (Override!)
""")


class Vehicle:
    """Parent Class."""
    def start(self):
        return "🔑 Vehicle starting..."
    
    def stop(self):
        return "🛑 Vehicle stopping..."
    
    def fuel_type(self):
        return "⛽ Unknown fuel"


class Car(Vehicle):
    def start(self):
        return "🚗 Car: Push button start! Vroom Vroom!"
    
    def fuel_type(self):
        return "⛽ Petrol/Diesel"


class ElectricCar(Vehicle):
    def start(self):
        return "🔌 Electric Car: Silent start... Ready!"
    
    def stop(self):
        return "🔋 Electric Car: Regenerative braking..."
    
    def fuel_type(self):
        return "⚡ Electric (Battery)"


class Bike(Vehicle):
    def start(self):
        return "🏍️  Bike: Kick start! Brap Brap!"
    
    def fuel_type(self):
        return "⛽ Petrol"


print("\n🔍 Vehicles — Same method, different behavior:")
vehicles = [Car(), ElectricCar(), Bike()]

for v in vehicles:
    print(f"   {v.start()}")
    print(f"   {v.fuel_type()}")
    print()


# ============================================================
# PART 4: METHOD OVERLOADING (PYTHON STYLE)
# ============================================================

print("=" * 60)
print("📊 METHOD OVERLOADING IN PYTHON")
print("=" * 60)

print("""
⚠️  IMPORTANT:
Python TRADITIONAL method overloading SUPPORT NAHI karta!
(Jaise Java/C++ mein hota hai)

Python mein ek hi naam ke do methods nahi ho sakte.
Lekin DEFAULT ARGUMENTS aur *args se same kaam kar sakte hain!
""")


# Python Style Overloading — Default Arguments
class Calculator:
    """Method Overloading using Default Arguments."""
    
    # Traditional overloading (Java/C++ style) — PYTHON MEIN NAHI CHALEGA!
    # def add(self, a, b):
    #     return a + b
    # def add(self, a, b, c):     ← Ye previous add() ko OVERWRITE kar dega!
    #     return a + b + c
    
    # Python Way — Default Arguments
    def add(self, a, b, c=0, d=0):
        """2, 3, ya 4 numbers add kar sakte hain!"""
        return a + b + c + d
    
    def multiply(self, *args):
        """Kitne bhi numbers multiply kar sakte hain!"""
        result = 1
        for num in args:
            result *= num
        return result
    
    def greet(self, name, greeting="Hello"):
        """Default greeting hai, change bhi kar sakte hain."""
        return f"{greeting}, {name}!"


print("\n🔍 Calculator — Python Style Overloading:")
calc = Calculator()

print(f"   add(5, 3)        = {calc.add(5, 3)}")           # 2 args
print(f"   add(5, 3, 2)     = {calc.add(5, 3, 2)}")        # 3 args
print(f"   add(5, 3, 2, 1)  = {calc.add(5, 3, 2, 1)}")     # 4 args

print(f"\n   multiply(2, 3)     = {calc.multiply(2, 3)}")
print(f"   multiply(2, 3, 4)  = {calc.multiply(2, 3, 4)}")

print(f"\n   {calc.greet('Ibrahim')}")
print(f"   {calc.greet('Ibrahim', 'Assalam O Alaikum')}")


# ============================================================
# PART 5: OPERATOR OVERLOADING (DUNDER METHODS)
# ============================================================

print("\n" + "=" * 60)
print("📊 OPERATOR OVERLOADING")
print("=" * 60)

print("""
Operator Overloading = Operators (+, -, *, /, etc.) ko
APNE CUSTOM OBJECTS ke liye define karna!

Dunder Methods (Double UNDERscore):
__add__  → + operator
__sub__  → - operator
__mul__  → * operator
__truediv__ → / operator
__str__  → print() ke liye string
__len__  → len() function
__eq__   → == operator
__gt__   → > operator
""")


class Vector:
    """2D Vector — Operator Overloading Example."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # + Operator (Addition)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # - Operator (Subtraction)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # * Operator (Scalar Multiplication)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # == Operator (Equality Check)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # > Operator (Greater Than — Magnitude compare)
    def __gt__(self, other):
        return (self.x**2 + self.y**2) > (other.x**2 + other.y**2)
    
    # str() / print() ke liye
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # len() ke liye
    def __len__(self):
        return 2  # 2D vector, always 2 components


print("\n🔍 Vector Operations:")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"   v1 = {v1}")
print(f"   v2 = {v2}")
print(f"   v1 + v2 = {v1 + v2}")        # __add__ call hua!
print(f"   v1 - v2 = {v1 - v2}")        # __sub__ call hua!
print(f"   v1 * 3  = {v1 * 3}")         # __mul__ call hua!
print(f"   v1 == v2? {v1 == v2}")       # __eq__ call hua!
print(f"   v1 > v2? {v1 > v2}")         # __gt__ call hua!
print(f"   len(v1) = {len(v1)}")        # __len__ call hua!


# Another Example — Money Class
class Money:
    """Money class with operator overloading."""
    
    def __init__(self, rupees, paisa=0):
        self.rupees = rupees
        self.paisa = paisa
        self._normalize()
    
    def _normalize(self):
        """Paisa 100 se zyada ho to rupees mein convert."""
        if self.paisa >= 100:
            self.rupees += self.paisa // 100
            self.paisa = self.paisa % 100
    
    def __add__(self, other):
        return Money(self.rupees + other.rupees, self.paisa + other.paisa)
    
    def __sub__(self, other):
        total1 = self.rupees * 100 + self.paisa
        total2 = other.rupees * 100 + other.paisa
        diff = total1 - total2
        return Money(diff // 100, diff % 100)
    
    def __str__(self):
        return f"Rs. {self.rupees}.{self.paisa:02d}"
    
    def __gt__(self, other):
        return (self.rupees, self.paisa) > (other.rupees, other.paisa)


print("\n\n🔍 Money Operations:")
m1 = Money(50, 75)   # Rs. 50.75
m2 = Money(25, 50)   # Rs. 25.50

print(f"   m1 = {m1}")
print(f"   m2 = {m2}")
print(f"   m1 + m2 = {m1 + m2}")
print(f"   m1 - m2 = {m1 - m2}")
print(f"   m1 > m2? {m1 > m2}")


# ============================================================
# PART 6: REAL LIFE POLYMORPHISM EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("📊 REAL LIFE POLYMORPHISM EXAMPLES")
print("=" * 60)


# Example 1: Notification System
print("\n🔍 1. NOTIFICATION SYSTEM:")
print("-" * 40)

class Email:
    def send(self, message, to):
        return f"📧 Email sent to {to}: {message}"

class SMS:
    def send(self, message, to):
        return f"📱 SMS sent to {to}: {message}"

class WhatsApp:
    def send(self, message, to):
        return f"💬 WhatsApp sent to {to}: {message}"

class PushNotification:
    def send(self, message, to):
        return f"🔔 Push notification to {to}: {message}"


def send_notification(notifier, message, to):
    """Polymorphic function — Kisi bhi notification type ke saath kaam karega!"""
    print(f"   {notifier.send(message, to)}")


# Sab ek hi function se bhej rahe hain!
send_notification(Email(), "Your order is confirmed!", "ibrahim@email.com")
send_notification(SMS(), "OTP: 123456", "03123456789")
send_notification(WhatsApp(), "Meeting at 2 PM", "+923001234567")
send_notification(PushNotification(), "New message received", "device_123")


# Example 2: Payment Gateway
print("\n\n🔍 2. PAYMENT GATEWAY:")
print("-" * 40)

class CreditCard:
    def pay(self, amount):
        return f"💳 Paid Rs. {amount} via Credit Card — 2% tax"

class JazzCash:
    def pay(self, amount):
        return f"📱 Paid Rs. {amount} via JazzCash — No tax"

class PayPal:
    def pay(self, amount):
        return f"🅿️  Paid Rs. {amount} via PayPal — 3% international fee"

class COD:
    def pay(self, amount):
        return f"💵 Pay Rs. {amount} via Cash on Delivery — 0% tax"


def process_payment(method, amount):
    """Polymorphic payment processor!"""
    print(f"   {method.pay(amount)}")


print("\n   Checking out...")
process_payment(CreditCard(), 5000)
process_payment(JazzCash(), 3000)
process_payment(PayPal(), 10000)
process_payment(COD(), 2000)


# Example 3: Shape Area Calculator
print("\n\n🔍 3. SHAPE AREA CALCULATOR:")
print("-" * 40)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def name(self):
        return f"Circle (r={self.radius})"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def name(self):
        return f"Rectangle ({self.length}×{self.width})"

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def name(self):
        return f"Triangle (b={self.base}, h={self.height})"


def calculate_area(shape):
    """Kisi bhi shape ka area calculate karo!"""
    print(f"   {shape.name():30} → Area: {shape.area():.2f}")


shapes = [Circle(5), Rectangle(10, 5), Triangle(8, 4)]
for shape in shapes:
    calculate_area(shape)


# ============================================================
# PART 7: COMPLETE SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("📊 COMPLETE SUMMARY — POLYMORPHISM")
print("=" * 60)

print("""
✅ POLYMORPHISM:
   • Poly + Morph = Many Forms
   • Same interface, different implementations
   • Code flexible aur reusable banta hai

✅ TYPES:
   1. Duck Typing — "If it quacks like a duck..."
   2. Method Overriding — Child changes parent method
   3. Method Overloading — Default args se (Python style)
   4. Operator Overloading — Dunder methods se

✅ DUCK TYPING:
   • Type nahi, BEHAVIOR important hai
   • Agar method exist karta hai, to object use kar sakte hain
   • Python ka sabse powerful feature!

✅ METHOD OVERRIDING:
   • Child parent ke method ko change kare
   • Same name, different behavior
   • Inheritance ke saath use hota hai

✅ OPERATOR OVERLOADING (Dunder Methods):
   • __add__  → +
   • __sub__  → -
   • __mul__  → *
   • __str__  → print()
   • __len__  → len()
   • __eq__   → ==
   • __gt__   → >

✅ REAL LIFE USE:
   • Notification systems (Email/SMS/WhatsApp)
   • Payment gateways (Card/JazzCash/COD)
   • Shape calculators
   • File handlers (TXT/JSON/CSV)

✅ GOLDEN RULES:
   • Duck typing — Python's superpower!
   • Method overriding ke liye inheritance chahiye
   • Operator overloading sensible use karo
   • Don't over-engineer — simple rakho
""")