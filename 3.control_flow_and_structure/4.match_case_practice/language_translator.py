# 🌐 Simple Language Translator — Match-Case Practice
# Real Life Scenario: Words ko different languages mein translate karna

print("=" * 40)
print("🌐 PYTHON TRANSLATOR")
print("=" * 40)

print("\n📋 Available Languages:")
print("1. English to Urdu")
print("2. English to Arabic")
print("3. English to Turkish")
print("4. English to Spanish")
print("5. English to French")

choice = input("\nChoose translation direction (1-5): ")

match choice:
    case "1":
        print("\n🇵🇰 ENGLISH → URDU")
        print("Common words: hello, thanks, love, book, water")
        
        word = input("Enter English word: ").lower()
        
        match word:
            case "hello":
                print("📝 Urdu: السلام علیکم (Assalam O Alaikum)")
            case "thanks":
                print("📝 Urdu: شکریہ (Shukriya)")
            case "love":
                print("📝 Urdu: محبت (Mohabbat)")
            case "book":
                print("📝 Urdu: کتاب (Kitaab)")
            case "water":
                print("📝 Urdu: پانی (Paani)")
            case "friend":
                print("📝 Urdu: دوست (Dost)")
            case "food":
                print("📝 Urdu: کھانا (Khaana)")
            case "mother":
                print("📝 Urdu: ماں (Maa)")
            case "father":
                print("📝 Urdu: باپ (Baap)")
            case "brother":
                print("📝 Urdu: بھائی (Bhai)")
            case _:
                print("❌ Word not in database yet!")
                print("💡 Try: hello, thanks, love, book, water")
                
    case "2":
        print("\n🇸🇦 ENGLISH → ARABIC")
        
        word = input("Enter English word: ").lower()
        
        match word:
            case "hello":
                print("📝 Arabic: السلام علیکم (As-Salaam-Alaikum)")
            case "thanks":
                print("📝 Arabic: شكرا (Shukran)")
            case "love":
                print("📝 Arabic: حب (Hubb)")
            case "book":
                print("📝 Arabic: کتاب (Kitaab)")
            case "water":
                print("📝 Arabic: ماء (Maa)")
            case "friend":
                print("📝 Arabic: صدیق (Sadeeq)")
            case "peace":
                print("📝 Arabic: سلام (Salaam)")
            case "god":
                print("📝 Arabic: الله (Allah)")
            case _:
                print("❌ Word not in database yet!")
                
    case "3":
        print("\n🇹🇷 ENGLISH → TURKISH")
        
        word = input("Enter English word: ").lower()
        
        match word:
            case "hello":
                print("📝 Turkish: Merhaba")
            case "thanks":
                print("📝 Turkish: Teşekkürler")
            case "love":
                print("📝 Turkish: Aşk")
            case "book":
                print("📝 Turkish: Kitap")
            case "water":
                print("📝 Turkish: Su")
            case "friend":
                print("📝 Turkish: Arkadaş")
            case "goodbye":
                print("📝 Turkish: Hoşça kal")
            case _:
                print("❌ Word not in database yet!")
                
    case "4":
        print("\n🇪🇸 ENGLISH → SPANISH")
        
        word = input("Enter English word: ").lower()
        
        match word:
            case "hello":
                print("📝 Spanish: Hola")
            case "thanks":
                print("📝 Spanish: Gracias")
            case "love":
                print("📝 Spanish: Amor")
            case "book":
                print("📝 Spanish: Libro")
            case "water":
                print("📝 Spanish: Agua")
            case "friend":
                print("📝 Spanish: Amigo")
            case "goodbye":
                print("📝 Spanish: Adiós")
            case _:
                print("❌ Word not in database yet!")
                
    case "5":
        print("\n🇫🇷 ENGLISH → FRENCH")
        
        word = input("Enter English word: ").lower()
        
        match word:
            case "hello":
                print("📝 French: Bonjour")
            case "thanks":
                print("📝 French: Merci")
            case "love":
                print("📝 French: Amour")
            case "book":
                print("📝 French: Livre")
            case "water":
                print("📝 French: Eau")
            case "friend":
                print("📝 French: Ami")
            case "goodbye":
                print("📝 French: Au revoir")
            case _:
                print("❌ Word not in database yet!")
                
    case _:
        print("❌ Invalid choice! Please select 1-5.")

print("\n🌟 Thank you for using Python Translator!")
print("💡 Tip: More words coming soon!")