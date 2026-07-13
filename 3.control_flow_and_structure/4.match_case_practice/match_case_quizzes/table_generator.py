# ============================================================
# QUICK QUIZ 1: Table Generator
# ============================================================
# Write a Python program that asks the user to enter a number.
# If the number is between 1 and 10 (inclusive), print its 
# multiplication table. Otherwise, display an appropriate 
# message indicating that only numbers from 1 to 10 are allowed.
# ============================================================


# ============================================================
# VERSION 1: BEGINNER FRIENDLY
# ============================================================
# Simple, easy to understand, step by step comments

print("=" * 40)
print("🧮 TABLE GENERATOR (Beginner Version)")
print("=" * 40)

# Step 1: User se number lo
number = int(input("Enter a number (1-10): "))

# Step 2: Match-Case se check karo
match number:
    case 1:
        # Agar 1 hai to table print karo
        print(f"\n📊 Table of {number}:")
        print("   1 x 1 = 1")
        print("   1 x 2 = 2")
        print("   1 x 3 = 3")
        print("   1 x 4 = 4")
        print("   1 x 5 = 5")
        print("   1 x 6 = 6")
        print("   1 x 7 = 7")
        print("   1 x 8 = 8")
        print("   1 x 9 = 9")
        print("   1 x 10 = 10")
        
    case 2:
        print(f"\n📊 Table of {number}:")
        print("   2 x 1 = 2")
        print("   2 x 2 = 4")
        print("   2 x 3 = 6")
        print("   2 x 4 = 8")
        print("   2 x 5 = 10")
        print("   2 x 6 = 12")
        print("   2 x 7 = 14")
        print("   2 x 8 = 16")
        print("   2 x 9 = 18")
        print("   2 x 10 = 20")
        
    case 3:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   3 x {i} = {3 * i}")
            
    case 4:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   4 x {i} = {4 * i}")
            
    case 5:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   5 x {i} = {5 * i}")
            
    case 6:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   6 x {i} = {6 * i}")
            
    case 7:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   7 x {i} = {7 * i}")
            
    case 8:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   8 x {i} = {8 * i}")
            
    case 9:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   9 x {i} = {9 * i}")
            
    case 10:
        print(f"\n📊 Table of {number}:")
        for i in range(1, 11):
            print(f"   10 x {i} = {10 * i}")
            
    case _:
        # Agar 1-10 ke beech mein nahi hai
        print("❌ Please enter a number between 1 and 10 only!")


print("\n" + "=" * 60)


# ============================================================
# VERSION 2: BETTER VERSION
# ============================================================
# Loop use kiya, code chhota hua, lekin simple hai

print("\n🧮 TABLE GENERATOR (Better Version)")
print("=" * 40)

number = int(input("Enter a number (1-10): "))

match number:
    case n if 1 <= n <= 10:
        # Guard use karke range check ki
        print(f"\n📊 Table of {n}:")
        print("-" * 20)
        for i in range(1, 11):
            print(f"   {n:2} x {i:2} = {n * i:3}")
        print("-" * 20)
    case _:
        print("❌ Please enter a number between 1 and 10 only!")


print("\n" + "=" * 60)


# ============================================================
# VERSION 3: SENIOR DEV VERSION
# ============================================================
# Function, error handling, reusable, professional

print("\n🧮 TABLE GENERATOR (Senior Dev Version)")
print("=" * 40)


def generate_table(num: int) -> str:
    """
    Generate multiplication table for a given number.
    
    Args:
        num: Number between 1 and 10
        
    Returns:
        Formatted table string
    """
    table = f"\n📊 Table of {num}:\n"
    table += "-" * 20 + "\n"
    table += "\n".join(f"   {num:2} x {i:2} = {num * i:3}" for i in range(1, 11))
    table += "\n" + "-" * 20
    return table


def main():
    """Main function to run the table generator."""
    try:
        number = int(input("Enter a number (1-10): "))
        
        match number:
            case n if 1 <= n <= 10:
                print(generate_table(n))
            case _:
                print("❌ Invalid input! Only numbers from 1 to 10 are allowed.")
                
    except ValueError:
        print("❌ Please enter a valid integer, not text!")


if __name__ == "__main__":
    main()