# OddEveen: Mark Joshwel (SXXXXXXXX)
nums = []

while True:
    num = int(input("Please enter a number (0 to end): "))
    if num == 0:
        break
    nums.append(num)

print(
    f"Odd numbers: {sorted([n for n in nums if (n % 2 != 0)])}\n"
    f"Even numbers: {sorted([n for n in nums if (n % 2 == 0)])}\n"
    f"Average = {sum(nums) / len(nums):.2f}"
)
