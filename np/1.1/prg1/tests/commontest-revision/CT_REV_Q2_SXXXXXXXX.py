# Mark Joshwel (SXXXXXXXX) - IM02

total = 0
aces = 0

card1 = int(input(f"Enter card 1: "))
aces += 1 if (card1 == 1) else 0
total += card1 if (card1 <= 10) else 10

card2 = int(input(f"Enter card 2: "))
aces += 1 if (card2 == 1) else 0
total += card2 if (card2 <= 10) else 10

card3 = int(input(f"Enter card 3: "))
aces += 1 if (card3 == 1) else 0
total += card3 if (card3 <= 10) else 10

if (total - (aces * 1) + (aces * 11)) <= 21:
    total = total - (aces * 1) + (aces * 11)

print(f"Total card value is {total}")
