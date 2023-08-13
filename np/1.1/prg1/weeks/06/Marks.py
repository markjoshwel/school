# Marks: Mark Joshwel (SXXXXXXXX)

with open("marks.txt", "r") as mfd:
    data = [l.split(";") for l in mfd.read().splitlines()]

print(
    """Name        Mark
----        ----"""
)
n = 0
marks = 0
for n, entry in enumerate(data, start=1):
    mark = float(entry[1])
    marks += mark
    print(f"{entry[0]:<11} {mark:.1f}")

print(f"\nAverage Mark: {marks / n:.2f}")
