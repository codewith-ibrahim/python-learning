# 🏧 ATM Machine — Match-Case Practice
# Real Life Scenario: ATM se paise nikalna

print("=" * 40)
print("🏧 WELCOME TO PYTHON ATM")
print("=" * 40)

# User account setup
account_pin = 1234
account_balance = 50000
account_name = "Shaikh Muhammad Ibrahim"

# Login
print("\n🔐 Please enter your PIN:")
pin = int(input("PIN: "))

match pin:
    case 1234:
        print(f"\n✅ Welcome, {account_name}!")
        print(f"💰 Current Balance: Rs. {account_balance}")
        
        # ATM Menu
        print("\n" + "-" * 30)
        print("📋 SELECT OPTION:")
        print("1. Fast Cash")
        print("2. Withdraw Amount")
        print("3. Balance Inquiry")
        print("4. Mini Statement")
        print("-" * 30)
        
        option = input("Enter option (1-4): ")
        
        match option:
            case "1":
                print("\n💵 FAST CASH:")
                print("1. Rs. 500")
                print("2. Rs. 1000")
                print("3. Rs. 2000")
                print("4. Rs. 5000")
                
                fast_cash = input("Choose amount (1-4): ")
                
                match fast_cash:
                    case "1":
                        amount = 500
                    case "2":
                        amount = 1000
                    case "3":
                        amount = 2000
                    case "4":
                        amount = 5000
                    case _:
                        amount = 0
                        print("❌ Invalid choice!")
                
                if amount > 0 and amount <= account_balance:
                    account_balance -= amount
                    print(f"✅ Rs. {amount} withdrawn successfully!")
                    print(f"💰 Remaining Balance: Rs. {account_balance}")
                    print("📄 Please collect your cash.")
                elif amount > account_balance:
                    print("❌ Insufficient balance!")
                    
            case "2":
                amount = int(input("\nEnter amount: Rs. "))
                
                match amount:
                    case a if a <= 0:
                        print("❌ Invalid amount!")
                    case a if a > account_balance:
                        print(f"❌ Insufficient balance! You have Rs. {account_balance}")
                    case a if a % 500 != 0:
                        print("❌ Please enter amount in multiples of 500!")
                    case _:
                        account_balance -= amount
                        print(f"✅ Rs. {amount} withdrawn successfully!")
                        print(f"💰 Remaining Balance: Rs. {account_balance}")
                        print("📄 Please collect your cash.")
                        
            case "3":
                print(f"\n💰 Your Balance: Rs. {account_balance}")
                print(f"📅 Last Transaction: Today")
                
            case "4":
                print("\n📄 MINI STATEMENT:")
                print("-" * 30)
                print("Today:")
                print("  Opening Balance:  Rs. 50,000")
                if account_balance < 50000:
                    print(f"  Withdrawal:      -Rs. {50000 - account_balance}")
                print(f"  Closing Balance:  Rs. {account_balance}")
                print("-" * 30)
                
            case _:
                print("❌ Invalid option!")
                
    case 1111 | 2222 | 3333:
        # Common wrong PINs hint
        print("❌ Wrong PIN! Try your actual PIN.")
        
    case _:
        print("❌ Incorrect PIN! Access Denied.")
        print("🔒 Your account has been locked for security.")
        print("   Please contact bank: 1800-123-4567")

print("\n🙏 Thank you for using Python ATM!")