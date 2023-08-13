def check_validity(months_left, months_to_entry):
    if (months_left - months_to_entry) <= 6:
        print("Valid passport.")
        return True

    else:
        print("You neeed tor renew your passport.")
        return False


# months_left = int(input("Enter number of months before passport expiry : "))
# months_to_entry = int(input("Enter number of months before passport expiry : "))
# validity = check_validity(months_left, months_to_entry)
# print(validity)
