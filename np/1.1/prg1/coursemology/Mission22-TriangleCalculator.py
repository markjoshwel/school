# imports
from math import sqrt

# inputs
a = float(input("Enter first side of triangle ('a'): "))
b = float(input("Enter first side of triangle ('b'): "))
c = float(input("Enter first side of triangle ('c'): "))

# process
s = (a + b + c) / 2  # semi-perim
A = sqrt(s * (s - a) * (s - b) * (s - c))  # area

# outputs
print(f"For a triangle with sides {a}, {b} and {c}")
print(f"The perimeter is {s * 2:^.2f}")
print(f"The area is {A:.2f}")
