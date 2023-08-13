# Temperature Conversion
# Mark Joshwel (SXXXXXXXXB - IM02/P12)


def convert_temperature(temp: float) -> float:
    return (temp * 9 / 5) + 32


temp_c = float(input("Enter the temperature in degree celsius: "))
temp_f = convert_temperature(temp_c)
print(f"The temperature is equivalent to {temp_f} fahrenheit.")
