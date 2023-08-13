from math import sqrt, pi


def calculate_circle(a: float, b: float) -> float:
    c = sqrt((a**2) + (b**2))
    r = c / 2
    return pi * (r**2)


a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))
area = calculate_circle(a=a, b=b)

print(f"The area of the circle is {area}")
