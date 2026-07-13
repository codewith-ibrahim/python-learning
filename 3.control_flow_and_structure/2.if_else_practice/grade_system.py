# 📊 Grade System
# Real Life Scenario: Exam Marks ke hisaab se Grade dena

print("=" * 40)
print("📊 STUDENT GRADE CALCULATOR")
print("=" * 40)

# Input
student_name = input("Enter Student Name: ")
marks = int(input(f"Enter {student_name}'s Marks (0-100): "))

# Validation
if marks < 0 or marks > 100:
    print("\n❌ Invalid Marks! 0 se 100 ke beech mein daalein.")
else:
    print(f"\n{student_name}'s Result:")
    print("-" * 25)

    # Grade Calculation
    if marks >= 90:
        grade = "A+"
        remark = "Outstanding! 🏆"
        gpa = "4.0"
    elif marks >= 80:
        grade = "A"
        remark = "Excellent! ⭐"
        gpa = "3.7"
    elif marks >= 70:
        grade = "B"
        remark = "Good! 👍"
        gpa = "3.0"
    elif marks >= 60:
        grade = "C"
        remark = "Average 📝"
        gpa = "2.5"
    elif marks >= 50:
        grade = "D"
        remark = "Pass (Need Improvement) ⚠️"
        gpa = "2.0"
    else:
        grade = "F"
        remark = "Fail 📚"
        gpa = "0.0"

    print(f"Marks:  {marks}/100")
    print(f"Grade:  {grade}")
    print(f"GPA:    {gpa}")
    print(f"Remark: {remark}")

    # Additional Advice
    if marks >= 90:
        print("\n🌟 Scholarship ke liye apply kar sakte hain!")
    elif marks < 50:
        print(f"\n💪 Hoshiyaar! {50 - marks} marks aur chahiye pass hone ke liye.")
        print("Agli baar zyada mehnat karo!")

print("\n📚 Keep Learning, Keep Growing!")