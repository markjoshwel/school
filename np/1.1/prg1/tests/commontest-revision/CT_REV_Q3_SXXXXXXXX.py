# Mark Joshwel (SXXXXXXXX) - IM02

# assign variables
details_list = [
    ["Sharon", "F", 33],
    ["Mic", "M", 23],
    ["Josh", "M", 25],
    ["Hannah", "F", 30],
    ["Hanzel", "M", 26],
]
weight_list = [59.50, 65.50, 49.80, 64.20, 47.50]
height_list = [172, 166, 187, 200, 166]
size_list = [c for c in "MLSMS"]
bmi_list, bmr_list, predicted_list = [], [], []

# process everything
for idx in range(len(details_list)):
    _, gender, age = details_list[idx]
    height, weight = height_list[idx], weight_list[idx]

    bmi = weight / ((height / 100) ** 2)
    bmi_list.append(bmi)

    bmr = 0
    if gender == "F":
        bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    else:
        bmr = 66.47 + (13.7 * weight) + (5 * height) - (6.8 * age)
    bmr_list.append(bmr)

    psize = "-"
    if bmi <= 18:
        psize = "S"
    elif bmi <= 21:
        psize = "M"
    else:
        # > 21
        psize = "L"

    predicted_list.append(psize)

accuracy = 100 * (
    len([p for s, p in zip(size_list, predicted_list) if s == p]) / len(predicted_list)
)


# print everything
print("Name     ", "Weight   ", "Height   ", "BMI      ", "Size     ")
for idx in range(len(details_list)):
    name, weight, height, bmi, size = (
        details_list[idx][0],
        weight_list[idx],
        height_list[idx],
        bmi_list[idx],
        size_list[idx],
    )
    print(f"{name:<9} {weight:<9} {height:<9} {bmi:<9.2f} {size:<9}")

print("\nName     ", "BMI      ", "Size     ", "Predicted")
for idx in range(len(details_list)):
    name, bmi, size, psize = (
        details_list[idx][0],
        bmi_list[idx],
        size_list[idx],
        predicted_list[idx],
    )
    print(f"{name:<9} {bmi:<9.2f} {size:<9} {psize:<8}")
print(f"Accuracy rate is {accuracy:.2f}")

print(
    "\nName     ",
    "Weight   ",
    "Height   ",
    "BMI      ",
    "Gender   ",
    "Age      ",
    "BMR",
)
for idx in range(len(details_list)):
    name, gender, age = details_list[idx]
    weight, height, bmi, bmr = (
        weight_list[idx],
        height_list[idx],
        bmi_list[idx],
        bmr_list[idx],
    )

    print(
        f"{name:<9} {weight:<9} {height:<9} {bmi:<9.2f} {gender:<9} {age:<9} {bmr:.2f}"
    )
