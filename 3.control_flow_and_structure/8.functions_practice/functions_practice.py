# ============================================================
# 5 REAL LIFE FUNCTIONS — Beginner Friendly
# ============================================================
# Har function ek real life problem solve karta hai
# Step-by-step explanation ke saath
# ============================================================


# ============================================================
# FUNCTION 1: BILL CALCULATOR (Restaurant)
# ============================================================
# Problem: Restaurant ka bill calculate karna
# Input: Item price, Quantity
# Output: Total bill with tax

print("=" * 60)
print("🧾 FUNCTION 1: RESTAURANT BILL CALCULATOR")
print("=" * 60)


def calculate_bill(item_name, price, quantity):
    """
    Restaurant ka bill calculate karta hai.
    
    Steps:
    1. Subtotal nikalo (price × quantity)
    2. Tax calculate karo (10% of subtotal)
    3. Final total nikalo (subtotal + tax)
    """
    
    # Step 1: Subtotal
    subtotal = price * quantity
    
    # Step 2: Tax (10%)
    tax = subtotal * 0.10
    
    # Step 3: Final Total
    total = subtotal + tax
    
    # Bill print karo
    print(f"\n📋 BILL FOR {item_name.upper()}:")
    print(f"   Item:      {item_name}")
    print(f"   Price:     Rs. {price}")
    print(f"   Quantity:  {quantity}")
    print(f"   Subtotal:  Rs. {subtotal}")
    print(f"   Tax (10%): Rs. {tax:.2f}")
    print(f"   ─────────────────")
    print(f"   TOTAL:     Rs. {total:.2f}")
    
    return total


# Function Call
bill1 = calculate_bill("Biryani", 250, 2)
bill2 = calculate_bill("Pizza", 500, 1)
bill3 = calculate_bill("Cold Drink", 80, 3)

print(f"\n💰 Total for all items: Rs. {bill1 + bill2 + bill3:.2f}")


print("\n" + "=" * 60)


# ============================================================
# FUNCTION 2: BMI CALCULATOR (Health)
# ============================================================
# Problem: Body Mass Index calculate karna
# Input: Weight (kg), Height (feet)
# Output: BMI with health category

print("\n⚕️  FUNCTION 2: BMI CALCULATOR")
print("=" * 60)


def calculate_bmi(name, weight_kg, height_feet):
    """
    BMI (Body Mass Index) calculate karta hai.
    
    Formula:
    1. Height ko feet se meters mein convert karo
    2. BMI = weight / (height × height)
    3. Category batana
    
    Note: 1 foot = 0.3048 meters
    """
    
    # Step 1: Height conversion (feet → meters)
    height_meters = height_feet * 0.3048
    
    # Step 2: BMI formula
    bmi = weight_kg / (height_meters ** 2)
    
    # Step 3: Category decide karo
    if bmi < 18.5:
        category = "Underweight ⚠️"
        advice = "Thoda weight badhao, healthy khao!"
    elif bmi < 25:
        category = "Normal ✅"
        advice = "Perfect! Aise hi maintain karo!"
    elif bmi < 30:
        category = "Overweight ⚠️"
        advice = "Exercise karo, diet control karo!"
    else:
        category = "Obese ❌"
        advice = "Doctor se consult karo!"
    
    # Result print karo
    print(f"\n📊 BMI REPORT FOR {name.upper()}:")
    print(f"   Weight:  {weight_kg} kg")
    print(f"   Height:  {height_feet} feet ({height_meters:.2f} meters)")
    print(f"   BMI:     {bmi:.1f}")
    print(f"   Status:  {category}")
    print(f"   💡 {advice}")
    
    return bmi


# Function Call
bmi1 = calculate_bmi("Ibrahim", 70, 5.8)
bmi2 = calculate_bmi("Ali", 85, 5.6)
bmi3 = calculate_bmi("Sara", 50, 5.4)


print("\n" + "=" * 60)


# ============================================================
# FUNCTION 3: ELECTRICITY BILL CALCULATOR
# ============================================================
# Problem: Bijli ka bill calculate karna
# Input: Units consumed
# Output: Total bill with tax

print("\n⚡ FUNCTION 3: ELECTRICITY BILL CALCULATOR")
print("=" * 60)


