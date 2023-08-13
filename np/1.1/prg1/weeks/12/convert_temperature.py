# Temperature Conversion (Activity 13)
# Mark Joshwel (SXXXXXXXXB - IM02/P12)


def fahr_to_cel(tempf: float) -> float:
    return 5 / 9 * (tempf - 32)


def cel_to_fahr(tempc: float) -> float:
    return (tempc * 9 / 5) + 32


option: int = 0
while option != 3:
    print(
        """Temperature Conversion
[1]Fahrenheit to Celsius
[2]Celsius to Fahrenheit
[3]Exit"""
    )

    option = int(input("Please enter your option : "))
    if option == 1:  # f-c
        tempf = float(input("Please enter the temperature in Fahrenheit : "))
        print(f"The temperature in celsius is {fahr_to_cel(tempf):.1f} degrees")

    elif option == 2:  # c-f
        tempf = float(input("Please enter the temperature in Celsius : "))
        print(f"The temperature in fahrenheit is {cel_to_fahr(tempf):.1f} degrees")

    elif option != 3:
        print("Invalid option.")

    print()
