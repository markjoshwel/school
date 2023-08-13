def calculate_sales(filename):
    results = []

    with open(filename, "r") as file:
        for line in file.readlines():
            data = line.split(",")

            month = data[0]
            sales = 0

            for sale in data[1:]:
                sales += int(sale)

            results.append([month, sales])

    return results


# filename = input("Please enter the name of the data file: ")
# results = calculate_sales(filename)
# print("Month          Sales")
# #      123456789    1234567
# for result in results:
#     print(f"{result[0]:<9}    {result[1]:>7}")
