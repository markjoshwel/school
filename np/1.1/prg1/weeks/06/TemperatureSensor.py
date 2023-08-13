# TemperatureSensor: Mark Joshwel (SXXXXXXXX)

MAX_TEMP = 29

reads_n, reads_ttl = 0, 0

print("The temperatures are")
with open("temperature.txt", "r") as tfd:
    for reads_n, _temp in enumerate(tfd.read().split(","), start=1):
        temp = float(_temp.strip())
        reads_ttl += temp
        print(f"  {temp} ** higher than 29!!!" if temp > MAX_TEMP else f"  {temp}")

print(
    f"\nNumber of readings: {reads_n}"
    f"\nAverage temperature: {reads_ttl / reads_n:.2f}"
)
