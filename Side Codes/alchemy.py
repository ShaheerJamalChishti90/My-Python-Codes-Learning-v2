import time
import random
import json
from functools import reduce

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

story_intro = """
Welcome, Alchemist.
In this world of code and magic,
you must brew potions using the ancient power of... PYTHON!
Each potion unlocks a new mystery...
"""

# === LOGGING FUNCTION ===
def log_potion(potion_name):
    with open("brew_log.txt", "a") as f:
        f.write(f"- {potion_name} brewed successfully!\n")

# === LAB PUZZLES ===

def list_potion():
    print("\n🧪 [POTION: List Elixir]")
    print("Create a list of 5 ingredients and reverse it.")
    ingredients = []
    for i in range(5):
        item = input(f"Enter ingredient {i+1}: ")
        ingredients.append(item)
    print("Original list:", ingredients)
    print("Reversed list:", ingredients[::-1])
    log_potion("List Elixir")
    return True

def open_ended_puzzle():
    print("\n🧪 [POTION: Open-Ended Flask]")
    print("Create a function that returns the sum of all even numbers in a list.")
    code = input("Write your function here (e.g., def sum_evens(lst): ...): ")
    try:
        exec(code)
        test_list = [1, 2, 3, 4, 5]
        if 'sum_evens' in locals():
            if locals()['sum_evens'](test_list) == 6:
                print("✅ Success! Magic flows through your function.")
                log_potion("Open-Ended Flask")
                return True
            else:
                print("❌ Function exists but logic failed.")
                return False
        else:
            print("❌ No function named sum_evens found.")
            return False
    except Exception as e:
        print("⚠️ Error in code:", e)
        return False

def search_sort_potion():
    print("\n🧪 [POTION: Sort & Seek Tonic]")
    nums = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted Numbers:", nums)
    nums.sort()
    print("Sorted Numbers:", nums)
    target = int(input("Enter a number to search: "))
    if target in nums:
        index = nums.index(target)
        print(f"Found {target} at index {index}")
        log_potion("Sort & Seek Tonic")
        return True
    else:
        print("Number not found. Try again.")
        return False

def tuple_dict_potion():
    print("\n🧪 [POTION: Tuple & Dictionary Draught]")
    hero_stats = ("Hero", 100, "Fire")
    name, hp, element = hero_stats
    print(f"Hero Info: Name={name}, HP={hp}, Element={element}")

    inventory = {
        "Health Potion": 3,
        "Mana Crystal": 2,
        "Sword": 1
    }
    print("Inventory:", inventory)
    key = input("Which item to use? ")
    if key in inventory:
        inventory[key] -= 1
        if inventory[key] <= 0:
            del inventory[key]
        print("Updated Inventory:", inventory)
        log_potion("Tuple & Dictionary Draught")
        return True
    else:
        print("Item not found.")
        return False

def module_package_potion():
    print("\n🧪 [POTION: Module & Package Elixir]")
    print("Import math and calculate square root of 144:")
    import math
    result = math.sqrt(144)
    print("Result:", result)
    log_potion("Module & Package Elixir")
    return True

def string_potion():
    print("\n🧪 [POTION: String Spell]")
    text = input("Enter a sentence: ")
    words = text.split()
    capitalized = ' '.join(word.capitalize() for word in words)
    reversed_text = text[::-1]
    print("Capitalized:", capitalized)
    print("Reversed:", reversed_text)
    log_potion("String Spell")
    return True

def file_potion():
    print("\n🧪 [POTION: File Essence]")
    data = {"score": 99, "player": "Alchemist"}
    with open("save_game.json", "w") as f:
        json.dump(data, f)
    print("Game saved!")

    with open("save_game.json", "r") as f:
        loaded = json.load(f)
    print("Loaded save:", loaded)
    log_potion("File Essence")
    return True

def exception_potion():
    print("\n🧪 [POTION: Exception Ward]")
    print("Try dividing two numbers. Handle any errors.")
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
        log_potion("Exception Ward")
        return True
    except ZeroDivisionError:
        print("🚫 Cannot divide by zero!")
        return False
    except ValueError:
        print("🚫 Invalid input. Must be numbers.")
        return False

# === MAIN GAME LOOP ===
def main():
    clear()
    print(title_art)
    print(story_intro)
    delay(2)

    name = input("Enter your alchemist name: ")
    print(f"\n🧙‍♂️ Welcome, {name}. Let's begin your journey...\n")
    delay(1)

    puzzles = [
        ("List Elixir", list_potion),
        ("Open-Ended Flask", open_ended_puzzle),
        ("Sort & Seek Tonic", search_sort_potion),
        ("Tuple & Dictionary Draught", tuple_dict_potion),
        ("Module & Package Elixir", module_package_potion),
        ("String Spell", string_potion),
        ("File Essence", file_potion),
        ("Exception Ward", exception_potion),
    ]

    for potion_name, func in puzzles:
        print("\n----------------------------------------")
        print(f"Brewing: {potion_name}")
        success = func()
        if not success:
            print("💀 Failed to brew potion. Game Over.")
            break
        else:
            print(f"✨ {potion_name} successfully brewed!")

    print("\n🎉 You've completed the Codex of Infinite Brews! 🎉")
    print("Thanks for playing, Alchemist.")

if __name__ == "__main__":
    main()