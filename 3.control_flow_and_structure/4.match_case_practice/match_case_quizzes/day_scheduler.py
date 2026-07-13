# ============================================================
# QUICK QUIZ 3: Day Scheduler
# ============================================================
# Write a Python program that asks the user to enter the name 
# of a day. Using match-case, display the scheduled activity 
# for that day. If the entered day is invalid, display an 
# appropriate error message.
# ============================================================


# ============================================================
# VERSION 1: BEGINNER FRIENDLY
# ============================================================
# Simple, har din ka alag case, easy to understand

print("=" * 40)
print("📅 DAY SCHEDULER (Beginner Version)")
print("=" * 40)

# Step 1: Din ka naam lo
print("\nValid Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")
day = input("Enter day of the week: ")

# Step 2: Capitalize karo (pehla letter bada)
day = day.capitalize()

# Step 3: Match-Case se schedule dikhao
match day:
    case "Monday":
        print("\n📅 MONDAY SCHEDULE:")
        print("   🌅 Morning: Wake up & Fajr prayer")
        print("   💻 9 AM: Python Learning")
        print("   📚 11 AM: University")
        print("   🍔 1 PM: Lunch break")
        print("   💻 5 PM: Coding practice")
        print("   😴 11 PM: Sleep")
        
    case "Tuesday":
        print("\n📅 TUESDAY SCHEDULE:")
        print("   🌅 Morning: Wake up & Fajr prayer")
        print("   💻 9 AM: Web Development")
        print("   📚 11 AM: University")
        print("   🍔 1 PM: Lunch break")
        print("   💻 5 PM: Mini projects")
        print("   😴 11 PM: Sleep")
        
    case "Wednesday":
        print("\n📅 WEDNESDAY SCHEDULE:")
        print("   🌅 Morning: Wake up & Fajr prayer")
        print("   💻 9 AM: Advanced Python")
        print("   📚 11 AM: University")
        print("   🍔 1 PM: Lunch break")
        print("   💻 5 PM: Problem solving")
        print("   😴 11 PM: Sleep")
        
    case "Thursday":
        print("\n📅 THURSDAY SCHEDULE:")
        print("   🌅 Morning: Wake up & Fajr prayer")
        print("   💻 9 AM: JavaScript")
        print("   📚 11 AM: University")
        print("   🍔 1 PM: Lunch break")
        print("   💻 5 PM: Group study")
        print("   😴 11 PM: Sleep")
        
    case "Friday":
        print("\n📅 FRIDAY SCHEDULE:")
        print("   🌅 Morning: Wake up & Fajr prayer")
        print("   📖 7 AM: Surah Kahf")
        print("   🕌 1:30 PM: Jummah prayer")
        print("   🍔 2:30 PM: Special lunch")
        print("   👨‍👩‍👧‍👦 5 PM: Family time")
        print("   🎬 9 PM: Movie night")
        
    case "Saturday":
        print("\n📅 SATURDAY SCHEDULE:")
        print("   🌅 7 AM: Wake up (thoda late!)")
        print("   💻 9:30 AM: Side projects")
        print("   🍔 1 PM: Lunch")
        print("   🏏 5 PM: Sports")
        print("   🎮 9 PM: Gaming time")
        
    case "Sunday":
        print("\n📅 SUNDAY SCHEDULE:")
        print("   🌅 8 AM: Wake up (late!)")
        print("   📝 10 AM: Week planning")
        print("   🍔 1 PM: Family lunch")
        print("   🛒 5 PM: Shopping")
        print("   😴 10 PM: Early sleep")
        
    case _:
        # Agar koi aur din likha
        print("\n❌ Invalid day!")
        print("   Please enter a valid day name.")
        print("   Example: Monday, Tuesday, etc.")


print("\n" + "=" * 60)


# ============================================================
# VERSION 2: BETTER VERSION
# ============================================================
# Function use kiya, code organized, schedule dictionary mein

print("\n📅 DAY SCHEDULER (Better Version)")
print("=" * 40)


def print_schedule(day: str, activities: list) -> None:
    """Print formatted schedule for a day."""
    print(f"\n📅 {day.upper()} SCHEDULE:")
    for activity in activities:
        print(f"   {activity}")


print("\nValid Days: Monday to Sunday")
day = input("Enter day of the week: ").capitalize()