def calculate_electricity_bill(name, units):
    """
    Electricity bill calculate karta hai.
    
    Rate per unit:
    • 1-100 units:   Rs. 10 per unit
    • 101-200 units:  Rs. 15 per unit
    • 201+ units:     Rs. 20 per unit
    
    Additional:
    • Fixed charges: Rs. 100
    • Tax: 17% on total
    """
    
    # Step 1: Calculate based on slab
    if units <= 100:
        rate = 10
        cost = units * rate
        slab = "Low (1-100)"
    elif units <= 200:
        rate = 15
        cost = units * rate
        slab = "Medium (101-200)"
    else:
        rate = 20
        cost = units * rate
        slab = "High (201+)"
    
    # Step 2: Fixed charges
    fixed_charges = 100
    
    # Step 3: Tax (17%)
    subtotal = cost + fixed_charges
    tax = subtotal * 0.17
    
    # Step 4: Final total
    total = subtotal + tax
    
    # Bill print karo
    print(f"\n🧾 ELECTRICITY BILL — {name.upper()}:")
    print(f"   Units Consumed:  {units}")
    print(f"   Rate Slab:       {slab} (@ Rs. {rate}/unit)")
    print(f"   Energy Cost:     Rs. {cost}")
    print(f"   Fixed Charges:   Rs. {fixed_charges}")
    print(f"   Tax (17%):       Rs. {tax:.2f}")
    print(f"   ─────────────────────")
    print(f"   TOTAL BILL:      Rs. {total:.2f}")
    
    # Warning agar units zyada hain
    if units > 300:
        print(f"   ⚠️  HIGH USAGE! Bill reduce karne ke liye bijli bachao!")
    
    return total


# Function Call
bill1 = calculate_electricity_bill("Ibrahim", 80)
bill2 = calculate_electricity_bill("Ali", 150)
bill3 = calculate_electricity_bill("Sara", 350)


print("\n" + "=" * 60)


# ============================================================
# FUNCTION 4: STUDENT REPORT CARD
# ============================================================
# Problem: Student ka report card generate karna
# Input: Student name, marks of 3 subjects
# Output: Complete report card with grade

print("\n📚 FUNCTION 4: STUDENT REPORT CARD")
print("=" * 60)


def generate_report_card(name, english, math, python):
    """
    Student ka report card generate karta hai.
    
    Steps:
    1. Total marks calculate karo
    2. Percentage nikalo
    3. Grade assign karo
    4. Report print karo
    """
    
    # Step 1: Total and Percentage
    total_marks = english + math + python
    max_marks = 300
    percentage = (total_marks / max_marks) * 100
    
    # Step 2: Grade Assignment
    if percentage >= 90:
        grade = "A+"
        remark = "🏆 Outstanding!"
    elif percentage >= 80:
        grade = "A"
        remark = "⭐ Excellent!"
    elif percentage >= 70:
        grade = "B"
        remark = "👍 Good!"
    elif percentage >= 60:
        grade = "C"
        remark = "📝 Average"
    elif percentage >= 50:
        grade = "D"
        remark = "⚠️ Need Improvement"
    else:
        grade = "F"
        remark = "❌ Fail — Try Again!"
    
    # Step 3: Print Report Card
    print(f"\n{'=' * 40}")
    print(f"📊 REPORT CARD — {name.upper()}")
    print(f"{'=' * 40}")
    print(f"   Subject         Marks   Status")
    print(f"   ─────────────────────────────")
    
    # English status
    eng_status = "✅ Pass" if english >= 50 else "❌ Fail"
    print(f"   English         {english:3}/100  {eng_status}")
    
    # Math status
    math_status = "✅ Pass" if math >= 50 else "❌ Fail"
    print(f"   Mathematics     {math:3}/100  {math_status}")
    
    # Python status
    py_status = "✅ Pass" if python >= 50 else "❌ Fail"
    print(f"   Python          {python:3}/100  {py_status}")
    
    print(f"   ─────────────────────────────")
    print(f"   Total:          {total_marks}/300")
    print(f"   Percentage:     {percentage:.2f}%")
    print(f"   Grade:          {grade}")
    print(f"   Remark:         {remark}")
    print(f"{'=' * 40}")
    
    # Bonus: Pass/Fail check
    if english >= 50 and math >= 50 and python >= 50:
        print(f"   🎉 CONGRATULATIONS! Aap PASS hain!")
    else:
        failed_subjects = []
        if english < 50:
            failed_subjects.append("English")
        if math < 50:
            failed_subjects.append("Mathematics")
        if python < 50:
            failed_subjects.append("Python")
        print(f"   😔 FAIL in: {', '.join(failed_subjects)}")
    
    return percentage, grade


# Function Call
result1 = generate_report_card("Ibrahim", 85, 92, 78)
result2 = generate_report_card("Ali", 45, 55, 62)
result3 = generate_report_card("Sara", 95, 88, 91)


print("\n" + "=" * 60)


# ============================================================
# FUNCTION 5: ZAKAT CALCULATOR
# ============================================================
# Problem: Zakat calculate karna
# Input: Total savings, Gold, Silver value
# Output: Zakat amount

print("\n🕌 FUNCTION 5: ZAKAT CALCULATOR")
print("=" * 60)


