# Exception Handling in Python (try-except)

# Exception Handling kya hota hai?
#
# Exception Handling ek MECHANISM hai jo program ko
# CRASH hone se bachata hai. Jab koi unexpected
# error aata hai, to program foran rukne ke bajaye
# us error ko GRACEFULLY handle karta hai.
#
# Technical Definition:
# Exception Handling runtime errors ko handle karne
# ka tareeqa hai. Try block mein suspicious code likhte
# hain, aur except block mein error ka response define
# karte hain. Program crash nahi hota, smoothly chalta hai.

# Real Life Analogy:
# Socho aap car chala rahe hain:
#
# 🚗 Normal Drive = Program ka normal execution
# ⚠️ Puncture = Exception (Unexpected problem)
# 🔧 Spare Wheel = Exception Handler (Solution)
#
# Agar spare wheel na ho (no exception handling):
# → Car wahin ruk jayegi (Program CRASH!)
#
# Agar spare wheel ho (exception handling):
# → Wheel change karo, continue drive (Program continues!)


# ============================================================
# PART 1: WHAT IS AN EXCEPTION?
# ============================================================

print("=" * 60)
print("📊 WHAT IS AN EXCEPTION?")
print("=" * 60)

print("""
EXCEPTION = Runtime Error (Program chalte waqt error)

ERROR vs EXCEPTION:
┌──────────────┬─────────────────────┬──────────────────────┐
│ Type         │ Kab aata hai?       │ Example              │
├──────────────┼─────────────────────┼──────────────────────┤
│ Syntax Error │ Code likhte waqt    │ Missing colon (:)    │
│ Exception    │ Program chalte waqt │ Division by zero     │
└──────────────┴─────────────────────┴──────────────────────┘

Common Exceptions in Python:
❌ ValueError        — Galat type ki value (int("abc"))
❌ TypeError         — Galat operation (5 + "hello")
❌ ZeroDivisionError — Zero se divide (5 / 0)
❌ IndexError        — List ke bahar index (list[100])
❌ KeyError          — Dictionary mein galat key
❌ FileNotFoundError — File nahi mili
❌ NameError         — Variable define nahi
❌ AttributeError    — Galat method/attribute
""")


# ============================================================
# PART 2: YOUR CODE — WITHOUT EXCEPTION HANDLING
# ============================================================

print("=" * 60)
print("📊 WITHOUT EXCEPTION HANDLING (PROBLEM)")
print("=" * 60)

print("""
❌ WITHOUT try-except:
─────────────────────────────────────
# User ne number ki jagah "ibrahim" likh diya

a = int(input("Enter a Number: "))     ← ValueError!
# Program CRASH!
print(a + 10)                           ← Ye line kabhi chalegi nahi!

OUTPUT:
Enter a Number: ibrahim
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    a = int(input("Enter a Number: "))
ValueError: invalid literal for int() with base 10: 'ibrahim'

→ Program YAHIN RUK GAYA!
→ Baaki ka code execute NAHI hoga!
→ User ko ugly error message dikhi!


PROBLEMS WITHOUT EXCEPTION HANDLING:
❌ Program crash ho jata hai
❌ User ko confusing error messages dikhte hain
❌ Baaki ka code execute nahi hota
❌ Production mein bahut badi problem!
❌ User trust khatam ho jata hai
""")


# ============================================================
# PART 3: BASIC try-except (YOUR CODE)
# ============================================================

print("=" * 60)
print("📊 BASIC try-except (YOUR CODE)")
print("=" * 60)

print("""
✅ WITH try-except:
─────────────────────────────────────
try:
    a = int(input("Enter a Number: "))  ← Suspicious code
    print(a + 10)
except:
    print("Error Occured! Only Enter Number")  ← Error handler

→ Agar user number de → Normal execution
→ Agar user text de → except block chalega
→ Program CRASH NAHI hoga!
→ User ko friendly message milega!
""")


print("\n🔍 DEMONSTRATION:")
print("-" * 40)

try:
    a = int(input("Enter a Number: "))
    print(f"   ✅ Success! {a} + 10 = {a + 10}")
except:
    print("   ❌ Error Occured! Only Enter Number")

print("   ✅ Program continues... (Crash nahi hua!)")


# ------------------------ How It Works ------------------------

print("\n" + "-" * 40)
print("📊 HOW try-except WORKS (Flow):")
print("-" * 40)

