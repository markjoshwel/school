SingaporeWest = [
    "Western Water Catchment",
    "Pioneer",
    "Jurong West",
    "Lim Chu Kang",
    "Tuas",
    "Choa Chu Kang",
    "Bukit Batok",
    "Western Islands Planning Area",
    "Tengah",
    "Jurong East",
    "Clementi",
    "Bukit Panjang",
    "Boon Lay",
]

SingaporeEast = [
    "Changi Bay",
    "Katong",
    "Lorong Halus",
    "Simei",
    "Bedok Reservoir",
    "Tanah Merah",
    "East Coast",
    "Pasir Ris",
    "Marine Parade",
    "Chai Chee",
    "Bedok",
    "Changi Village",
    "Kembangan",
    "Loyang",
    "Tampines",
    "Ubi",
    "Siglap",
    "Elias",
    "Joo Chiat",
    "Kaki Bukit",
    "Changi East",
    "Changi",
]


def Sort(strings, flag=False):
    sstrs = sorted(strings)
    return sstrs if not flag else sstrs[::-1]


print("Singapore - West (Ascending)")
for town in Sort(SingaporeWest, False):
    print(town)

print("\nSingapore - East (Ascending)")
for town in Sort(SingaporeEast, True):
    print(town)
