import time
import random

# === LAB 14: FILE HANDLING - Read sentences ===
try:
    with open("sentences.txt", "r") as file:
        lines = file.readlines()
    sentences = [line.strip() for line in lines if line.strip()]
except FileNotFoundError:
    print("⚠️ File 'sentences.txt' not found. Please create it with some sentences.")
    exit()

# === LAB 08: LIST - Pick one sentence randomly ===
sentence = random.choice(sentences)
print("\n🌟 Welcome to the CLI Typing Tutor 🌟")
print("Type the following sentence as fast and accurately as you can:\n")

# === LAB 13: STRING - Display sentence ===
print(f"📜 Sentence: {sentence}\n")

# === LAB 12: MODULES - Start timer ===
input("Press Enter to start typing...")
start_time = time.time()

# === LAB 09: OPEN-ENDED - Get user input ===
typed = input("\n📝 Your typing: ")

end_time = time.time()
total_time = round(end_time - start_time, 2)

# === LAB 10: SEARCHING & SORTING - Accuracy check ===
original_words = sentence.split()
typed_words = typed.split()
correct_count = sum(1 for o, t in zip(original_words, typed_words) if o == t)
accuracy = round((correct_count / len(original_words)) * 100, 2)

# === LAB 11: TUPLE & DICTIONARY - Result data structure ===
result = {
    "sentence": sentence,
    "typed": typed,
    "time": total_time,
    "accuracy": accuracy
}

# === LAB 14: FILE HANDLING - Log result ===
with open("results.txt", "a") as f:
    f.write(f"Sentence: {result['sentence']}\n")
    f.write(f"Typed: {result['typed']}\n")
    f.write(f"Time: {result['time']} sec | Accuracy: {result['accuracy']}%\n\n")

# === LAB 15: EXCEPTION HANDLING - Optional extra safety ===
try:
    print("\n✅ Test complete!")
    print(f"⏱️ Time taken: {result['time']} seconds")
    print(f"🎯 Accuracy: {result['accuracy']}%")
except KeyError as e:
    print(f"❌ Missing key in result dictionary: {e}")