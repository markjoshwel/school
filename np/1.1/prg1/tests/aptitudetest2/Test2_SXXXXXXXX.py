# Mark Joshwel SXXXXXXXX - IM02

from math import ceil

header = []  # type: list[str]
data = []  # type: list[list[str]]

# 1a

with open("trip_prices.txt") as tfd:
    header = next(tfd).strip().split(",")  # skip header

    for line in tfd:
        data.append(line.strip().split(","))

print(f"Trip prices:\n{data}")

# 1b

n_adult = 5
n_child = 2
n_extns = 3

n_adult_twin = 5 // 2
n_adult_sngl = n_adult - (n_adult_twin * 2)
n_rooms = ceil((n_adult + n_child) / 2)

print(
    f"""
Number of adults: {n_adult}
Number of children: {n_child}
Number of extension: {n_extns}
Number of adult-twin for the tour package / land tour: {n_adult_twin}
Number of adult-single for the tour package / land tour: {n_adult_sngl}
Number of children for the tour package / land tour: {n_child}
Number of rooms for extension per night: {n_rooms}
"""
)


# 1c

total_amt_list = []  # type: list[list[int]]
header.extend(["Total Amount", "Amount w Land Tour"])

#       0     1      2      3      4     5           6           7         8             9
#       01234 012345 012345 012345 01234 0123456789A 0123456789A 012345678 0123456789ABC -
print(
    f"{header[0]:<5} {header[1]:<6} {header[2]:<6} {header[3]:<6} {header[4]:<5} {header[5]:<11} {header[6]:<11} {header[7]:<9} {header[8]:<13} {header[9]}"
)
for entry in data:
    price_hotel = price_land_tour = (
        (int(entry[1]) * n_adult_twin)
        + (int(entry[2]) * n_adult_sngl)
        + (int(entry[3]) * n_child)
        + (int(entry[4]) * n_rooms * n_extns)  # extensions
    )

    price_land_tour = (
        (int(entry[5]) * n_adult_twin)
        + (int(entry[6]) * n_adult_sngl)
        + (int(entry[7]) * n_child)
    )

    total_amt_list.append([price_hotel, price_hotel + price_land_tour])

    print(
        f"{entry[0]:<5} {entry[1]:<6} {entry[2]:<6} {entry[3]:<6} {entry[4]:<5} {entry[5]:<11} {entry[6]:<11} {entry[7]:<9} {price_hotel:<13} {price_hotel + price_land_tour}"
    )


# 1d

budget = 25000

#         12345678
print(f"\nOptions Available for SGD${budget} budget:")

for data_index, entry in enumerate(data):
    hotel = entry[0]

    for tal_index, amt_entry in enumerate(total_amt_list):
        if data_index != tal_index:
            # skip if the indexes dont match
            continue

        total_amt, total_amt_w_land_tour = amt_entry

        if total_amt <= budget:
            print(f"        Hotel {hotel} w/o land tour")

        if total_amt_w_land_tour <= budget:
            print(f"        Hotel {hotel} w land tour")


# # alternative answer (no nested loop)
# # i would suggest this as the actual solution but apparently we need a nested loop :/
#
# for hotel, amt_entry in zip([d[0] for d in data], total_amt_list):
#     # [total amt, amt w land tour]
#     total_amt, total_amt_w_land_tour = amt_entry
#
#     if total_amt <= budget:
#         print(f"        Hotel {hotel} w/o land tour")
#
#     if total_amt_w_land_tour <= budget:
#         print(f"        Hotel {hotel} w land tour")
