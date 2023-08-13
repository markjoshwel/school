def find_favourite_numbers(start_range, end_range):
    fav_numbers = []

    for num in range(start_range, end_range + 1):
        if (num % 5 == 0) and (num % 7 == 0):
            fav_numbers.append(num)

    return fav_numbers


# start_range = int(input("Enter the starting number:"))
# end_range = int(input("Enter the ending number:"))
# fav_numbers = find_favourite_numbers(start_range, end_range)
# print(f"Suspect's numbers are: {fav_numbers}")
