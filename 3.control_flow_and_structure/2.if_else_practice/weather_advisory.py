# 🌤️ Weather Advisory System
# Real Life Scenario: Temperature ke hisaab se advice dena

print("=" * 40)
print("🌤️  WEATHER ADVISORY SYSTEM")
print("=" * 40)

# City aur Temperature input
city = input("Enter Your City Name: ")
temperature = int(input(f"Enter {city}'s Temperature (°C): "))

print(f"\n{city} Weather Report:")
print("-" * 30)

# Temperature Categories
if temperature > 45:
    category = "🔥 EXTREME HEAT"
    advice = [
        "Ghar ke andar rahein!",
        "AC ya cooler chalao.",
        "Din mein bahar na niklein (12 PM - 4 PM).",
        "Zyada se zyada pani piyo (8-10 glass).",
        "Heat stroke ka khatra hai!"
    ]
    emoji = "🥵"
    
elif temperature > 35:
    category = "☀️ VERY HOT"
    advice = [
        "Halka aur loose kapda pehno.",
        "Sunscreen lagao.",
        "Pani zyada piyo.",
        "Dhoop mein zyada der na raho."
    ]
    emoji = "😎"
    
elif temperature > 25:
    category = "🌤️ WARM"
    advice = [
        "Weather pleasant hai!",
        "Ghoomne ja sakte hain.",
        "Halka kapda pehno.",
        "Picnic ka plan banao!"
    ]
    emoji = "🌤️"
    
elif temperature > 15:
    category = "🍂 PLEASANT"
    advice = [
        "Bahut accha weather hai!",
        "Morning walk ke liye perfect.",
        "Outdoor activities enjoy karo.",
        "Park mein time bitao."
    ]
    emoji = "🍂"
    
elif temperature > 5:
    category = "🧥 COLD"
    advice = [
        "Garam kapde pehno.",
        "Jacket ya sweater zaroor pehno.",
        "Garam cheezein khao/piyo.",
        "Raat mein zyada thand ho sakti hai."
    ]
    emoji = "🧥"
    
else:
    category = "❄️ VERY COLD"
    advice = [
        "Heater chalao!",
        "Bahar mat niklo agar zaroori na ho.",
        "Garam kapdon ki layers pehno.",
        "Garam soup/tea piyo.",
        "Skin dry ho sakti hai, moisturizer lagao."
    ]
    emoji = "❄️"

# Output
print(f"Temperature: {temperature}°C {emoji}")
print(f"Category:    {category}")
print("\n📋 ADVISORY:")
for i, tip in enumerate(advice, 1):
    print(f"  {i}. {tip}")

print(f"\nStay safe, {city}! 🌍")