print("""
EXECUTION FLOW:

1. Python enters try block
2. Executes code line by line
3. IF NO ERROR → except block SKIP, continue after
4. IF ERROR → Immediately JUMP to except block
5. After except → Continue with rest of program


VISUAL FLOW:

try:                          ← Step 1: Enter
    a = int(input(...))       ← Step 2: Execute
    print(a + 10)             ← Step 3: No error? Continue!
except:                       ← Step 4: Error? Jump here!
    print("Error...")         ← Step 5: Handle error
    
print("Done")                 ← Step 6: Always executes
""")


# ============================================================
# PART 4: CATCHING SPECIFIC EXCEPTIONS
# ============================================================

print("=" * 60)
print("📊 CATCHING SPECIFIC EXCEPTIONS")
print("=" * 60)

print("""
❌ BAD PRACTICE (Bare except):
─────────────────────────────────
try:
    # code
except:
    print("Error")
→ Ye SAB errors catch karega (ValueError, TypeError, etc.)
→ Kya error aaya, pata nahi chalega!
→ Debugging mushkil!


✅ GOOD PRACTICE (Specific except):
────────────────────────────────────
try:
    # code
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except FileNotFoundError:
    print("File not found!")
→ Specific error ke liye specific message!
→ Debugging easy!
""")


# Example: Multiple Specific Exceptions
print("\n🔍 Example: Multiple Specific Exceptions")
print("-" * 40)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"   ✅ {num1} / {num2} = {result}")

except ValueError:
    print("   ❌ ValueError: Please enter valid numbers only!")
    
except ZeroDivisionError:
    print("   ❌ ZeroDivisionError: Cannot divide by zero!")
    
except Exception as e:
    print(f"   ❌ Some other error: {e}")

print("   ✅ Program continues...")


# ============================================================
# PART 5: EXCEPTION AS e (YOUR CODE — ERROR MESSAGE)
# ============================================================

print("\n" + "=" * 60)
print("📊 EXCEPTION AS e (ERROR MESSAGE PRINT)")
print("=" * 60)

print("""
Exception as e:
→ e mein ERROR OBJECT store hota hai
→ e ko print karke actual error message dikha sakte hain
→ Debugging ke liye HELPFUL hai
→ Production mein user ko show NAHI karna chahiye!

SYNTAX:
try:
    # code
except Exception as e:
    print("Error:", e)           ← Error message print
""")


# Your Code Example
print("\n🔍 Your Code Example:")
print("-" * 40)

try:
    a = int(input("Enter a Number: "))
    print(f"   ✅ {a} + 10 = {a + 10}")
    
except Exception as e:
    print(f"   ❌ Error Occured! Only Enter Number")
    print(f"   📝 Technical Error: {e}")
    print(f"   📝 Error Type: {type(e).__name__}")

print("   ✅ Program continues...")


# ============================================================
# PART 6: ALL EXCEPTION BLOCKS (COMPLETE STRUCTURE)
# ============================================================

print("\n" + "=" * 60)
print("📊 COMPLETE try-except STRUCTURE")
print("=" * 60)

print("""
FULL SYNTAX:
┌─────────────────────────────────────────────┐
│ try:                                        │
│     # Suspicious code                       │
│                                             │
│ except SpecificError:                       │
│     # Handle specific error                 │
│                                             │
│ except AnotherError:                        │
│     # Handle another error                  │
│                                             │
│ except Exception as e:                      │
│     # Handle any other error                │
│                                             │
│ else:                                       │
│     # Runs if NO error                      │
│                                             │
│ finally:                                    │
│     # ALWAYS runs (error ho ya na ho)       │
└─────────────────────────────────────────────┘


🔹 try:      Code jo error de sakta hai
🔹 except:   Error handle karta hai (Multiple allowed)
🔹 else:     Sirf tab jab koi error NAHI aaya
🔹 finally:  HAMESHA execute hota hai
""")


# Example: Complete Structure
print("\n🔍 Complete try-except-else-finally:")
print("-" * 40)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    
except ValueError:
    print("   ❌ Please enter valid numbers!")
    
except ZeroDivisionError:
    print("   ❌ Cannot divide by zero!")
    
else:
    # Ye sirf tab chalega jab koi error NAHI aaya
    print(f"   ✅ Success! {num1} / {num2} = {result:.2f}")
    
finally:
    # Ye HAMESHA chalega
    print("   🔒 Resources cleaned up! (Finally block)")

print("   ✅ Program continues...")


# ============================================================
# PART 7: REAL LIFE EXCEPTION HANDLING EXAMPLES
# ============================================================

print("\n" + "=" * 60)
print("📊 REAL LIFE EXCEPTION HANDLING EXAMPLES")
print("=" * 60)


# Example 1: File Reading
print("\n🔍 EXAMPLE 1: File Reading")
print("-" * 40)

