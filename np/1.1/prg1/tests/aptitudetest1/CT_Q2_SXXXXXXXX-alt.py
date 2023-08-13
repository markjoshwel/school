"""
alternate file with a much saner merge method
"""

# Mark Joshwel (SXXXXXXXX) - IM02

word = input("Enter your word: ").lower()
print(f"Your input has {len(word)} characters")
scramble_pos = [
    int(idx) - 1
    for idx in input(
        "Input the positions of the characters to select, separated by ',': "
    ).split(",")
]
print(
    f"Swapping the characters '{word[scramble_pos[0]]}' and '{word[scramble_pos[1]]}'"
)

scrambled_word = ""
for c in word:
    if c == word[scramble_pos[0]]:
        scrambled_word += word[scramble_pos[1]]
    elif c == word[scramble_pos[1]]:
        scrambled_word += word[scramble_pos[0]]
    else:
        scrambled_word += c

print(f"Scrambled word: {scrambled_word}")
