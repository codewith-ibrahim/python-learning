# File I/O (Input/Output) in Python

# File Handling kya hota hai?
#
# File Handling Python ka ek FEATURE hai jo humein
# FILES ko READ, WRITE, UPDATE, aur DELETE karne
# ki ability deta hai. Python programs files ke saath
# interact kar sakte hain — bilkul Notepad jaisa!
#
# Technical Definition:
# File I/O (Input/Output) ek mechanism hai jo program
# ko EXTERNAL FILES (text, CSV, JSON, etc.) ke saath
# data exchange karne ki ability deta hai. Python
# built-in open() function se files ko handle karta hai.

# Real Life Analogy:
# Socho aapke paas ek DIARY hai:
#
# 📖 Diary Khoolna = open() function
# ✍️ Kuch likhna = write mode ("w")
# 📖 Padhna = read mode ("r")
# ✍️ Aakhir mein kuch aur likhna = append mode ("a")
# 📖 Diary Band karna = close() function


# ============================================================
# PART 1: SAMPLE DATA (YOUR PARAGRAPH)
# ============================================================

paragraph = """
Ibrahim is learning Python and is focused on becoming an AI Engineer.
He has already completed the basics of Python, including variables, data types,
loops, functions, and collections. Currently, he is learning file handling and
object-oriented programming (OOP). His goal is to build real-world projects,
such as AI agents, automation tools, web applications, and machine learning
projects. Every day, he practices coding, solves programming problems, and
improves his problem-solving skills. He believes that consistent practice and
building projects are the best ways to master Python and prepare for a career
in Agentic AI.
"""

print("📄 Sample paragraph ready!")


# ============================================================
# PART 2: WHAT IS open() FUNCTION?
# ============================================================

print("\n" + "=" * 60)
print("📊 WHAT IS open() FUNCTION?")
print("=" * 60)

print("""
open() Python ka BUILT-IN FUNCTION hai jo file ko
open karta hai aur FILE OBJECT return karta hai.

SYNTAX:
open(file_name, mode, encoding)

🔹 file_name  → File ka naam/path (e.g., "test.txt")
🔹 mode       → File open karne ka mode (read/write/append)
🔹 encoding   → Character encoding (default: UTF-8)

MODES (Bohot Important!):
┌──────────┬──────────────────────┬──────────────────────────┐
│ Mode     │ Symbol               │ Kya Karta Hai?           │
├──────────┼──────────────────────┼──────────────────────────┤
│ Read     │ "r"                  │ Sirf padh sakte hain     │
│ Write    │ "w"                  │ Likho (Purana DELETE!)   │
│ Append   │ "a"                  │ Aakhir mein jodo         │
│ Create   │ "x"                  │ Nayi file (Exist→Error)  │
│ Binary   │ "rb", "wb", "ab"     │ Binary files (images)    │
│ Read+Wr  │ "r+"                 │ Padho aur likho          │
└──────────┴──────────────────────┴──────────────────────────┘
""")


# ============================================================
# PART 3: WHAT IS with STATEMENT? (CONTEXT MANAGER)
# ============================================================

print("=" * 60)
print("📊 WHAT IS with STATEMENT? (Context Manager)")
print("=" * 60)

print("""
with Python ka CONTEXT MANAGER hai.

SIMPLE DEFINITION:
with statement AUTOMATICALLY file close karta hai.
Aapko manually close() call karne ki zaroorat nahi!


❌ WITHOUT with (LENGTHY WAY):
─────────────────────────────────
fp = open("test.txt", "w")      ← File open
fp.write(paragraph)              ← Write karo
fp.close()                       ← Manually close karo!
→ Agar close() bhool gaye = Memory leak!
→ Agar error aaya beech mein = File open reh jayegi!


✅ WITH with (SHORTER WAY — RECOMMENDED):
──────────────────────────────────────────
with open("test.txt", "w") as f:  ← File open
    f.write(paragraph)             ← Write karo
→ File AUTOMATICALLY close hogi (chahe error aaye ya na aaye!)

with = "With this file, do something, then automatically close it"


HOW with WORKS INTERNALLY:
1. __enter__() method call → File open
2. Block execute → f.write() etc.
3. __exit__() method call → File close (HAMESHA!)
   (Chahe error aaye ya na aaye, close hoga!)


WHY with IS BETTER:
✅ Automatic cleanup (No memory leaks)
✅ Shorter, cleaner code
✅ Exception safe (Error aaye to bhi close)
✅ No need to remember close()
✅ Python best practice
""")