def read_file_safely(filename):
    """File ko safely read karo — crash nahi hoga!"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"   ✅ File '{filename}' read successfully!")
            print(f"   📄 First 50 chars: {content[:50]}...")
            return content
    except FileNotFoundError:
        print(f"   ❌ File '{filename}' not found!")
        print("   💡 Check file name or create new file.")
    except PermissionError:
        print(f"   ❌ Permission denied for '{filename}'!")
        print("   💡 Run as administrator.")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
    finally:
        print("   🔒 File operation completed.")

# Test
read_file_safely("data.txt")        # File nahi hogi
read_file_safely("students.txt")    # File nahi hogi


# Example 2: API/Network Request
print("\n\n🔍 EXAMPLE 2: Network Request")
print("-" * 40)

def fetch_data_from_api(url):
    """API se data safely fetch karo."""
    try:
        # Simulate network request
        import requests  # Agar installed hai
        print(f"   🌐 Connecting to {url}...")
        # response = requests.get(url, timeout=5)
        # response.raise_for_status()
        # print(f"   ✅ Data fetched! Status: {response.status_code}")
        
        # Simulate for demo (since requests may not be installed)
        raise ConnectionError("Simulated network error for demo")
        
    except ImportError:
        print("   ❌ 'requests' library not installed!")
        print("   💡 Run: pip install requests")
    except ConnectionError:
        print("   ❌ Network connection failed!")
        print("   💡 Check internet connection.")
    except TimeoutError:
        print("   ❌ Request timed out!")
        print("   💡 Server busy, try again later.")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    finally:
        print("   🔒 Request completed.")

fetch_data_from_api("https://api.example.com/data")


# Example 3: User Input Validation
print("\n\n🔍 EXAMPLE 3: User Input Validation")
print("-" * 40)

def get_age_safely():
    """User se age input lo — invalid input handle karo."""
    while True:
        try:
            age = int(input("   Enter your age: "))
            
            if age < 0:
                raise ValueError("Age cannot be negative!")
            if age > 150:
                raise ValueError("Age cannot be more than 150!")
                
            print(f"   ✅ Age accepted: {age}")
            return age
            
        except ValueError as e:
            print(f"   ❌ Invalid input! {e}")
            print("   💡 Please enter a valid number (0-150).")

# Test (Comment out for demo)
# age = get_age_safely()


# Example 4: Database Connection
print("\n\n🔍 EXAMPLE 4: Database Connection")
print("-" * 40)

def connect_to_database():
    """Database se safely connect karo."""
    connected = False
    try:
        # Simulate database connection
        print("   🔌 Connecting to database...")
        # db = sqlite3.connect("database.db")  # Real code
        # connected = True
        
        # Simulate error for demo
        raise ConnectionError("Database server not responding")
        
    except ConnectionError as e:
        print(f"   ❌ Connection failed: {e}")
        print("   💡 Check database server status.")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
    else:
        print("   ✅ Connected successfully!")
        connected = True
    finally:
        if not connected:
            print("   🔒 Connection resources cleaned up.")
        print("   🔒 Operation completed.")

connect_to_database()


# Example 5: Division Calculator
print("\n\n🔍 EXAMPLE 5: Safe Division Calculator")
print("-" * 40)

def safe_divide():
    """Do numbers ka safe division."""
    try:
        num1 = float(input("   Enter numerator: "))
        num2 = float(input("   Enter denominator: "))
        
        result = num1 / num2
        
    except ValueError:
        print("   ❌ Please enter valid numbers!")
        return None
    except ZeroDivisionError:
        print("   ❌ Cannot divide by zero! Infinity hota hai.")
        print("   💡 Denominator zero nahi ho sakta.")
        return None
    else:
        print(f"   ✅ {num1} / {num2} = {result:.2f}")
        return result
    finally:
        print("   🔒 Calculation completed.")

# Test
# safe_divide()


# ============================================================
# PART 8: COMMON EXCEPTIONS — HOW TO PREVENT
# ============================================================

print("\n" + "=" * 60)
print("📊 COMMON EXCEPTIONS & PREVENTION")
print("=" * 60)

print("""
┌──────────────────────┬─────────────────────────┬──────────────────────────┐
│ EXCEPTION            │ EXAMPLE                 │ HOW TO PREVENT           │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ ValueError           │ int("abc")              │ Validate input pehle     │
│                      │ float("hello")          │ .isdigit() check karo    │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ TypeError            │ 5 + "hello"             │ Type check karo          │
│                      │ len(5)                  │ isinstance() use karo    │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ ZeroDivisionError    │ 10 / 0                  │ Denominator check karo   │
│                      │ 10 % 0                  │ if denom != 0:           │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ IndexError           │ list[100]               │ len() check karo         │
│                      │ "hello"[10]             │ if index < len(list):    │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ KeyError             │ dict["nonexistent"]     │ .get() method use karo   │
│                      │                         │ if key in dict:          │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ AttributeError       │ "hello".push()          │ dir() se check karo      │
│                      │ 5.append()              │ hasattr() use karo       │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ FileNotFoundError    │ open("abc.txt")         │ os.path.exists() check   │
│                      │                         │ try-except best!         │
├──────────────────────┼─────────────────────────┼──────────────────────────┤
│ NameError            │ print(undefined_var)    │ Variable define karo     │
│                      │                         │ Spelling check karo      │
└──────────────────────┴─────────────────────────┴──────────────────────────┘
""")


# Prevention Examples
print("🔍 PREVENTION TECHNIQUES:")
print("-" * 40)

# 1. Prevent ValueError
print("\n1. PREVENT ValueError:")
user_input = "abc"
if user_input.isdigit():
    number = int(user_input)
    print(f"   ✅ Valid number: {number}")
else:
    print(f"   ❌ '{user_input}' is not a number!")

# 2. Prevent ZeroDivisionError
print("\n2. PREVENT ZeroDivisionError:")
numerator = 10
denominator = 0
if denominator != 0:
    result = numerator / denominator
    print(f"   ✅ Result: {result}")
else:
    print(f"   ❌ Cannot divide by zero!")

# 3. Prevent IndexError
print("\n3. PREVENT IndexError:")
my_list = [1, 2, 3]
index = 5
if index < len(my_list):
    print(f"   ✅ Value at index {index}: {my_list[index]}")
else:
    print(f"   ❌ Index {index} out of range! List length: {len(my_list)}")

# 4. Prevent KeyError
print("\n4. PREVENT KeyError:")
student = {"name": "Ibrahim", "age": 22}
key = "grade"
if key in student:
    print(f"   ✅ {key}: {student[key]}")
else:
    print(f"   ❌ Key '{key}' not found!")
    print(f"   💡 Using .get() → {student.get(key, 'Not Available')}")

# 5. Prevent AttributeError
print("\n5. PREVENT AttributeError:")
text = "Hello"
if hasattr(text, 'append'):
    text.append(" World")
else:
    print(f"   ❌ String has no 'append' method!")
    print(f"   💡 Use '+' instead: '{text + ' World'}'")


# ============================================================
# PART 9: CREATING CUSTOM EXCEPTIONS
# ============================================================

print("\n" + "=" * 60)
print("📊 CUSTOM EXCEPTIONS")
print("=" * 60)

print("""
Kabhi kabhi built-in exceptions enough nahi hote.
Tab hum APNI EXCEPTIONS bana sakte hain!

