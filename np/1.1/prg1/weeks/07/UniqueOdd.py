# UniqueOdd: Mark Joshwel (SXXXXXXXX)
numbers = [2, 7, 11, 6, 7, 3, 17, 7, 12, 41, 8, 11, 13, 10, 15]
everseen, uniqueodd5 = [], []

for n in numbers:
    if len(uniqueodd5) >= 5:
        break
    if n in everseen:
        continue
    everseen.append(n)
    if n % 2 != 0:
        uniqueodd5.append(n)

print(uniqueodd5)
