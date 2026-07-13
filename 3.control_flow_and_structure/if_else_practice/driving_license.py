# 🚗 Driving License Check
# Real Life Scenario: Driving License Eligibility

# Pakistan mein driving license ke liye minimum age 18 years hai.
# Ye program check karega ke aap driving license ke liye eligible hain ya nahi.

print("=" * 40)
print("🚗 DRIVING LICENSE ELIGIBILITY CHECK")
print("=" * 40)

# User se age input lena
age = int(input("Enter Your Age: "))

print("\nChecking eligibility...\n")

# Condition check
if age >= 18:
    print("✅ Congratulations!")
    print("Aap driving license ke liye ELIGIBLE hain.")
    print("Aap nearest driving license center ja sakte hain.")
    
    # Bonus: Additional categories
    if age >= 50:
        print("📋 Note: Aap senior citizen category mein aate hain.")
        print("   Medical checkup zaroori hoga.")
elif age >= 16:
    print("⚠️ Aap abhi 16-17 saal ke hain.")
    print("Aap MOTORCYCLE (70cc) learning permit le sakte hain.")
    print("Car license ke liye 18 saal ka hona zaroori hai.")
else:
    print("❌ Sorry!")
    print("Aap abhi driving license ke liye ELIGIBLE NAHI hain.")
    print(f"Aapko abhi {18 - age} saal aur intezaar karna hoga.")

print("\nThank you for using Driving License Checker! 🚦")