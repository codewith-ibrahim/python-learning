# 🔐 Simple Login System
# Real Life Scenario: Username aur Password se Login

print("=" * 40)
print("🔐 LOGIN SYSTEM")
print("=" * 40)

# Pre-defined users database
# Dictionary ke andar dictionary!
users = {
    "ibrahim": {
        "password": "py123",
        "name": "Shaikh Ibrahim",
        "role": "Admin"
    },
    "ali": {
        "password": "ali456",
        "name": "Ali Ahmed",
        "role": "Student"
    },
    "sara": {
        "password": "sara789",
        "name": "Sara Khan",
        "role": "Teacher"
    }
}

# Login
print("\nPlease login to continue...")
username = input("Username: ").lower()  # Case insensitive banaya
password = input("Password: ")

print("\nChecking credentials...\n")

# Authentication
if username in users:
    if password == users[username]["password"]:
        # Successful Login
        print("✅ LOGIN SUCCESSFUL!")
        print("-" * 30)
        print(f"Welcome, {users[username]['name']}!")
        print(f"Role: {users[username]['role']}")
        print("-" * 30)
        
        # Role-based welcome message
        if users[username]["role"] == "Admin":
            print("\n🔧 Admin Panel Available")
            print("You have full access to the system.")
        elif users[username]["role"] == "Teacher":
            print("\n📚 Teacher Dashboard")
            print("You can manage your courses.")
        else:
            print("\n📖 Student Dashboard")
            print("Check your courses and assignments.")
    else:
        # Wrong Password
        print("❌ LOGIN FAILED!")
        print("Incorrect password.")
        print("Please try again.")
else:
    # Wrong Username
    print("❌ LOGIN FAILED!")
    print("Username not found.")
    print("Please check your username or register first.")

# Security Tip
print("\n🔒 Security Tip: Kabhi apna password kisi ke saath share na karein!")