# ============================================================
# PART 4: WRITING TO A FILE — COMPLETE EXPLANATION
# ============================================================

print("=" * 60)
print("📊 WRITING TO A FILE (Write Mode — 'w')")
print("=" * 60)

print("""
WRITE MODE ("w") KI PROPERTIES:
┌─────────────────────────────────────────────────────┐
│ ✅ Agar file exist KARTI HAI → Purana content       │
│    DELETE hoga, naya content likha jayega!           │
│                                                     │
│ ✅ Agar file exist NAHI KARTI → Nayi file CREATE    │
│    hogi, phir content likha jayega!                  │
│                                                     │
│ ⚠️  WARNING: "w" mode PURANA CONTENT DELETE KAR     │
│    DETA HAI! Agar existing data rakhna hai, to       │
│    APPEND mode ("a") use karo!                       │
└─────────────────────────────────────────────────────┘

WHEN TO USE "w" MODE:
✅ Fresh file create karni hai
✅ Purana data replace karna hai
✅ Log file reset karni hai
✅ New configuration file banana hai

WHEN NOT TO USE "w" MODE:
❌ Existing data mein kuch add karna hai (Use "a")
❌ Data lose nahi karna (Use "a" or "r+")
""")


# --- METHOD 1: Using with (SHORTER & RECOMMENDED) ---
print("\n🔍 METHOD 1: Using with (Recommended)")
print("-" * 40)

with open("test.txt", "w") as f:
    f.write(paragraph)
    print("   ✅ File written successfully (with statement)!")

# Behind the scenes:
# 1. open("test.txt", "w") → File object create/overwrite
# 2. as f → File object ko 'f' variable mein store karo
# 3. f.write(paragraph) → Content write karo
# 4. with block end → File AUTOMATICALLY close!


# --- METHOD 2: Without with (LENGTHY — NOT RECOMMENDED) ---
print("\n🔍 METHOD 2: Without with (Manual)")
print("-" * 40)

fp = open("test.txt", "w")    # Step 1: File open
fp.write(paragraph)           # Step 2: Write content
fp.close()                    # Step 3: Manually close
print("   ✅ File written successfully (manual close)!")

# Problems with manual close:
# ❌ close() bhool sakte hain
# ❌ Error aaya to close() execute nahi hoga
# ❌ Memory leak ho sakta hai


# ============================================================
# PART 5: READING A FILE — COMPLETE EXPLANATION
# ============================================================

print("\n" + "=" * 60)
print("📊 READING A FILE (Read Mode — 'r')")
print("=" * 60)

print("""
READ MODE ("r") KI PROPERTIES:
┌─────────────────────────────────────────────────────┐
│ ✅ Agar file exist KARTI HAI → File open hogi,      │
│    content read kar sakte hain.                      │
│                                                     │
│ ❌ Agar file exist NAHI KARTI → FileNotFoundError!  │
│    (Error aayega, program crash ho sakta hai)        │
│                                                     │
│ 📝 "r" DEFAULT mode hai — agar mode na do to "r"    │
│    automatically use hota hai.                       │
└─────────────────────────────────────────────────────┘

READ METHODS:
┌──────────────────┬──────────────────────────────────┐
│ Method           │ Kya Karta Hai?                   │
├──────────────────┼──────────────────────────────────┤
│ f.read()         │ Poori file ek string mein       │
│ f.read(n)        │ Sirf n characters padho         │
│ f.readline()     │ Sirf ek line padho              │
│ f.readlines()    │ Saari lines list mein           │
└──────────────────┴──────────────────────────────────┘
""")


# --- METHOD 1: Using with (SHORTER & RECOMMENDED) ---
print("\n🔍 METHOD 1: Reading with with (Recommended)")
print("-" * 40)

