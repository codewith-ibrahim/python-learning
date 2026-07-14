# ============================================================
# PRACTICE 5: LOG FILE (Daily Logger)
# ============================================================
# Problem: Har activity ka log file mein record rakho
#          with timestamp, type, and message.
# ============================================================

from datetime import datetime
import os

print("=" * 50)
print("📝 LOG FILE PRACTICE")
print("=" * 50)


# ---------- STEP 1: Simple Logger Function ----------
print("\n1️⃣  CREATING logger function...")

def log_activity(log_type, message):
    """
    Activity ko log file mein save karo.
    
    Parameters:
    log_type = INFO, WARNING, ERROR, SUCCESS
    message  = Activity ka description
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{log_type:8}] {message}\n"
    
    with open("activity.log", "a") as file:
        file.write(log_entry)
    
    # Console mein bhi show karo
    emoji = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌", "SUCCESS": "✅"}
    print(f"   {emoji.get(log_type, '📝')} {log_entry.strip()}")

print("   ✅ Logger function ready!")


# ---------- STEP 2: Log different activities ----------
print("\n2️⃣  LOGGING activities...")

log_activity("INFO", "Application started")
log_activity("INFO", "Loading user settings...")
log_activity("SUCCESS", "User settings loaded successfully")
log_activity("INFO", "Connecting to database...")
log_activity("ERROR", "Database connection failed! Retrying...")
log_activity("WARNING", "Low disk space on drive C:")
log_activity("SUCCESS", "Database connected on retry 2")
log_activity("INFO", "Processing data...")
log_activity("SUCCESS", "Data processed: 150 records")
log_activity("INFO", "Application shutdown complete")

print("\n   ✅ All activities logged!")


# ---------- STEP 3: Read log file ----------
print("\n3️⃣  READING log file...")

with open("activity.log", "r") as file:
    log_content = file.read()

# Count statistics
total_lines = len(log_content.strip().split("\n"))
errors = log_content.count("[ERROR")
warnings = log_content.count("[WARNING")
success = log_content.count("[SUCCESS")
info = log_content.count("[INFO")

print(f"   📊 LOG STATISTICS:")
print(f"   📝 Total Entries: {total_lines}")
print(f"   ℹ️  INFO:     {info}")
print(f"   ✅ SUCCESS:  {success}")
print(f"   ⚠️  WARNING:  {warnings}")
print(f"   ❌ ERROR:    {errors}")


# ---------- STEP 4: Filter logs ----------
print("\n4️⃣  FILTERING logs...")
print("   ERRORS ONLY:")
print("   " + "─" * 40)

with open("activity.log", "r") as file:
    for line in file:
        if "[ERROR" in line:
            print(f"   {line.strip()}")

print("   " + "─" * 40)


# ---------- STEP 5: Daily log file ----------
print("\n5️⃣  CREATING daily log file...")

today = datetime.now().strftime("%Y-%m-%d")
daily_log_file = f"log_{today}.txt"

# Header with date
with open(daily_log_file, "w") as file:
    file.write(f"{'='*50}\n")
    file.write(f"DAILY LOG - {today}\n")
    file.write(f"{'='*50}\n\n")
    file.write("Today's Learning:\n")
    file.write("-" * 30 + "\n")
    file.write("✅ File Handling in Python\n")
    file.write("✅ Text file (read/write/append)\n")
    file.write("✅ Binary file (images)\n")
    file.write("✅ JSON file (data storage)\n")
    file.write("✅ CSV file (spreadsheet)\n")
    file.write("✅ Log file (activity tracking)\n")
    file.write("-" * 30 + "\n")
    file.write(f"\nTotal Practice: 5 exercises\n")
    file.write(f"Time Spent: 2 hours\n")

print(f"   ✅ Daily log saved to '{daily_log_file}'!")

# Show daily log
print(f"\n   📄 {daily_log_file} CONTENT:")
with open(daily_log_file, "r") as file:
    for line in file:
        print(f"   {line.strip()}")


# ---------- STEP 6: Check if files exist ----------
print("\n6️⃣  CHECKING all files...")

practice_files = [
    "my_notes.txt",
    "demo_image.jpg",
    "student.json",
    "students.csv",
    "activity.log",
    daily_log_file,
]

print("\n   📁 PRACTICE FILES CREATED:")
for file in practice_files:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"   ✅ {file:25} ({size} bytes)")
    else:
        print(f"   ❌ {file:25} (NOT FOUND)")


# ---------- KEY LEARNING ----------
print("\n" + "=" * 50)
print("📊 WHAT I LEARNED:")
print("=" * 50)
print("""
✅ Log files = Activity tracking with timestamps
✅ datetime.now() = Current date & time
✅ strftime() = Date/time ko format karna
✅ File append = Log entries add karte rehna
✅ Log filtering = Specific type ke logs dhundhna
✅ Daily logs = Date ke hisaab se alag file
✅ os.path.exists() = Check if file exists
✅ os.path.getsize() = File size check karna
""")

print("\n🎉 ALL FILE HANDLING PRACTICE COMPLETED!")
print("📁 Check your folder for all created files!")