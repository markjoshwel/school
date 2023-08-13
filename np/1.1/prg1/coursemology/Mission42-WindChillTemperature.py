from math import pow


def wind_chill(ta: float, v: float):
    if (-58 <= ta <= 41) and (v > 2):
        twc = (
            35.74
            + (0.6215 * ta)
            - (35.75 * pow(v, 0.16))
            + (0.4275 * ta * pow(v, 0.16))
        )
        print(f"The wind-chill index is {twc:.2f}")

    else:
        print("Incorrect input")


ta = float(input("Please enter the outside temperature in Fahrenheit: "))
v = float(input("Please enter the wind speed in miles per hour: "))
wind_chill(ta, v)