Real Life Use: Age validation, Password strength, etc.
""")

# Custom Exception Class
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

class WeakPasswordError(Exception):
    """Custom exception for weak passwords."""
    pass


def register_user(name, age, password):
    """User registration with custom exceptions."""
    try:
        # Age validation
        if age < 18:
            raise InvalidAgeError(f"Age must be 18+, got {age}")
        if age > 120:
            raise InvalidAgeError(f"Age seems invalid: {age}")
        
        # Password validation
        if len(password) < 6:
            raise WeakPasswordError("Password must be at least 6 characters!")
        if password.isalpha():
            raise WeakPasswordError("Password must contain numbers too!")
        
        print(f"   ✅ User '{name}' registered successfully!")
        
    except InvalidAgeError as e:
        print(f"   ❌ Age Error: {e}")
    except WeakPasswordError as e:
        print(f"   ❌ Password Error: {e}")
    except Exception as e:
        print(f"   ❌ Unexpected Error: {e}")


# Test Custom Exceptions
print("\n🔍 Testing Custom Exceptions:")
print("-" * 40)

register_user("Ibrahim", 22, "py123")       # ✅ Success
register_user("Ali", 15, "pass123")         # ❌ Age error
register_user("Sara", 25, "abc")            # ❌ Weak password
register_user("Ahmed", 25, "hello")         # ❌ No numbers


# ============================================================
# PART 10: BEST PRACTICES
# ============================================================

print("\n" + "=" * 60)
print("📊 BEST PRACTICES")
print("=" * 60)

print("""
✅ DO's:
  1. Specific exceptions catch karo (ValueError, not bare except)
  2. else block use karo (Code jo sirf success par chalna chahiye)
  3. finally block use karo (Resources clean up)
  4. Exception as e use karo (Debugging ke liye)
  5. Custom exceptions banao meaningful names ke saath
  6. User-friendly error messages dikhao
  7. Log errors for debugging (Production mein)
  8. try block ko chhota rakho (Sirf suspicious code)

