import time
import random
import json

# === UTILITY FUNCTIONS ===
def delay(seconds=1):
    time.sleep(seconds)

def clear():
    print("\n" * 50)

# === ASCII ART ===
title_art = """
   _____ _             _ _          _   
  |_   _| |__   ___   | (_)______ _| |_ 
    | | | '_ \ / _ \  | | |_  / _` | __|
    | | | | | | (_) | | | |/ / (_| | |_ 
    |_| |_| |_|\___/  |_|_/___\__,_|\__|
"""

intro_text = """
🔮 Welcome to The Oracle of Code 🔮
A realm where fate is written in loops,
and destiny flows through data types.
Ask wisely...
"""

# === LOGGING FORTUNE ===
def log_fortune(msg):
    with open("fortunes.log", "a") as f:
        f.write(msg + "\n")

# === LAB PUZZLES ===

def list_fortune():
    print("\n📜 [Fortune #1: List of Fates]")
    print("The Oracle whispers: Reveal your past by listing 5 memories.")
    memories = []
    for i in range(5):
        mem = input(f"Memory {i+1}: ")
        memories.append(mem)
    print("\nYour Past:", memories)
    print("Reversed Fate:", memories[::-1])
    log_fortune("[List] Memories revealed.")
    return True

def open_ended_challenge():
    print("\n🧩 [Fortune #2: Open-Ended Riddle]")
    print("Solve this mystery: Create a function that returns the average of a list.")
    code = input("Write it here (e.g., def avg(lst): ...): ")
    try:
        exec(code)
        test_list = [10, 20, 30]
        if 'avg' in locals():
            result = locals()['avg'](test_list)
            if result == 20.0:
                print("✨ Magic aligns. Your function works!")
                log_fortune("[Open-Ended] Average function created.")
                return True
            else:
                print("❌ Function exists but logic failed.")
                return False
        else:
            print("❌ No function named avg found.")
            return False
    except Exception as e:
        print("⚠️ Error in code:", e)
        return False

def search_sort_fate():
    print("\n🔍 [Fortune #3: Seek & Sort Destiny]")
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Oracle sees chaos:", nums)
    nums.sort()
    print("Sorted Vision:", nums)
    target = int(input("Which number do you seek? "))
    if target in nums:
        index = nums.index(target)
        print(f"Found {target} at position {index}")
        log_fortune("[Search/Sort] Number found.")
        return True
    else:
        print("That fate is not meant for you.")
        return False

def tuple_dict_fortune():
    print("\n📓 [Fortune #4: Tuple & Dictionary Insight]")
    hero = ("Knight", 90, "Light")
    name, power, alignment = hero
    print(f"Hero: {name}, Power: {power}, Alignment: {alignment}")

    inventory = {
        "Sword": 1,
        "Potion": 3,
        "Scroll": 2
    }
    print("Inventory:", inventory)
    item = input("Use an item: ")
    if item in inventory:
        inventory[item] -= 1
        if inventory[item] <= 0:
            del inventory[item]
        print("Updated Inventory:", inventory)
        log_fortune("[Tuple/Dict] Item used.")
        return True
    else:
        print("Item not found.")
        return False

def module_package_spell():
    print("\n📦 [Fortune #5: Module Mystery]")
    print("To see the stars, import math and calculate sqrt(64)")
    import math
    result = math.sqrt(64)
    print("Result:", result)
    log_fortune("[Module] Math imported.")
    return True

def string_fortune():
    print("\n🔤 [Fortune #6: String Prophecy]")
    text = input("Speak your wish: ")
    words = text.split()
    title_case = ' '.join(word.capitalize() for word in words)
    reversed_text = text[::-1]
    print("Prophecy Revealed:", title_case)
    print("Secret Message:", reversed_text)
    log_fortune("[String] Wish spoken.")
    return True

def file_fortune():
    print("\n💾 [Fortune #7: Eternal Record]")
    data = {"player": "Seeker", "score": 100}
    with open("save.json", "w") as f:
        json.dump(data, f)
    print("Future saved!")

    with open("save.json", "r") as f:
        loaded = json.load(f)
    print("Past Reading:", loaded)
    log_fortune("[File] Future recorded.")
    return True

def exception_fortune():
    print("\n🚫 [Fortune #8: Divine Protection]")
    print("Test the gods: Divide two numbers. Beware zero.")
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        result = a / b
        print("Divine Answer:", result)
        log_fortune("[Exception] Division successful.")
        return True
    except ZeroDivisionError:
        print("🔥 You dared divide by zero! The gods are angry.")
        return False
    except ValueError:
        print("🧙 Input must be numbers!")
        return False

# === MAIN GAME LOOP ===
def main():
    clear()
    print(title_art)
    print(intro_text)
    delay(2)

    name = input("What is your name, seeker? ")
    print(f"\n🔮 Greetings, {name}. Ask the Oracle...\n")
    delay(1)

    fortunes = [
        ("📜 List of Fates", list_fortune),
        ("🧩 Open-Ended Riddle", open_ended_challenge),
        ("🔍 Seek & Sort Destiny", search_sort_fate),
        ("📓 Tuple & Dictionary Insight", tuple_dict_fortune),
        ("📦 Module Mystery", module_package_spell),
        ("🔤 String Prophecy", string_fortune),
        ("💾 Eternal Record", file_fortune),
        ("🚫 Divine Protection", exception_fortune),
    ]

    for fortune_name, func in fortunes:
        print("\n----------------------------------------")
        print(f"{fortune_name}")
        success = func()
        if not success:
            print("💀 Your fate is lost...")
            break
        else:
            print(f"✨ {fortune_name} completed!")

    print("\n🌟 Your full destiny has been revealed. Farewell, Seeker.")
    log_fortune(f"[END] {name} completed their journey.")

if __name__ == "__main__":
    main()