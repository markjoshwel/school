from math import pi

# constants
G = 6.6743 * (10**-11)

# inputs
cyl_r = float(input("Enter the radius of the cylinder (in m): "))
cyl_h = float(input("Enter the height of the cylinder (in m): "))
sph_r = float(input("Enter the radius of the sphere (in m): "))
obj1_m = float(input("Enter the mass of object 1 (in kg): "))
obj2_m = float(input("Enter the mass of object 2 (in kg): "))
obj_dist = float(input("Enter the distance between the objects (in m): "))

# calculations
cyl_vol = pi * (cyl_r**2) * cyl_h
sph_sarea = 4 * pi * (sph_r**2)
obj_force = (G * obj1_m * obj2_m) / (obj_dist**2)

# output
print(
    f"""Results:
     Volume of the cylinder: {cyl_vol:.2f} cubic meters
     Surface area of the sphere: {sph_sarea:.2f} square meters
     Force of gravity between the objects: {obj_force} Newtons"""
)