❌ DON'Ts:
  1. Bare except: mat use karo (Bugs hide ho jate hain)
  2. except pass: mat karo (Error silently ignore!)
  3. Har line ko try-except mein mat wrap karo
  4. Error messages mein sensitive info mat dikhao
  5. Exception handling ko flow control ke liye use mat karo
  6. Production mein full traceback user ko mat dikhao
""")


# ============================================================
# PART 11: LOGGING ERRORS (ADVANCED)
# ============================================================

print("=" * 60)
print("📊 LOGGING ERRORS (Production Best Practice)")
print("=" * 60)

def safe_operation_with_logging():
    """Error ko log bhi karo, user ko friendly message bhi dikhao."""
    import logging
    
    # Logging setup
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app_errors.log'
    )
    
    try:
        # Some risky operation
        number = int(input("   Enter a number: "))
        result = 100 / number
        
    except ValueError as e:
        # Log the error (Developer ke liye)
        logging.error(f"ValueError: {e}")
        # User-friendly message (User ke liye)
        print("   ❌ Please enter a valid number!")
        
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError: {e}")
        print("   ❌ Cannot divide by zero!")
        
    else:
        print(f"   ✅ Result: {result}")
        
    finally:
        print("   🔒 Operation completed. Errors logged to 'app_errors.log'")

# Test
# safe_operation_with_logging()


# ============================================================
# PART 12: COMPLETE SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("📊 COMPLETE SUMMARY — EXCEPTION HANDLING")
print("=" * 60)

print("""
✅ WHAT IS EXCEPTION HANDLING?
   Program ko crash hone se bachane ka mechanism.
   Runtime errors ko gracefully handle karta hai.

✅ BASIC SYNTAX:
   try:
       # Risky code
   except SpecificError:
       # Handle error
   except Exception as e:
       # Handle any error (e = error object)
   else:
       # No error → This runs
   finally:
       # Always runs

✅ COMMON EXCEPTIONS:
   • ValueError         — Wrong value type
   • TypeError          — Wrong operation
   • ZeroDivisionError  — Divide by zero
   • IndexError         — List index out of range
   • KeyError           — Dict key not found
   • FileNotFoundError  — File doesn't exist
   • NameError          — Variable not defined
   • AttributeError     — Wrong method/attribute

✅ PREVENTION TECHNIQUES:
   • .isdigit() check before int()
   • if denom != 0: before division
   • if index < len(list): before access
   • .get() method for dictionaries
   • hasattr() for attributes

✅ REAL LIFE USE CASES:
   • File operations (read/write)
   • Network requests (API calls)
   • User input validation
   • Database connections
   • Payment processing

✅ BEST PRACTICES:
   ✅ Specific exceptions catch karo
   ✅ User-friendly messages dikhao
   ✅ finally mein resources clean karo
   ✅ Log errors for debugging
   ❌ Bare except: mat use karo
   ❌ Errors silently ignore mat karo
   ❌ Sensitive info user ko mat dikhao

✅ GOLDEN RULES:
   • try block jitna chhota ho sake, rakho
   • except block mein proper action lo
   • else mein success code rakho
   • finally mein cleanup rakho
   • Error messages meaningful rakho
""")


# ============================================================
# QUICK QUIZ
# ============================================================

print("\n" + "=" * 60)
print("📝 QUICK QUIZ — EXCEPTION HANDLING")
print("=" * 60)

print("""
Q1: Exception handling ka use kya hai?
A:  Program ko crash hone se bachana aur errors ko gracefully handle karna.

Q2: try-except ka basic syntax kya hai?
A:  try: (risky code) → except: (error handler)

Q3: Exception as e mein 'e' kya hai?
A:  Error object jisme error ka message hota hai.

Q4: else block kab chalta hai?
A:  Sirf tab jab try block mein koi error NAHI aaya.

Q5: finally block kab chalta hai?
A:  HAMESHA — error aaye ya na aaye.

Q6: 5 / 0 se kaunsa exception aata hai?
A:  ZeroDivisionError

Q7: int("abc") se kaunsa exception aata hai?
A:  ValueError

Q8: Bare except: kyun avoid karna chahiye?
A:  Sab errors catch karta hai, bugs hide kar deta hai, debugging mushkil.

Q9: User input validation ka best tareeqa kya hai?
A:  try-except with loop (jab tak sahi input na mile)

Q10: Production mein error user ko dikhana chahiye?
A:   Nahi! Sirf friendly message dikhao, technical details log karo.
""")