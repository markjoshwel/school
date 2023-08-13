# Even Integers
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def is_even(num: int) -> bool:
    return True if (num % 2 == 0) else False


num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
print("Even numbers in the list:", ", ".join([str(n) for n in num_list if is_even(n)]))