with open("test.txt", "r") as f:
    reading_file = f.read()
    print("   ✅ File content:")
    print("   " + "-" * 40)
    # Print first 100 characters with ...
    preview = reading_file[:100] + "..." if len(reading_file) > 100 else reading_file
    print(f"   {preview}")
    print("   " + "-" * 40)

print("Paragraph reading successfully!")


# --- METHOD 2: Without with (LENGTHY) ---
print("\n🔍 METHOD 2: Reading without with (Manual)")
print("-" * 40)

fp = open("test.txt", "r")    # Step 1: File open
reading_file = fp.read()      # Step 2: Read content
print("   ✅ File read successfully!")
fp.close()                    # Step 3: Close

print("Paragraph reading successfully! (Manual)")


# ============================================================
# PART 6: APPENDING TO A FILE — COMPLETE EXPLANATION
# ============================================================

print("\n" + "=" * 60)
print("📊 APPENDING TO A FILE (Append Mode — 'a')")
print("=" * 60)

print("""
APPEND MODE ("a") KI PROPERTIES:
┌─────────────────────────────────────────────────────┐
│ ✅ Agar file exist KARTI HAI → File ke END mein     │
│    naya content ADD hoga. Purana data SAFE rahega!   │
│                                                     │
│ ✅ Agar file exist NAHI KARTI → Nayi file CREATE    │
│    hogi (Bilkul "w" mode ki tarah).                  │
│                                                     │
│ ✅ Cursor hamesha file ke END mein hota hai.         │
│                                                     │
│ ✅ PURANA DATA DELETE NAHI HOTA!                     │
└─────────────────────────────────────────────────────┘

WHEN TO USE "a" MODE:
✅ Log file mein naya entry add karna
✅ Existing data ke aage kuch likhna
✅ Data collect karte rehna (e.g., sensor readings)
✅ Journal/Diary maintain karna

"w" vs "a" — IMPORTANT DIFFERENCE:
┌──────────────┬─────────────────────┬──────────────────────┐
│ "w" (Write)  │ Purana DELETE → Naya│ Fresh file banana     │
│ "a" (Append) │ Purana SAFE → Add   │ Existing mein add     │
└──────────────┴─────────────────────┴──────────────────────┘
""")


# --- METHOD 1: Using with (SHORTER & RECOMMENDED) ---
print("\n🔍 METHOD 1: Appending with with (Recommended)")
print("-" * 40)

append_text = "\n\n--- This line was APPENDED later ---\nNew learning: File handling completed successfully!"

with open("test.txt", "a") as f:
    f.write(append_text)
    print("   ✅ Content appended successfully (with statement)!")


# --- METHOD 2: Without with (LENGTHY) ---
print("\n🔍 METHOD 2: Appending without with (Manual)")
print("-" * 40)

append_text2 = "\n\n--- Another APPEND operation ---\nNew learning: OOP concepts started!"

fp = open("test.txt", "a")     # Step 1: Open in append mode
fp.write(append_text2)         # Step 2: Append content
fp.close()                     # Step 3: Close
print("   ✅ Content appended successfully (manual)!")


# ============================================================
# PART 7: ALL FILE MODES — COMPLETE TABLE
# ============================================================

print("\n" + "=" * 60)
print("📊 ALL FILE MODES — COMPLETE REFERENCE")
print("=" * 60)

print("""
┌────────┬──────────┬──────────────────────┬──────────────────────┐
│ Mode   │ Symbol   │ File Exists?         │ File Doesn't Exist?  │
├────────┼──────────┼──────────────────────┼──────────────────────┤
│ Read   │ "r"      │ Open for reading     │ ERROR!               │
│ Write  │ "w"      │ OVERWRITE (Delete!)  │ Create new           │
│ Append │ "a"      │ Add at end           │ Create new           │
│ Create │ "x"      │ ERROR!               │ Create new           │
├────────┼──────────┼──────────────────────┼──────────────────────┤
│ Text   │ "t"      │ Default (text mode)  │ Text file            │
│ Binary │ "b"      │ Binary data          │ Images, PDFs, etc.   │
├────────┼──────────┼──────────────────────┼──────────────────────┤
│ Read+  │ "r+"     │ Read & Write         │ ERROR!               │
│ Write+ │ "w+"     │ Read & Write (OVR)   │ Create new           │
│ Append+│ "a+"     │ Read & Append        │ Create new           │
└────────┴──────────┴──────────────────────┴──────────────────────┘

COMBINATIONS (Most Used):
"rt" = Read Text (Same as "r")         ← Default
"wt" = Write Text (Same as "w")        ← Default
"rb" = Read Binary (Images, PDFs)
"wb" = Write Binary (Save images)
""")


