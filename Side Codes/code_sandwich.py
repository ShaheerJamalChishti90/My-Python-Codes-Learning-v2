# The 8-Layer Code Sandwich 🥪

sandwich = []

print("Welcome to the 8-Layer Code Sandwich!\n")

# Lab 08: Lists
sandwich.append("Bread Base")
print("1. List Layer:", sandwich)

# Lab 09: Open-Ended (custom logic)
filling = input("2. Add your favorite filling: ")
sandwich.append(filling)

# Lab 10: Searching & Sorting
sandwich += ["Lettuce", "Tomato", "Cheese"]
sandwich.sort()
print("3. Sorted Veggies:", sandwich)

# Lab 11: Tuples & Dictionaries
ingredients = ("Onion", "Pickles")
sandwich.append(ingredients)
info = {"name": "Code Sandwich", "layers": len(sandwich)}
print("4. Tuple Layer + Info:", info)

# Lab 12: Modules
import random
random.shuffle(sandwich)
print("5. Shuffled Layers:", sandwich)

# Lab 13: Strings
final_touch = "Sprinkle of Salt".upper()
sandwich.append(final_touch)
print("6. String Layer:", final_touch)

# Lab 14: File Handling
with open("recipe.txt", "w") as f:
    f.write("\n".join(str(i) for i in sandwich))
print("7. Recipe saved!")

# Lab 15: Exception Handling
try:
    print(f"8. Final Bite: {sandwich[100]}")
except IndexError:
    print("8. Exception handled: Too many layers!")

print("\n🥪 Your 8-layer code sandwich is complete!")