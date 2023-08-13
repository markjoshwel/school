def calculate_fare(board, alight):
    fares = []

    with open("distance-based-fare.csv") as farefd:
        next(farefd)

        for fare in farefd:
            up_to, cents = fare.split(",")
            fares.append((float(up_to), int(cents)))

    distance = 0
    fare = 0

    with open("bus_174.csv") as busfd:
        next(busfd)

        for stop in busfd:
            trip_distance, bus_stop, road, description = stop.strip().split(",")

            if bus_stop == board:
                distance = -float(trip_distance)

            if bus_stop == alight:
                distance += float(trip_distance)

    for fare_data in fares:
        if fare_data[0] >= distance:
            fare = fares[fares.index(fare_data)][1] / 100
            break

    return [distance, fare]


# board = input("Enter boarding busstop: ")
# alight = input("Enter alighting busstop: ")
# print(calculate_fare(board, alight))
