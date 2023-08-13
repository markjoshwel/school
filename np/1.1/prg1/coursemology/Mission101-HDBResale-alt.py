filename = "HDB-Resale-Price.csv"


def ReadCSV(filename):
    data = {}

    with open(filename) as cfd:
        next(cfd)

        for price in cfd:
            quarter, town, flat_type, price = price.strip().split(",")

            if quarter not in data:
                data[quarter] = {}

            if town not in data[quarter]:
                data[quarter][town] = {}

            if price.isdigit():
                data[quarter][town][flat_type] = int(price)

    y2022_4_room = []
    highest_resale_town = ""
    highest_resale_price = 0

    for quarter in data:
        # print(quarter, data[quarter])

        if quarter.startswith("2022"):
            for town in data[quarter]:
                # print(quarter, town, data[quarter][town], "")

                if data[quarter][town].get("4-room") is None:
                    continue

                y2022_4_room.append(data[quarter][town]["4-room"])

                if data[quarter][town].get("5-room", 0) > highest_resale_price:
                    highest_resale_price = data[quarter][town]["5-room"]

                    highest_resale_town = town

    y2022_average = sum(y2022_4_room) / len(y2022_4_room)
    y2022_above_average = len([n for n in y2022_4_room if n > y2022_average])

    return [round(y2022_average, 2), y2022_above_average, highest_resale_town]


print(ReadCSV("HDB-Resale-Price.csv"))
