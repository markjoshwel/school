with open("Week04-data_Mark Joshwel.txt", "r", encoding="utf-8") as dfd:
    data = dfd.read().splitlines()[0].split(",")

    weight_kg, height_m, gender, age = (
        float(data[0]),
        float(data[1]),
        data[2],
        int(data[3]),
    )

    bmr = 0
    if gender == "Female":
        bmr = 10 * weight_kg + 6.25 * (height_m * 100) - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * (height_m * 100) - 5 * age - 161

    print(
        f"""Weight: {weight_kg:.1f}kg
Height: {height_m:.1f}m
Age: {age}
Gender: {gender}
BMR: {bmr:.1f} kcal/day"""
    )
