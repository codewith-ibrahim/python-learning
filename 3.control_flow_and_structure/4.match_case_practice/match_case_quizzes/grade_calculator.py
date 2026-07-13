# ============================================================
# QUICK QUIZ 2: Grade Calculator
# ============================================================
# Write a Python program that asks the user to enter their 
# percentage. Calculate and display the corresponding grade 
# using match-case with guards. Handle invalid percentages 
# (less than 0 or greater than 100) appropriately.
# ============================================================


# ============================================================
# VERSION 1: BEGINNER FRIENDLY
# ============================================================
# Har condition ko alag se check kiya, simple samajh aaye

print("=" * 40)
print("📊 GRADE CALCULATOR (Beginner Version)")
print("=" * 40)

# Step 1: User se percentage lo
percentage = float(input("Enter your percentage: "))

# Step 2: Match-Case se grade decide karo
match percentage:
    case p if p >= 90 and p <= 100:
        # 90 se 100 ke beech
        print("\n📋 Result:")
        print("   Grade: A+")
        print("   Remark: Outstanding! 🏆")
        
    case p if p >= 80 and p < 90:
        # 80 se 89 ke beech
        print("\n📋 Result:")
        print("   Grade: A")
        print("   Remark: Excellent! ⭐")
        
    case p if p >= 70 and p < 80:
        # 70 se 79 ke beech
        print("\n📋 Result:")
        print("   Grade: B")
        print("   Remark: Good! 👍")
        
    case p if p >= 60 and p < 70:
        # 60 se 69 ke beech
        print("\n📋 Result:")
        print("   Grade: C")
        print("   Remark: Average 📝")
        
    case p if p >= 50 and p < 60:
        # 50 se 59 ke beech
        print("\n📋 Result:")
        print("   Grade: D")
        print("   Remark: Need Improvement ⚠️")
        
    case p if p >= 0 and p < 50:
        # 0 se 49 ke beech
        print("\n📋 Result:")
        print("   Grade: F")
        print("   Remark: Fail ❌")
        
    case _:
        # 0 se kam ya 100 se zyada
        print("\n❌ Invalid percentage!")
        print("   Percentage 0 se 100 ke beech hona chahiye.")


print("\n" + "=" * 60)


# ============================================================
# VERSION 2: BETTER VERSION
# ============================================================
# Code compact kiya, variable mein grade store kiya

print("\n📊 GRADE CALCULATOR (Better Version)")
print("=" * 40)

percentage = float(input("Enter your percentage: "))

match percentage:
    case p if 90 <= p <= 100:
        grade, remark = "A+", "🏆 Outstanding!"
    case p if 80 <= p < 90:
        grade, remark = "A", "⭐ Excellent!"
    case p if 70 <= p < 80:
        grade, remark = "B", "👍 Good!"
    case p if 60 <= p < 70:
        grade, remark = "C", "📝 Average"
    case p if 50 <= p < 60:
        grade, remark = "D", "⚠️ Need Improvement"
    case p if 0 <= p < 50:
        grade, remark = "F", "❌ Fail"
    case _:
        grade, remark = "N/A", "Invalid percentage (0-100 only!)"

print(f"\n📋 Result:")
print(f"   Percentage: {percentage}%")
print(f"   Grade:      {grade}")
print(f"   Remark:     {remark}")


print("\n" + "=" * 60)


# ============================================================
# VERSION 3: SENIOR DEV VERSION
# ============================================================
# Function, dictionary mapping, proper validation, docstrings

print("\n📊 GRADE CALCULATOR (Senior Dev Version)")
print("=" * 40)


def get_grade(percentage: float) -> dict:
    """
    Calculate grade based on percentage.
    
    Args:
        percentage: Student's percentage (0-100)
        
    Returns:
        Dictionary with grade, remark, and status
    """
    match percentage:
        case p if not (0 <= p <= 100):
            return {"grade": "N/A", "remark": "Invalid! Enter 0-100.", "passed": False}
        case p if p >= 90:
            return {"grade": "A+", "remark": "Outstanding! 🏆", "passed": True}
        case p if p >= 80:
            return {"grade": "A", "remark": "Excellent! ⭐", "passed": True}
        case p if p >= 70:
            return {"grade": "B", "remark": "Good! 👍", "passed": True}
        case p if p >= 60:
            return {"grade": "C", "remark": "Average 📝", "passed": True}
        case p if p >= 50:
            return {"grade": "D", "remark": "Need Improvement ⚠️", "passed": True}
        case _:
            return {"grade": "F", "remark": "Fail ❌", "passed": False}


def display_result(percentage: float, result: dict) -> None:
    """Display formatted result."""
    print(f"\n📋 Result:")
    print(f"   Percentage: {percentage}%")
    print(f"   Grade:      {result['grade']}")
    print(f"   Remark:     {result['remark']}")
    print(f"   Status:     {'✅ PASS' if result['passed'] else '❌ FAIL'}")


def main():
    """Main function to run the grade calculator."""
    try:
        percentage = float(input("Enter your percentage: "))
        result = get_grade(percentage)
        display_result(percentage, result)
    except ValueError:
        print("❌ Please enter a valid number!")


if __name__ == "__main__":
    main()