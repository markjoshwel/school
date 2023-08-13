# Cars
#   Mark Joshwel, SXXXXXXXX
# =========================
# display car prices from cars.txt, prompt for order, output order to file

with open("cars.txt") as cfd:
    # 'throw away' first two lines
    _ = cfd.readline()
    _ = cfd.readline()

    # car1_name, car1_price = cfd.readline().strip().split(" : ")
    # print("1.", car1_name)

    # car2_name, car2_price = cfd.readline().strip().split(" : ")
    # print("2.", car2_name)

    # car3_name, car3_price = cfd.readline().strip().split(" : ")
    # print("3.", car3_name)

    # car4_name, car4_price = cfd.readline().strip().split(" : ")
    # print("4.", car4_name)

    # cars = [
    #     (car1_name, car1_price),
    #     (car2_name, car2_price),
    #     (car3_name, car3_price),
    #     (car4_name, car4_price),
    # ]  # type: list[tuple[str, str]]

    cars = []  # type: list[tuple[str, str]]
    for idx, line in enumerate(cfd.read().splitlines(), start=1):
        print(f"{idx}. {line}")
        cars.append(line.split(" : "))

    order_no = input("\nEnter the order number: ")
    order_cname = input("Customer Name: ")
    choice = int(input("Enter car choice: ")) - 1  # -1 for 0-indexing

    with open(f"{order_no}.txt", "w") as ofd:
        ofd.write(
            f"Peter tan ordered the {cars[choice][0]} at the price of {cars[choice][1]}\n"
        )

    print("Car has been successfully ordered.")
