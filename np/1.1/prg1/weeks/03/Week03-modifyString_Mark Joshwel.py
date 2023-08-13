original_string = input("Enter original string: ")
target_substring = input("Substring to delete: ")
print(f"The modified string is: {original_string.replace(target_substring, '', 1)}")
