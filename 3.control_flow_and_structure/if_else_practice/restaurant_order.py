# 🍽️ Restaurant Ordering System
# Real Life Scenario: Restaurant se khana order karna

print("=" * 40)
print("🍽️  PYTHON RESTAURANT")
print("=" * 40)

# Menu Display
print("\n📋 MENU:")
print("-" * 25)
print("1. Biryani       Rs. 250")
print("2. Burger        Rs. 150")
print("3. Pizza         Rs. 500")
print("4. Cold Drink    Rs. 80")
print("5. Ice Cream     Rs. 100")
print("-" * 25)

# Order
choice = int(input("\nEnter your choice (1-5): "))
quantity = int(input("Enter quantity: "))

print("\nProcessing your order...\n")

# Order Processing
if choice == 1:
    item = "Biryani 🍛"
    price = 250
elif choice == 2:
    item = "Burger 🍔"
    price = 150
elif choice == 3:
    item = "Pizza 🍕"
    price = 500
elif choice == 4:
    item = "Cold Drink 🥤"
    price = 80
elif choice == 5:
    item = "Ice Cream 🍦"
    price = 100
else:
    item = None
    print("❌ Invalid choice! 1-5 ke beech mein choose karein.")

if item:
    total = price * quantity
    
    # Discount Logic
    discount = 0
    if total > 1000:
        discount = total * 0.10  # 10% discount
        print("🎉 Congratulations! 10% discount applied!")
    
    final_amount = total - discount

    # Bill
    print("=" * 40)
    print("🧾 BILL")
    print("=" * 40)
    print(f"Item:      {item}")
    print(f"Price:     Rs. {price} x {quantity}")
    print(f"Subtotal:  Rs. {total}")
    if discount > 0:
        print(f"Discount:  -Rs. {int(discount)}")
    print("-" * 25)
    print(f"Total:     Rs. {int(final_amount)}")
    print("=" * 40)
    print("🍽️  Thank you! Visit Again!")