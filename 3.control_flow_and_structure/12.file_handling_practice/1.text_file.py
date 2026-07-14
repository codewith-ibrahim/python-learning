# ============================================================
# PRACTICE 1: TEXT FILE HANDLING
# ============================================================
# Problem: Text file mein data write karo, phir read karo,
#          phir append karo, phir dobara read karo.
# ============================================================

print("=" * 50)
print("📄 TEXT FILE PRACTICE")
print("=" * 50)

# ---------- STEP 1: WRITE ----------
print("\n1️⃣  WRITING to file...")

with open("my_notes.txt", "w") as file:
    file.write("📅 Date: 14th July 2026\n")
    file.write("📝 Topic: Python File Handling\n")
    file.write("⏰ Time: 2:00 PM\n")
    file.write("─" * 30 + "\n")

print("   ✅ Notes written successfully!")


# ---------- STEP 2: READ ----------
print("\n2️⃣  READING from file...")

with open("my_notes.txt", "r") as file:
    content = file.read()
    print("   📄 File Content:")
    print("   " + "─" * 30)
    for line in content.split("\n"):
        if line:
            print(f"   {line}")
    print("   " + "─" * 30)

print("   ✅ File read successfully!")


# ---------- STEP 3: APPEND ----------
print("\n3️⃣  APPENDING to file...")

with open("my_notes.txt", "a") as file:
    file.write("\n📌 NEW NOTES (Appended):\n")
    file.write("─" * 30 + "\n")
    file.write("✅ Completed: Text file writing\n")
    file.write("✅ Completed: Text file reading\n")
    file.write("✅ Completed: Text file appending\n")
    file.write("✅ Learning: with statement is best!\n")

print("   ✅ Notes appended successfully!")


# ---------- STEP 4: READ AGAIN ----------
print("\n4️⃣  READING final file...")

with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    print(f"   📄 File has {len(lines)} lines now!")
    print("   " + "─" * 30)
    print("   FULL CONTENT:")
    for line in lines:
        print(f"   {line.strip()}")
    print("   " + "─" * 30)

print("\n✅ All operations completed!")


# ---------- KEY LEARNING ----------
print("\n" + "=" * 50)
print("📊 WHAT I LEARNED:")
print("=" * 50)
print("""
✅ "w" mode = Write (Fresh start, purana delete)
✅ "r" mode = Read (File exist karni chahiye)
✅ "a" mode = Append (Purana safe, end mein add)
✅ with statement = Auto close (Best practice!)
✅ write() = String write karta hai
✅ read() = Poori file ek string mein
✅ readlines() = Lines ki list deta hai
""")