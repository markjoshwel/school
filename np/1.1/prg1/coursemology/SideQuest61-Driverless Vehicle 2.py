def fail_safety_distance(roundTrips):
    objects, strips = [], roundTrips.split(",")
    while len(objects) < len(strips):
        objects.append(float(strips[len(objects)].strip()))

    if len(objects) < 5:
        print("Error: number of round trips entered is lesser than 5")
        return [-1, -1]

    tooNear = False

    if (min(objects) * (344 / 2)) < 50:
        tooNear = True

    return tooNear


# roundTrips = input("Enter minimum 5 round trip times, each value separated by comma: ")
# result = fail_safety_distance(roundTrips)
# print("Vehicle is too near an object" if result else "Vehicle is at a safe distance")
