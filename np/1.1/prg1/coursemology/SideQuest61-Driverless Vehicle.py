def closest_object(roundTrips):
    objects, strips = [], roundTrips.split(",")
    while len(objects) < len(strips):
        objects.append(float(strips[len(objects)].strip()))

    if len(objects) < 5:
        print("Error: number of round trips entered is lesser than 5")
        return [-1, -1]

    closestObject = [objects.index(min(objects)), min(objects) * (344 / 2)]
    return closestObject


# roundTrips = input("Enter minimum 5 round trip times, each value separated by comma: ")
# result = closest_object(roundTrips)
# print(f"The closest object is object {result[0]} which is {result[1]}m away")