def calculate_zakat(name, savings, gold_value, silver_value):
    """
    Zakat calculate karta hai.
    
    Islamic Rules:
    • Zakat = 2.5% of total wealth
    • Nisab = 7.5 tola gold ya 52.5 tola silver
    
    Steps:
    1. Total wealth calculate karo
    2. Check karo ke nisab ke barabar hai ya nahi
    3. Agar haan, to 2.5% calculate karo
    """
    
    # Step 1: Total Wealth
    total_wealth = savings + gold_value + silver_value
    
    # Step 2: Nisab Check (Gold: Rs. 200,000 per tola × 7.5)
    gold_per_tola = 200000  # Approximate
    nisab = gold_per_tola * 7.5
    
    # Step 3: Zakat Calculation
    zakat_rate = 0.025  # 2.5%
    
    if total_wealth >= nisab:
        zakat_amount = total_wealth * zakat_rate
        eligible = True
    else:
        zakat_amount = 0
        eligible = False
    
    # Print Report
    print(f"\n🕌 ZAKAT CALCULATION — {name.upper()}:")
    print(f"   ─────────────────────────────")
    print(f"   Savings:        Rs. {savings:,.2f}")
    print(f"   Gold Value:     Rs. {gold_value:,.2f}")
    print(f"   Silver Value:   Rs. {silver_value:,.2f}")
    print(f"   ─────────────────────────────")
    print(f"   Total Wealth:   Rs. {total_wealth:,.2f}")
    print(f"   Nisab (Gold):   Rs. {nisab:,.2f}")
    print(f"   ─────────────────────────────")
    
    if eligible:
        print(f"   ✅ ZAKAT ELIGIBLE")
        print(f"   Zakat Rate:     2.5%")
        print(f"   ZAKAT AMOUNT:   Rs. {zakat_amount:,.2f}")
        print(f"   💡 Pay your Zakat to deserving people!")
    else:
        print(f"   ❌ NOT ELIGIBLE for Zakat")
        print(f"   Shortfall:      Rs. {nisab - total_wealth:,.2f}")
        print(f"   💡 Save more to reach Nisab!")
    
    return zakat_amount


# Function Call
zakat1 = calculate_zakat("Ibrahim", 500000, 300000, 50000)
zakat2 = calculate_zakat("Ali", 50000, 100000, 20000)
zakat3 = calculate_zakat("Sara", 1000000, 500000, 100000)


# ============================================================
# BONUS: ALL FUNCTIONS TOGETHER
# ============================================================

print("\n\n" + "=" * 60)
print("🎯 BONUS: CALLING ALL FUNCTIONS")
print("=" * 60)

print("""
Above 5 functions cover:
   🧾  Restaurant Billing
   ⚕️   Health (BMI)
   ⚡  Utility Billing (Electricity)
   📚  Education (Report Card)
   🕌  Islamic Finance (Zakat)

Each function:
   ✅ Takes INPUT (Parameters)
   ✅ Does PROCESSING (Calculation)
   ✅ Shows OUTPUT (Print + Return)
   ✅ Has DOCUMENTATION (Docstring)
   ✅ Is REUSABLE (Call multiple times)
""")


# ============================================================
# PRACTICE EXERCISES
# ============================================================

print("=" * 60)
print("📝 PRACTICE EXERCISES — TRY YOURSELF!")
print("=" * 60)

print("""
1. Petrol Cost Calculator
   → Input: Distance (km), Mileage (km/liter), Petrol price
   → Output: Total cost of trip
   
   Hint: def petrol_cost(distance, mileage, price_per_liter):


2. Age Calculator
   → Input: Birth year
   → Output: Current age
   
   Hint: def calculate_age(birth_year):


3. Simple Interest Calculator
   → Input: Principal, Rate, Time
   → Output: Simple Interest
   
   Formula: SI = (P × R × T) / 100
   Hint: def simple_interest(principal, rate, time):


4. Temperature Converter
   → Input: Celsius
   → Output: Fahrenheit
   
   Formula: F = (C × 9/5) + 32
   Hint: def celsius_to_fahrenheit(celsius):


5. Discount Calculator
   → Input: Original price, Discount percentage
   → Output: Final price after discount
   
   Hint: def apply_discount(price, discount_percent):
""")


# ============================================================
# SOLUTION: Practice Exercise 1
# ============================================================

print("=" * 60)
print("✅ SOLUTION 1: PETROL COST CALCULATOR")
print("=" * 60)


def petrol_cost(distance, mileage, price_per_liter):
    """
    Trip ka petrol cost calculate karta hai.
    
    Formula:
    Petrol needed = Distance / Mileage
    Total cost = Petrol needed × Price per liter
    """
    petrol_needed = distance / mileage
    total_cost = petrol_needed * price_per_liter
    
    print(f"\n🚗 TRIP COST:")
    print(f"   Distance:      {distance} km")
    print(f"   Mileage:       {mileage} km/liter")
    print(f"   Petrol Price:  Rs. {price_per_liter}/liter")
    print(f"   Petrol Needed: {petrol_needed:.2f} liters")
    print(f"   ─────────────────────────")
    print(f"   TOTAL COST:    Rs. {total_cost:.2f}")
    
    return total_cost


# Test
trip1 = petrol_cost(200, 15, 280)  # 200 km, 15 km/l, Rs. 280/liter
trip2 = petrol_cost(500, 12, 280)  # 500 km, 12 km/l, Rs. 280/liter