# ============================================================
# PART 8: FILE READING TECHNIQUES
# ============================================================

print("=" * 60)
print("📊 FILE READING TECHNIQUES")
print("=" * 60)


# Technique 1: read() — Poori file ek baar mein
print("\n🔍 1. f.read() — Poori file ek string mein:")
print("-" * 40)
with open("test.txt", "r") as f:
    content = f.read()
    print(f"   Total characters: {len(content)}")
    print(f"   First 80 chars: {content[:80]}...")


# Technique 2: read(n) — Sirf n characters
print("\n🔍 2. f.read(n) — Sirf n characters:")
print("-" * 40)
with open("test.txt", "r") as f:
    first_50 = f.read(50)
    print(f"   First 50 chars: {first_50}...")


# Technique 3: readline() — Ek line padho
print("\n🔍 3. f.readline() — Ek-ek line:")
print("-" * 40)
with open("test.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"   Line 1: {line1.strip()[:60]}...")
    print(f"   Line 2: {line2.strip()[:60]}...")


# Technique 4: readlines() — Saari lines list mein
print("\n🔍 4. f.readlines() — Saari lines list mein:")
print("-" * 40)
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(f"   Total lines: {len(lines)}")
    print(f"   Line 3: {lines[2].strip()[:60]}...")


# Technique 5: Loop — Best for large files
print("\n🔍 5. for loop — Line by line (Memory Efficient):")
print("-" * 40)
with open("test.txt", "r") as f:
    line_count = 0
    for line in f:
        line_count += 1
        if line_count <= 2:  # Sirf pehli 2 lines print
            print(f"   Line {line_count}: {line.strip()[:60]}...")
    print(f"   Total lines read: {line_count}")


# ============================================================
# PART 9: REAL LIFE EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("📊 REAL LIFE FILE HANDLING EXAMPLES")
print("=" * 60)


# Example 1: Student Logger
print("\n🔍 EXAMPLE 1: Student Logger")
print("-" * 40)

def log_student(name, course, marks):
    """Student ka record file mein save karo."""
    with open("students_log.txt", "a") as f:
        f.write(f"Student: {name}, Course: {course}, Marks: {marks}\n")
    print(f"   ✅ {name}'s record saved!")

log_student("Ibrahim", "Python", 95)
log_student("Ali", "Python", 80)
log_student("Sara", "Python", 88)

# Read the log
print("\n   📄 Students Log File Content:")
with open("students_log.txt", "r") as f:
    print(f.read())


# Example 2: Daily Diary
print("\n\n🔍 EXAMPLE 2: Daily Diary")
print("-" * 40)

from datetime import datetime

def write_diary(entry):
    """Daily diary with timestamp."""
    today = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"\n[{today}]\n{entry}\n{'─'*40}\n")
    print(f"   ✅ Diary entry saved!")

write_diary("Today I learned File Handling in Python. It was amazing!")
write_diary("Built a student logger and diary app using file I/O.")


# Example 3: To-Do List Manager
print("\n\n🔍 EXAMPLE 3: To-Do List Manager")
print("-" * 40)

def add_task(task):
    """Task add karo."""
    with open("todo.txt", "a") as f:
        f.write(f"[ ] {task}\n")
    print(f"   ✅ Task added: {task}")

def show_tasks():
    """Saare tasks dikhao."""
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            if tasks:
                print("   📋 YOUR TO-DO LIST:")
                for i, task in enumerate(tasks, 1):
                    print(f"   {i}. {task.strip()}")
            else:
                print("   📋 No tasks yet!")
    except FileNotFoundError:
        print("   📋 No tasks yet! Add some tasks first.")

