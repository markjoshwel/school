# Power
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def power(x: int, n: int):
    return x**n


base = int(input("Enter base as a non-zero integer: "))
expn = int(input("Enter exponent as an intege     : "))
print(f"The power of {base}^{expn} is {power(base, expn)}")
