# Count Letters: CountLetters.py
# Mark Joshwel - SXXXXXXXX (IM02/P12)

chars = {}
sentence = input("Enter a sentence: ")
for char in sentence:
    if not char.isalpha():
        continue

    if char.lower() not in chars:
        chars[char.lower()] = 0

    chars[char.lower()] += 1

for char, times in chars.items():
    print(f"{char} : {times}")