add_task("Complete Python File Handling")
add_task("Practice OOP Concepts")
add_task("Build a mini project")
add_task("Revise all topics")

print()
show_tasks()


# Example 4: Simple Note-Taking App
print("\n\n🔍 EXAMPLE 4: Note-Taking App")
print("-" * 40)

def create_note(title, content):
    """Note create karo with title."""
    filename = f"note_{title.lower().replace(' ', '_')}.txt"
    with open(filename, "w") as f:
        f.write(f"{'='*50}\n")
        f.write(f"TITLE: {title}\n")
        f.write(f"{'='*50}\n\n")
        f.write(content)
        f.write(f"\n\n{'='*50}\n")
        f.write(f"Created: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
    print(f"   ✅ Note saved: {filename}")

def read_note(title):
    """Note read karo."""
    filename = f"note_{title.lower().replace(' ', '_')}.txt"
    try:
        with open(filename, "r") as f:
            print(f"   📄 Note Content:\n   {'─'*40}")
            print(f.read())
    except FileNotFoundError:
        print(f"   ❌ Note '{title}' not found!")

create_note("Python Learning", "Today I learned:\n1. File I/O\n2. Context Managers\n3. File Modes")
print()
read_note("Python Learning")


# Example 5: Simple CSV Writer
print("\n\n🔍 EXAMPLE 5: Simple CSV Writer")
print("-" * 40)

def save_students_csv():
    """Students data CSV format mein save karo."""
    students = [
        ["Name", "Age", "Course", "Marks"],
        ["Ibrahim", "22", "Python", "95"],
        ["Ali", "21", "Python", "80"],
        ["Sara", "23", "Python", "88"],
        ["Ahmed", "22", "Python", "75"]
    ]
    
    with open("students.csv", "w") as f:
        for student in students:
            f.write(",".join(student) + "\n")
    
    print("   ✅ Students data saved to 'students.csv'!")
    
    # Read and display
    print("\n   📄 CSV Content:")
    with open("students.csv", "r") as f:
        print(f.read())

save_students_csv()


# ============================================================
# PART 10: ERROR HANDLING IN FILE OPERATIONS
# ============================================================

print("\n" + "=" * 60)
print("📊 ERROR HANDLING IN FILE OPERATIONS")
print("=" * 60)

def safe_file_read(filename):
    """File ko SAFELY read karo — kabhi crash nahi hoga!"""
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"   ✅ File '{filename}' read successfully!")
            print(f"   📏 Size: {len(content)} characters")
            return content
    except FileNotFoundError:
        print(f"   ❌ File '{filename}' not found!")
        print(f"   💡 Create the file first or check spelling.")
    except PermissionError:
        print(f"   ❌ Permission denied for '{filename}'!")
        print(f"   💡 Check file permissions.")
    except IsADirectoryError:
        print(f"   ❌ '{filename}' is a directory, not a file!")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
    finally:
        print(f"   🔒 File operation completed.\n")
    return None

# Test
safe_file_read("test.txt")           # ✅ File exists
safe_file_read("nonexistent.txt")    # ❌ File nahi hai
safe_file_read("test.txt")           # ✅ File exists


# ============================================================
# PART 11: BEST PRACTICES
# ============================================================

print("=" * 60)
print("📊 BEST PRACTICES — FILE HANDLING")
print("=" * 60)

print("""
✅ DO's:
  1. HAMESHA with statement use karo (Auto close)
  2. File operations ko try-except mein wrap karo
  3. Meaningful file names rakho
  4. Binary files ke liye "rb"/"wb" use karo
  5. Large files ke liye loop/readline use karo (read() nahi)
  6. File path ke liye os.path use karo (Cross-platform)
  7. Encoding specify karo (utf-8)

❌ DON'Ts:
  1. close() karna mat bhoolo (agar with use nahi kiya)
  2. "w" mode mein existing data overwrite ka dhyan rakho
  3. Binary files ko text mode mein mat kholo
  4. User input se direct filename mat lo (Path Traversal)
  5. Poori file ek baar mein memory mein load na karo (Large files)


MEMORY TIP:
┌──────────────────┬──────────────────────────────────────┐
│ Small File (<1MB)│ f.read() — Poori ek baar mein ✅      │
│ Large File (>1MB)│ for line in f — Line by line ✅       │
│ Huge File (>1GB) │ f.read(n) — Chunks mein padho ✅     │
└──────────────────┴──────────────────────────────────────┘
""")


