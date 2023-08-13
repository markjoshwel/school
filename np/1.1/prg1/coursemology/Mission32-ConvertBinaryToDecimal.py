def binaryToDecimal(binary_value):
    decimal_value = 0

    for idx, bch in enumerate(binary_value[::-1]):
        if bch == "1":
            decimal_value += 2**idx

    return decimal_value


# input
# binary_value = input("Enter a 4-figit binary value: ")

# process
# decimal_value = binaryToDecimal(binary_value)

# output
# print(f"Decimal value: {decimal_value}")
