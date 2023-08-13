# WordCount: Mark Joshwel (SXXXXXXXX)

words = []

i = 0
while i < 5:
    response = input("Enter word (x to exit): ")

    if response == "x":
        break

    if response in words:
        print(f"{response} has already been entered.")
    else:
        words.append(response)
        i += 1

print(f"The words are {words}")
print(f"The number of letters in these words is {sum([len(w) for w in words])}")
