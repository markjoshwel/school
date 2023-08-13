# Extreme Values
# Mark Joshwel (SXXXXXXXX - IM02/P12)


from math import inf


def get_extremes(nums: list[int]):
    smallest = inf
    biggest = -inf

    for num in nums:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num

    return smallest, biggest


nums = [int(n) for n in input("Enter comma-seperated integers: ").split(",")]
smallest, largest = get_extremes(nums)
print(f"Smallest is {smallest}\nLargest is {largest}")
