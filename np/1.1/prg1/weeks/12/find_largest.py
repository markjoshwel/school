# Find Largest Value
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def find_larger(n1: int, n2: int) -> int:
    return n1 if n1 > n2 else n2


num1 = int(input("Enter the first integer numbr : "))
num2 = int(input("Enter the second integer numbr: "))
num3 = int(input("Enter the third integer numbr : "))
num4 = int(input("Enter the forth integer numbr : "))

larger_1_2 = find_larger(num1, num2)
larger_3_4 = find_larger(num3, num4)
largest = find_larger(larger_1_2, larger_3_4)
print(f"The largest integer is {largest}")
