# ============================================================
# PRACTICE 4: CSV FILE HANDLING
# ============================================================
# Problem: Student records CSV format mein save karo,
#          phir CSV file se data read karo.
# ============================================================

import csv

print("=" * 50)
print("📊 CSV FILE PRACTICE")
print("=" * 50)


# ---------- STEP 1: Create student data ----------
print("\n1️⃣  CREATING student data...")

students = [
    ["Name", "Age", "Course", "Marks", "Grade"],
    ["Shaikh Ibrahim", "22", "Python", "95", "A+"],
    ["Ali Ahmed", "21", "Python", "80", "A"],
    ["Sara Khan", "23", "Python", "88", "A"],
    ["Huzaifa Ali", "20", "Python", "65", "C"],
    ["Fatima Zahra", "22", "Python", "72", "B"],
]

print(f"   📊 Total records: {len(students) - 1} students")


# ---------- STEP 2: Write CSV file ----------
print("\n2️⃣  WRITING CSV file...")

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)  # Saari rows ek baar mein

print("   ✅ Student records saved to 'students.csv'!")


# ---------- STEP 3: Read CSV file ----------
print("\n3️⃣  READING CSV file...")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    print("\n   📄 STUDENT RECORDS:")
    print("   " + "─" * 50)
    
    for row in reader:
        if reader.line_num == 1:
            # Header row
            print(f"   {row[0]:20} {row[1]:5} {row[2]:10} {row[3]:6} {row[4]}")
            print("   " + "─" * 50)
        else:
            print(f"   {row[0]:20} {row[1]:5} {row[2]:10} {row[3]:6} {row[4]}")

print("   " + "─" * 50)
print("   ✅ CSV file read successfully!")


# ---------- STEP 4: Append new record ----------
print("\n4️⃣  APPENDING new student...")

new_student = ["Zainab Bibi", "21", "Python", "90", "A+"]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print(f"   ✅ Added: {new_student[0]}")

# Show updated file
print("\n   📄 UPDATED RECORDS:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if reader.line_num == 1:
            print(f"   {row[0]:20} {row[1]:5} {row[2]:10} {row[3]:6} {row[4]}")
            print("   " + "─" * 50)
        else:
            print(f"   {row[0]:20} {row[1]:5} {row[2]:10} {row[3]:6} {row[4]}")


# ---------- STEP 5: CSV with Dictionary ----------
print("\n5️⃣  CSV with DICTIONARY...")

# Write with DictWriter
fieldnames = ["name", "age", "course", "marks"]

dict_students = [
    {"name": "Ibrahim", "age": "22", "course": "Python", "marks": "95"},
    {"name": "Ali", "age": "21", "course": "Python", "marks": "80"},
    {"name": "Sara", "age": "23", "course": "Python", "marks": "88"},
]

with open("students_dict.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()         # Header likho
    writer.writerows(dict_students)  # Data likho

print("   ✅ Dictionary data saved!")

# Read with DictReader
print("\n   📄 DICTIONARY CSV CONTENT:")
with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"   👤 {row['name']:10} | Age: {row['age']} | {row['course']}: {row['marks']}%")


# ---------- KEY LEARNING ----------
print("\n" + "=" * 50)
print("📊 WHAT I LEARNED:")
print("=" * 50)
print("""
✅ CSV = Comma Separated Values (Spreadsheet format)
✅ csv.writer() = CSV file mein write karna
✅ csv.reader() = CSV file se read karna
✅ csv.DictWriter() = Dictionary se CSV write
✅ csv.DictReader() = CSV se dictionary read
✅ newline="" = Windows par extra lines avoid
✅ writerow() = Ek row write
✅ writerows() = Multiple rows write
""")