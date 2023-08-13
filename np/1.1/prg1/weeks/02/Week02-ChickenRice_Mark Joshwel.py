from math import ceil

SIDE_PRICE = 1.20
price = float(input("Enter the price of chicken rice: "))
sides = int(input("Enter the number of side-dishes: "))
total = ceil(10.8 * (price + (SIDE_PRICE * sides))) / 10
print(f"Total cost of the purchase is ${total:.2f}")
