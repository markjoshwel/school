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

# i genuinely know no simpler way, this is probably not the simplest way

# create replaces
scramble_a, scramble_b = (
    word.replace(word[scramble_pos[0]], word[scramble_pos[1]]),
    word.replace(word[scramble_pos[1]], word[scramble_pos[0]]),
)

# create delta
scramble_a_delta = [
    (idx, ischr[1])
    for (idx, ischr) in enumerate(zip(word, scramble_a))
    if (ischr[0] != ischr[1])
]
scramble_b_delta = [
    (idx, ischr[1])
    for (idx, ischr) in enumerate(zip(word, scramble_b))
    if (ischr[0] != ischr[1])
]


# merge
scrambled_list = [c for c in word]
for idx, schr in scramble_a_delta + scramble_b_delta:
    scrambled_list[idx] = schr
scrambled_word = "".join(scrambled_list)

print(f"Scrambled word: {scrambled_word}")
