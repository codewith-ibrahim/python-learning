# ============================================================
# PRACTICE 2: BINARY FILE HANDLING
# ============================================================
# Problem: Ek simple image file create karo (binary mein),
#          phir uski copy banao binary mode se.
# ============================================================

print("=" * 50)
print("🖼️  BINARY FILE PRACTICE")
print("=" * 50)


# ---------- STEP 1: Create a simple binary file ----------
print("\n1️⃣  CREATING binary file...")

# Simple binary data (Example: small black pixel)
# Ye real image nahi hai, sirf demo ke liye!
binary_data = bytes([255, 216, 255, 224, 0, 16, 74, 70, 73, 70, 
                     0, 1, 1, 0, 0, 1, 0, 1, 0, 0])

with open("demo_image.jpg", "wb") as file:
    file.write(binary_data)

print("   ✅ Binary file 'demo_image.jpg' created!")
print(f"   📏 File size: {len(binary_data)} bytes")


# ---------- STEP 2: Read binary file ----------
print("\n2️⃣  READING binary file...")

with open("demo_image.jpg", "rb") as file:
    data = file.read()
    print(f"   📏 Read {len(data)} bytes")
    print(f"   📊 First 10 bytes: {list(data[:10])}")

print("   ✅ Binary file read successfully!")


# ---------- STEP 3: Copy binary file ----------
print("\n3️⃣  COPYING binary file...")

with open("demo_image.jpg", "rb") as source:
    with open("demo_image_copy.jpg", "wb") as destination:
        # Read and write in chunks (Best for large files)
        chunk = source.read(5)  # 5 bytes at a time
        while chunk:
            destination.write(chunk)
            chunk = source.read(5)

print("   ✅ Binary file copied to 'demo_image_copy.jpg'!")


# ---------- STEP 4: Verify copy ----------
print("\n4️⃣  VERIFYING copy...")

with open("demo_image.jpg", "rb") as original:
    with open("demo_image_copy.jpg", "rb") as copy:
        if original.read() == copy.read():
            print("   ✅ Copy is IDENTICAL to original!")
        else:
            print("   ❌ Copy is DIFFERENT!")


# ---------- BONUS: Copy image with progress ----------
print("\n5️⃣  BONUS: Copy with progress...")

with open("demo_image.jpg", "rb") as src:
    # Saara data ek baar mein read karo (Small file ke liye OK)
    all_data = src.read()
    total_size = len(all_data)

with open("demo_image_progress.jpg", "wb") as dest:
    dest.write(all_data)
    print(f"   📊 Total: {total_size} bytes")
    print("   ████████████████████████ 100%")
    print("   ✅ Copy complete!")


# ---------- KEY LEARNING ----------
print("\n" + "=" * 50)
print("📊 WHAT I LEARNED:")
print("=" * 50)
print("""
✅ "wb" mode = Write Binary (Images, PDFs, etc.)
✅ "rb" mode = Read Binary
✅ bytes() = Binary data create karna
✅ Chunk reading = Best for large files
✅ Binary copy = Read from source, write to destination
✅ Text mode ("r"/"w") binary files ke liye USE MAT KARO!
""")