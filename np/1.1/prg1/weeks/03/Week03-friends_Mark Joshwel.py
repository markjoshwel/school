friends = ["Izzat", "Bryan", "Dalton", "Ethan", "Isaac"]  # type: list[str]
friends.append(input("What is the name of your new friend? "))
print(f"My friends are: {friends}")
to_be_friendzoned = input("Who do you want to friendzone? ")
to_be_friendzoned_idx = friends.index(to_be_friendzoned)
print(
    f"{to_be_friendzoned} was in position {to_be_friendzoned_idx}. They will be friendzoned."
)
friends.pop(to_be_friendzoned_idx)
print(f"My eligible friends are now: {friends}")