# ============================================================
# PART 12: FILE POINTER (SEEK & TELL)
# ============================================================

print("=" * 60)
print("📊 FILE POINTER — seek() & tell()")
print("=" * 60)

print("""
File Pointer = CURSOR ki position file mein
(Aage se kitne characters padh liye)

🔹 f.tell() → Current pointer position batata hai
🔹 f.seek(n) → Pointer ko n position par le jata hai
🔹 f.seek(0) → Pointer wapas START mein!
""")

# Demonstration
print("\n🔍 Demonstration:")
print("-" * 40)

with open("test.txt", "r") as f:
    print(f"   Start position: {f.tell()}")         # 0
    
    first_20 = f.read(20)
    print(f"   Read 20 chars. Position: {f.tell()}") # 20
    
    next_20 = f.read(20)
    print(f"   Read 20 more. Position: {f.tell()}")  # 40
    
    f.seek(0)  # Wapas start mein!
    print(f"   After seek(0). Position: {f.tell()}")  # 0
    
    first_line = f.readline()
    print(f"   Read first line. Position: {f.tell()}")


# ============================================================
# PART 13: COMPLETE SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("📊 COMPLETE SUMMARY — FILE HANDLING")
print("=" * 60)

print("""
✅ WHAT IS FILE HANDLING?
   Files ko read, write, append karne ka mechanism.
   Python ka open() function use hota hai.

✅ WHAT IS with STATEMENT?
   Context manager — file ko automatically close karta hai.
   with open("file.txt", "r") as f:
       # f automatically close hoga!

✅ FILE MODES:
   "r"  → Read (Default)
   "w"  → Write (Purana DELETE → Naya likho)
   "a"  → Append (Purana SAFE → End mein jodo)
   "x"  → Create (Nayi file, exist→Error)
   "rb" → Read Binary
   "wb" → Write Binary

✅ "w" vs "a":
   "w" = Purana delete + Naya likho (FRESH START)
   "a" = Purana safe + End mein add karo (CONTINUE)

✅ READING METHODS:
   f.read()      → Poori file (String)
   f.read(n)     → Sirf n characters
   f.readline()  → Ek line
   f.readlines() → Saari lines (List)
   for line in f → Best for large files!

✅ WRITING METHODS:
   f.write(text)        → String write karo
   f.writelines(list)   → List of strings write karo

✅ FILE POINTER:
   f.tell()  → Current position
   f.seek(n) → Position set karo

✅ BEST PRACTICES:
   ✅ with statement use karo
   ✅ try-except wrap karo
   ✅ Large files: line by line
   ✅ Binary: "rb"/"wb"
   ❌ close() mat bhoolo
   ❌ Large file: read() mat karo
""")


# ============================================================
# QUICK QUIZ
# ============================================================

print("\n" + "=" * 60)
print("📝 QUICK QUIZ — FILE HANDLING")
print("=" * 60)

print("""
Q1: File open karne ke liye kaunsa function use hota hai?
A:  open()

Q2: with statement kya hai?
A:  Context manager — file ko automatically close karta hai.

Q3: "w" aur "a" mode mein kya difference hai?
A:  "w" = Purana delete → Naya likho
    "a" = Purana safe → End mein add karo

Q4: Agar file exist na kare aur "r" mode use karein to kya hoga?
A:  FileNotFoundError aayega!

Q5: Poori file ek baar mein padhne ke liye kaunsa method?
A:  f.read()

Q6: Large files ke liye best reading technique kya hai?
A:  for line in f: (Line by line — Memory efficient)

Q7: f.seek(0) kya karta hai?
A:  File pointer ko START mein le jata hai.

Q8: f.tell() kya karta hai?
A:  Current pointer position batata hai.

Q9: File handling mein try-except kyun use karte hain?
A:  File not found, permission errors handle karne ke liye.

Q10: Binary file (image) read karne ke liye kaunsa mode?
A:   "rb" (Read Binary)
""")