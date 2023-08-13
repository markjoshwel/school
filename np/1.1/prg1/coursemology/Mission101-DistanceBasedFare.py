from csv import reader


def calculate_fare(board, alight):
    fares = []

    with open("distance-based-fare.csv") as farefd:
        fares = reader(farefd)
        next(fares)  # skip column headers

        for up_to, cents in fares:
            if header:
                header = False
                continue

            fares.append((float(up_to), int(cents)))

    distance = 0
    fare = 0

    with open("bus_174.csv") as busfd:
        stops = reader(busfd)
        next(stops)

        for trip_distance, bus_stop, road, description in stops:
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
