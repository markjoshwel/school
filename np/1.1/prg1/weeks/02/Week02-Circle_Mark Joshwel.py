from math import sqrt, pi

a = float(input("Enter the length of a: "))
b = float(input("Enter the length of b: "))
c = sqrt((a**2) + (b**2))
r = c / 2
area = pi * (r**2)

print(f"The length of c is {c}\nThe area of the circle is {area}")
