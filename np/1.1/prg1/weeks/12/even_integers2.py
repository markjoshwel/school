# Even Integers 2
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def is_even(num: int) -> bool:
    return True if (num % 2 == 0) else False


def find_even(nums: list[int]) -> None:
    print("Even numbers in the list:", ", ".join([str(n) for n in nums if is_even(n)]))


num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
find_even(num_list)