match day:
    case "Monday":
        schedule = [
            "🌅 Morning: Wake up & Fajr",
            "💻 9 AM: Python Learning",
            "📚 11 AM: University",
            "💻 5 PM: Coding practice",
        ]
        print_schedule("Monday", schedule)
        
    case "Tuesday":
        schedule = [
            "🌅 Morning: Wake up & Fajr",
            "💻 9 AM: Web Development",
            "📚 11 AM: University",
            "💻 5 PM: Mini projects",
        ]
        print_schedule("Tuesday", schedule)
        
    case "Wednesday":
        schedule = [
            "🌅 Morning: Wake up & Fajr",
            "💻 9 AM: Advanced Python",
            "📚 11 AM: University",
            "💻 5 PM: Problem solving",
        ]
        print_schedule("Wednesday", schedule)
        
    case "Thursday":
        schedule = [
            "🌅 Morning: Wake up & Fajr",
            "💻 9 AM: JavaScript",
            "📚 11 AM: University",
            "💻 5 PM: Group study",
        ]
        print_schedule("Thursday", schedule)
        
    case "Friday":
        schedule = [
            "🌅 Morning: Wake up & Fajr",
            "📖 7 AM: Surah Kahf",
            "🕌 1:30 PM: Jummah prayer",
            "👨‍👩‍👧‍👦 5 PM: Family time",
        ]
        print_schedule("Friday", schedule)
        
    case "Saturday":
        schedule = [
            "🌅 7 AM: Wake up (late)",
            "💻 9:30 AM: Side projects",
            "🏏 5 PM: Sports",
            "🎮 9 PM: Gaming",
        ]
        print_schedule("Saturday", schedule)
        
    case "Sunday":
        schedule = [
            "🌅 8 AM: Wake up (late)",
            "📝 10 AM: Week planning",
            "🍔 1 PM: Family lunch",
            "😴 10 PM: Early sleep",
        ]
        print_schedule("Sunday", schedule)
        
    case _:
        print("\n❌ Invalid day! Please enter Monday-Sunday.")


print("\n" + "=" * 60)


# ============================================================
# VERSION 3: SENIOR DEV VERSION
# ============================================================
# Dictionary mapping, single match-case, professional structure

print("\n📅 DAY SCHEDULER (Senior Dev Version)")
print("=" * 40)

from typing import Optional

# Schedule data (Dictionary)
WEEKLY_SCHEDULE = {
    "Monday": {
        "type": "Weekday",
        "activities": [
            "🌅 6 AM: Wake up & Fajr prayer",
            "💻 9 AM: Python Learning",
            "📚 11 AM: University",
            "🍔 1 PM: Lunch break",
            "💻 5 PM: Coding practice",
            "😴 11 PM: Sleep"
        ],
        "motto": "New week, new goals! 🎯"
    },
    "Tuesday": {
        "type": "Weekday",
        "activities": [
            "🌅 6 AM: Wake up & Fajr prayer",
            "💻 9 AM: Web Development",
            "📚 11 AM: University",
            "🍔 1 PM: Lunch break",
            "💻 5 PM: Mini projects",
            "😴 11 PM: Sleep"
        ],
        "motto": "Consistency is key! 🔑"
    },
    "Wednesday": {
        "type": "Weekday",
        "activities": [
            "🌅 6 AM: Wake up & Fajr prayer",
            "💻 9 AM: Advanced Python",
            "📚 11 AM: University",
            "🍔 1 PM: Lunch break",
            "💻 5 PM: Problem solving",
            "😴 11 PM: Sleep"
        ],
        "motto": "Halfway through! 💪"
    },
    "Thursday": {
        "type": "Weekday",
        "activities": [
            "🌅 6 AM: Wake up & Fajr prayer",
            "💻 9 AM: JavaScript",
            "📚 11 AM: University",
            "🍔 1 PM: Lunch break",
            "💻 5 PM: Group study",
            "😴 11 PM: Sleep"
        ],
        "motto": "Keep learning! 📚"
    },
    "Friday": {
        "type": "Special",
        "activities": [
            "🌅 6 AM: Wake up & Fajr prayer",
            "📖 7 AM: Surah Kahf reading",
            "🕌 1:30 PM: Jummah prayer",
            "🍔 2:30 PM: Special lunch",
            "👨‍👩‍👧‍👦 5 PM: Family time",
            "🎬 9 PM: Movie night"
        ],
        "motto": "Jummah Mubarak! 🕌"
    },
    "Saturday": {
        "type": "Weekend",
        "activities": [
            "🌅 7 AM: Wake up (thoda late!)",
            "💻 9:30 AM: Side projects",
            "🍔 1 PM: Lunch",
            "🏏 5 PM: Outdoor sports",
            "🎮 9 PM: Gaming time"
        ],
        "motto": "Weekend vibes! 🎉"
    },
    "Sunday": {
        "type": "Weekend",
        "activities": [
            "🌅 8 AM: Wake up (late!)",
            "📝 10 AM: Plan next week",
            "🍔 1 PM: Family lunch",
            "🛒 5 PM: Shopping",
            "😴 10 PM: Early sleep"
        ],
        "motto": "Recharge for next week! 🔋"
    }
}


def get_day_schedule(day: str) -> Optional[dict]:
    """Retrieve schedule for a given day."""
    return WEEKLY_SCHEDULE.get(day, None)


def display_schedule(day: str, schedule: dict) -> None:
    """Display formatted schedule."""
    print(f"\n📅 {day.upper()} SCHEDULE ({schedule['type']})")
    print("-" * 30)
    for activity in schedule['activities']:
        print(f"   {activity}")
    print("-" * 30)
    print(f"💡 {schedule['motto']}")


def main():
    """Main function to run the day scheduler."""
    print("\nDays: Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday")
    day = input("Enter day of the week: ").strip().capitalize()
    
    schedule = get_day_schedule(day)
    
    match schedule:
        case dict():
            display_schedule(day, schedule)
        case None:
            print(f"\n❌ '{day}' is not a valid day!")
            print("   Please enter: Monday, Tuesday, Wednesday, etc.")


if __name__ == "__main__":
    main()