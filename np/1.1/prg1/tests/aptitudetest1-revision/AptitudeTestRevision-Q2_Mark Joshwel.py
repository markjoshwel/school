abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ref = "AZYXUTSRPMLKJHGEDCB"

plate = input("Enter the vehicle number to be validated: ")

valid = False
plate_c1 = abc.index(plate[1]) + 1
plate_c2 = abc.index(plate[2]) + 1
plate_n1 = int(plate[3])
plate_n2 = int(plate[4])
plate_n3 = int(plate[5])
plate_n4 = int(plate[6])

remainder = (
    sum(
        [
            plate_c1 * 9,
            plate_c2 * 4,
            plate_n1 * 5,
            plate_n2 * 4,
            plate_n3 * 3,
            plate_n4 * 2,
        ]
    )
    % 19
)
if ref[remainder] == plate[-1]:
    valid = True

print("Validity of the vechicle number:", ("Valid" if valid else "Invalid"))
