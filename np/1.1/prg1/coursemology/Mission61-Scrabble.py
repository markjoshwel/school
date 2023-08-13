def factorial(number_of_letters):
    result = 1
    i = 0

    while i < number_of_letters:
        print(result, number_of_letters)
        result *= number_of_letters - i
        i += 1

    return result


# number_of_letters = int(input("Enter number of letters you have in your hands: "))
# result = factorial(number_of_letters)
# print(f"Possible n-letter word combinations: {result}")
