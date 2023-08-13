# imports
from math import sqrt, pi

# input
r = float(input("Enter the base circle radius: "))
h = float(input("Enter the base circle height: "))

# process
v = (1 / 3) * pi * (r**2) * h
s = sqrt((r**2) + (h**2))
A = pi * (r**2) + pi * r * s

# output
print(
    f"""For a cone with base circle radius {r} and height {h}:
Slant height is {s:.2f}
Volume is {v:.4f}
Surface area (including base circle) is {A:.4f}"""
)
