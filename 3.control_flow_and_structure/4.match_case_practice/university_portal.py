# 🎓 University Portal — Match-Case Practice
# Real Life Scenario: Student portal for different departments

print("=" * 50)
print("🎓 PYTHON UNIVERSITY — STUDENT PORTAL")
print("=" * 50)

# Student login
print("\n📝 LOGIN")
student_id = input("Enter Student ID: ")

match student_id:
    case "CS101" | "CS102" | "CS103":
        department = "Computer Science"
        print(f"\n✅ Welcome! Department: {department}")
        
        print("\n📋 MENU:")
        print("1. View Courses")
        print("2. Check Attendance")
        print("3. Submit Assignment")
        print("4. View Grades")
        
        choice = input("Enter choice (1-4): ")
        
        match choice:
            case "1":
                print("\n📚 YOUR COURSES:")
                print("-" * 30)
                print("CS-201: Python Programming")
                print("CS-301: Data Structures")
                print("CS-401: Database Systems")
                print("CS-501: Web Development")
                
                semester = input("\nSelect semester (1st/2nd/3rd/4th): ").lower()
                
                match semester:
                    case "1st":
                        print("📖 1st Semester: CS-201 Python Programming")
                        print("   Teacher: Dr. Ahmed")
                        print("   Timing: Mon-Wed 9:00 AM")
                    case "2nd":
                        print("📖 2nd Semester: CS-301 Data Structures")
                        print("   Teacher: Prof. Sarah")
                        print("   Timing: Tue-Thu 11:00 AM")
                    case "3rd":
                        print("📖 3rd Semester: CS-401 Database Systems")
                        print("   Teacher: Dr. Usman")
                        print("   Timing: Mon-Wed 2:00 PM")
                    case "4th":
                        print("📖 4th Semester: CS-501 Web Development")
                        print("   Teacher: Prof. Ayesha")
                        print("   Timing: Tue-Thu 10:00 AM")
                    case _:
                        print("❌ Invalid semester!")
                        
            case "2":
                print("\n📊 ATTENDANCE REPORT:")
                print("-" * 30)
                print("CS-201: Python Programming  → 85%")
                print("CS-301: Data Structures      → 78%")
                print("CS-401: Database Systems     → 92%")
                print("CS-501: Web Development      → 80%")
                
            case "3":
                print("\n📤 SUBMIT ASSIGNMENT")
                subject = input("Enter subject code (CS-201/CS-301/CS-401/CS-501): ").upper()
                
                match subject:
                    case "CS-201":
                        print("📝 Assignment: Build a Calculator in Python")
                        print("📅 Deadline: 15 July 2026")
                        print("✅ Submitted successfully!")
                    case "CS-301":
                        print("📝 Assignment: Implement Linked List")
                        print("📅 Deadline: 20 July 2026")
                        print("✅ Submitted successfully!")
                    case "CS-401":
                        print("📝 Assignment: Design ER Diagram")
                        print("📅 Deadline: 18 July 2026")
                        print("⚠️  Pending submission!")
                    case "CS-501":
                        print("📝 Assignment: Create Responsive Website")
                        print("📅 Deadline: 25 July 2026")
                        print("⚠️  Pending submission!")
                    case _:
                        print("❌ Invalid subject code!")
                        
            case "4":
                print("\n📈 YOUR GRADES:")
                print("-" * 30)
                print("CS-201: Python Programming  → A (88%)")
                print("CS-301: Data Structures      → B+ (78%)")
                print("CS-401: Database Systems     → A- (85%)")
                print("CS-501: Web Development      → B (72%)")
                
            case _:
                print("❌ Invalid choice!")
                
    case "BBA101" | "BBA102":
        department = "Business Administration"
        print(f"\n✅ Welcome! Department: {department}")
        
        print("\n📋 MENU:")
        print("1. View Courses")
        print("2. Check Attendance")
        
        choice = input("Enter choice: ")
        
        match choice:
            case "1":
                print("\n📚 YOUR COURSES:")
                print("BBA-201: Principles of Management")
                print("BBA-301: Marketing")
                print("BBA-401: Finance")
            case "2":
                print("\n📊 ATTENDANCE: 90%")
            case _:
                print("❌ Invalid choice!")
                
    case "ENG101":
        department = "Engineering"
        print(f"\n✅ Welcome! Department: {department}")
        print("\n📚 Courses: Mechanical, Electrical, Civil")
        
    case "MED101":
        department = "Medical"
        print(f"\n✅ Welcome! Department: {department}")
        print("\n📚 Courses: Anatomy, Physiology, Biochemistry")
        
    case _:
        print("❌ Invalid Student ID!")
        print("💡 Contact administration: admin@pythonuniversity.edu")

print("\n🎓 Best of luck for your studies!")