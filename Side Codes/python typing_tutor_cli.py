# import time
# import random

# try:
#     with open("sentences.txt", "r") as file:
#         lines = file.readlines()
#     sentences = [line.strip() for line in lines if line.strip()]
# except FileNotFoundError:
#     print("⚠️ File 'sentences.txt' not found. Please create it with some sentences.")
#     exit()

# sentence = random.choice(sentences)
# print("\nWelcome to the CLI Typing Tutor")
# print("Type the following sentence as fast and accurately as you can:\n")

# print(f"📜 Sentence: {sentence}\n")

# input("Press Enter to start typing...")
# start_time = time.time()

# typed = input("\n📝 Your typing: ")

# end_time = time.time()
# total_time = round(end_time - start_time, 2)

# original_words = sentence.split()
# typed_words = typed.split()
# correct_count = sum(1 for o, t in zip(original_words, typed_words) if o == t)
# accuracy = round((correct_count / len(original_words)) * 100, 2)

# result = {
#     "sentence": sentence,
#     "typed": typed,
#     "time": total_time,
#     "accuracy": accuracy
# }

# with open("results.txt", "a") as f:
#     f.write(f"Sentence: {result['sentence']}\n")
#     f.write(f"Typed: {result['typed']}\n")
#     f.write(f"Time: {result['time']} sec | Accuracy: {result['accuracy']}%\n\n")

# try:
#     print("\n✅ Test complete!")
#     print(f"⏱️ Time taken: {result['time']} seconds")
#     print(f"🎯 Accuracy: {result['accuracy']}%")
# except KeyError as e:
#     print(f"❌ Missing key in result dictionary: {e}")


import time
import random

try:
    with open("sentences.txt", "r") as file:
        lines = file.readlines()
    sentences = [line.strip() for line in lines if line.strip()]
except FileNotFoundError:
    print("Error: sentences.txt file not found.")
    exit()

sentence = random.choice(sentences)

print("Welcome to Typing Tutor")
print("Type the sentence below as fast and accurately as possible:")
print()
print(sentence)
print()

input("Press Enter to start...")
start_time = time.time()

typed = input("Start typing:\n")

end_time = time.time()
total_time = round(end_time - start_time, 2)

original_words = sentence.split()
typed_words = typed.split()

correct = 0
for i in range(len(original_words)):
    if i < len(typed_words) and original_words[i] == typed_words[i]:
        correct += 1

accuracy = round((correct / len(original_words)) * 100, 2)

result = {
    "sentence": sentence,
    "typed": typed,
    "time": total_time,
    "accuracy": accuracy
}

with open("results.txt", "a") as file:
    file.write("Sentence: " + result["sentence"] + "\n")
    file.write("Typed: " + result["typed"] + "\n")
    file.write("Time: " + str(result["time"]) + " sec\n")
    file.write("Accuracy: " + str(result["accuracy"]) + "%\n\n")

try:
    print()
    print("Results saved!")
    print("Time taken:", result["time"], "seconds")
    print("Accuracy:", result["accuracy"], "%")
except KeyError:
    print("There was an error saving your results.")