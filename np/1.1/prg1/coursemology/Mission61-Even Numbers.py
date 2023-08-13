def total_num(start, end):
    total = 0

    i = start
    while i <= end:
        if i % 2 == 0:
            total += i
        i += 1
    return total


# start = int(input("Enter start of range: "))
# start = int(input("Enter end of range: "))
# total = total_num(start, end)
# print(total)
