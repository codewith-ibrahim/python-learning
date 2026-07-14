# ============================================================
# PRACTICE 3: JSON FILE HANDLING
# ============================================================
# Problem: Python dictionary/list ko JSON file mein save karo,
#          phir JSON file se data load karo.
# ============================================================

import json

print("=" * 50)
print("📋 JSON FILE PRACTICE")
print("=" * 50)


# ---------- STEP 1: Create Python data ----------
print("\n1️⃣  CREATING Python data...")

student_data = {
    "name": "Shaikh Muhammad Ibrahim",
    "age": 22,
    "city": "Karachi",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "education": {
        "degree": "BSCS",
        "university": "Your University",
        "year": 2026
    },
    "is_learning": True,
    "projects": 5
}

print(f"   📊 Data Type: {type(student_data)}")
print(f"   📝 Keys: {list(student_data.keys())}")


# ---------- STEP 2: Save to JSON file ----------
print("\n2️⃣  SAVING to JSON file...")

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("   ✅ Data saved to 'student.json'!")


# ---------- STEP 3: Read from JSON file ----------
print("\n3️⃣  READING from JSON file...")

with open("student.json", "r") as file:
    loaded_data = json.load(file)

print(f"   📊 Loaded Type: {type(loaded_data)}")
print(f"   👤 Name: {loaded_data['name']}")
print(f"   🎂 Age: {loaded_data['age']}")
print(f"   📍 City: {loaded_data['city']}")
print(f"   💻 Skills: {', '.join(loaded_data['skills'])}")

print("   ✅ Data loaded successfully!")


# ---------- STEP 4: Pretty print JSON ----------
print("\n4️⃣  PRETTY PRINT JSON:")

json_string = json.dumps(loaded_data, indent=4)
print(f"   📄 JSON Content:")
for line in json_string.split("\n"):
    print(f"   {line}")


# ---------- STEP 5: Save list to JSON ----------
print("\n5️⃣  SAVING list to JSON...")

tasks = [
    {"task": "Learn Python", "completed": True, "priority": "High"},
    {"task": "Build Project", "completed": False, "priority": "High"},
    {"task": "Practice DSA", "completed": False, "priority": "Medium"},
    {"task": "Read Documentation", "completed": True, "priority": "Low"},
]

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

print("   ✅ Tasks saved to 'tasks.json'!")

# Read back
with open("tasks.json", "r") as file:
    loaded_tasks = json.load(file)
    print(f"\n   📋 TASKS LIST:")
    for i, task in enumerate(loaded_tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"   {i}. {status} {task['task']} ({task['priority']})")


# ---------- KEY LEARNING ----------
print("\n" + "=" * 50)
print("📊 WHAT I LEARNED:")
print("=" * 50)
print("""
✅ JSON = JavaScript Object Notation (Data format)
✅ json.dump() = Python data → JSON file
✅ json.load() = JSON file → Python data
✅ json.dumps() = Python data → JSON string
✅ indent=4 = Pretty formatting
✅ JSON supports: dict, list, str, int, float, bool, None
✅ Use case: Save/Load settings, user data, configurations
""")