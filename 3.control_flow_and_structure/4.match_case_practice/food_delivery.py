# 🛵 Food Delivery Status — Match-Case Practice
# Real Life Scenario: Food delivery app order tracking

print("=" * 50)
print("🛵 PYTHON FOOD DELIVERY")
print("=" * 50)

# Restaurant Selection
print("\n🍽️  SELECT RESTAURANT:")
print("1. Biryani House")
print("2. Pizza Corner")
print("3. Burger King")
print("4. Desi Dhaba")

restaurant = input("Choose restaurant (1-4): ")

match restaurant:
    case "1":
        restaurant_name = "Biryani House"
        menu = {
            "1": ("Chicken Biryani", 250),
            "2": ("Mutton Biryani", 350),
            "3": ("Vegetable Biryani", 200),
            "4": ("Biryani + Drink Combo", 300)
        }
    case "2":
        restaurant_name = "Pizza Corner"
        menu = {
            "1": ("Small Pizza", 400),
            "2": ("Medium Pizza", 600),
            "3": ("Large Pizza", 800),
            "4": ("Pizza + Cold Drink", 650)
        }
    case "3":
        restaurant_name = "Burger King"
        menu = {
            "1": ("Zinger Burger", 350),
            "2": ("Beef Burger", 300),
            "3": ("Chicken Burger", 250),
            "4": ("Burger Meal", 500)
        }
    case "4":
        restaurant_name = "Desi Dhaba"
        menu = {
            "1": ("Daal Chawal", 150),
            "2": ("Chicken Karahi", 500),
            "3": ("Nihari", 300),
            "4": ("Seekh Kabab", 200)
        }
    case _:
        print("❌ Invalid restaurant!")
        exit()

# Display Menu
print(f"\n📋 {restaurant_name} MENU:")
print("-" * 30)
for key, (item, price) in menu.items():
    print(f"{key}. {item:25} Rs. {price}")
print("-" * 30)

# Order
item_choice = input("Choose item (1-4): ")

match item_choice:
    case "1" | "2" | "3" | "4":
        selected_item, item_price = menu[item_choice]
        
        quantity = int(input("Quantity: "))
        total = item_price * quantity
        
        # Delivery options
        print("\n🚚 DELIVERY OPTION:")
        print("1. Standard (30-45 min)  — Free")
        print("2. Express (15-20 min)   — Rs. 50")
        print("3. Super Fast (5-10 min)  — Rs. 100")
        
        delivery = input("Choose delivery (1-3): ")
        
        match delivery:
            case "1":
                delivery_time = "30-45 minutes"
                delivery_charge = 0
                delivery_type = "Standard"
            case "2":
                delivery_time = "15-20 minutes"
                delivery_charge = 50
                delivery_type = "Express"
            case "3":
                delivery_time = "5-10 minutes"
                delivery_charge = 100
                delivery_type = "Super Fast"
            case _:
                print("❌ Invalid! Defaulting to Standard delivery.")
                delivery_time = "30-45 minutes"
                delivery_charge = 0
                delivery_type = "Standard"
        
        # Payment
        final_total = total + delivery_charge
        
        print("\n" + "=" * 50)
        print("🧾 ORDER SUMMARY")
        print("=" * 50)
        print(f"Restaurant:  {restaurant_name}")
        print(f"Item:        {selected_item}")
        print(f"Quantity:    {quantity}x")
        print(f"Item Total:  Rs. {total}")
        print(f"Delivery:    {delivery_type} (+Rs. {delivery_charge})")
        print("-" * 30)
        print(f"TOTAL:       Rs. {final_total}")
        print("=" * 50)
        
        payment = input("\n💳 Payment method (cash/card/jazzcash): ").lower()
        
        match payment:
            case "cash":
                print("💵 Cash on Delivery selected.")
            case "card":
                print("💳 Card payment processing... ✅ Done!")
            case "jazzcash":
                print("📱 JazzCash payment processing... ✅ Done!")
            case _:
                print("💵 Default: Cash on Delivery")
        
        # Order Status Tracking
        print("\n📦 ORDER STATUS:")
        print("-" * 30)
        
        import time
        
        statuses = ["Order Received ✅", "Preparing Food 🔪", "Food Ready 🍽️", 
                    "Rider Picked Up 🛵", "On The Way 🛵💨", "Near Your Location 📍"]
        
        for status in statuses:
            print(f"  {status}")
            time.sleep(0.5)  # Simulate waiting (Half second)
        
        print(f"\n🛵 Estimated Delivery: {delivery_time}")
        print(f"📍 Delivering to: Your Location")
        print(f"👤 Rider: Ahmed (0312-3456789)")
        print(f"\n🍽️  Enjoy your {selected_item} from {restaurant_name}!")
        
    case _:
        print("❌ Invalid item choice!")

print("\n🙏 Thank you for ordering with Python Food Delivery!")
print("⭐ Please rate your experience!")