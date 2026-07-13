# 🎮 Game Controller — Match-Case Practice
# Real Life Scenario: Keyboard controls se game character control karna

print("=" * 40)
print("🎮 PYTHON GAME CONTROLLER")
print("=" * 40)

# Game State
player_name = "Hero"
player_health = 100
player_position = [0, 0]  # [x, y]
player_score = 0
inventory = []

print(f"\n👤 Player: {player_name}")
print(f"❤️  Health: {player_health}")
print(f"📍 Position: ({player_position[0]}, {player_position[1]})")
print(f"🏆 Score: {player_score}")

print("\n" + "-" * 40)
print("🎯 CONTROLS:")
print("W — Move Up")
print("S — Move Down")
print("A — Move Left")
print("D — Move Right")
print("F — Fight Enemy")
print("I — Open Inventory")
print("H — Heal")
print("Q — Quit Game")
print("-" * 40)

# Game Loop
game_running = True

while game_running:
    command = input("\n🎮 Enter command: ").upper()
    
    match command:
        case "W":
            player_position[1] += 1
            print(f"⬆️  Moving UP... New Position: ({player_position[0]}, {player_position[1]})")
            player_score += 5
            
        case "S":
            player_position[1] -= 1
            print(f"⬇️  Moving DOWN... New Position: ({player_position[0]}, {player_position[1]})")
            player_score += 5
            
        case "A":
            player_position[0] -= 1
            print(f"⬅️  Moving LEFT... New Position: ({player_position[0]}, {player_position[1]})")
            player_score += 5
            
        case "D":
            player_position[0] += 1
            print(f"➡️  Moving RIGHT... New Position: ({player_position[0]}, {player_position[1]})")
            player_score += 5
            
        case "F":
            print("⚔️  Fighting Enemy...")
            
            # Enemy types
            import random
            enemy_type = random.choice(["goblin", "skeleton", "dragon", "slime"])
            
            match enemy_type:
                case "goblin":
                    damage = 10
                    points = 50
                    loot = "Gold Coin"
                    print(f"   👺 Goblin appeared! (-{damage} HP)")
                    
                case "skeleton":
                    damage = 15
                    points = 75
                    loot = "Bone Armor"
                    print(f"   💀 Skeleton appeared! (-{damage} HP)")
                    
                case "dragon":
                    damage = 30
                    points = 200
                    loot = "Dragon Scale"
                    print(f"   🐉 Dragon appeared! (-{damage} HP)")
                    
                case "slime":
                    damage = 5
                    points = 25
                    loot = "Slime Gel"
                    print(f"   🟢 Slime appeared! (-{damage} HP)")
                    
            player_health -= damage
            player_score += points
            inventory.append(loot)
            
            print(f"   ✅ Enemy defeated! +{points} points")
            print(f"   🎁 Loot: {loot}")
            
            if player_health <= 0:
                print(f"\n💀 {player_name} has been defeated!")
                print(f"🏆 Final Score: {player_score}")
                game_running = False
                
        case "I":
            print("\n🎒 INVENTORY:")
            if inventory:
                for i, item in enumerate(inventory, 1):
                    print(f"   {i}. {item}")
            else:
                print("   (Empty)")
                
        case "H":
            if "Health Potion" in inventory:
                player_health = min(100, player_health + 30)
                inventory.remove("Health Potion")
                print(f"🧪 Used Health Potion! +30 HP")
                print(f"❤️  Health: {player_health}")
            else:
                print("❌ No Health Potion in inventory!")
                print("💡 Defeat enemies to find items!")
                
        case "Q":
            print(f"\n👋 Thanks for playing, {player_name}!")
            print(f"🏆 Final Score: {player_score}")
            print(f"🎒 Items Collected: {len(inventory)}")
            game_running = False
            
        case _:
            print("❌ Invalid command! Use W, A, S, D, F, I, H, Q")

print("\n🎮 Game Over! Come back soon!")