# Lab Exercise 10: Frequency Counter using Dictionaries
sentence = input("Enter a sentence: ")
# convert to lowercase, remove punctuation and split into words
cleaned = ""
for ch in sentence.lower():
    if ch.isalnum() or ch == " ":
        cleaned += ch

words = cleaned.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\n--- WORD FREQUENCY ---")
for word, count in frequency.items():
    print(word, ":", count)

if frequency:
    most_common = max(frequency, key=frequency.get)
    print("\nMost frequent word:", most_common, "(" + str(frequency[most_common]) + " times)")
