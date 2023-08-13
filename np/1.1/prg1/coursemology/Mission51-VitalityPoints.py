def check_gift(distance):
    gift = 0

    if distance < 25:
        gift = 0
    elif distance < 50:
        gift = 5
    elif distance < 75:
        gift = 10
    else:
        gift = 20

    return gift


distance = float(input("Enter number of distance traveled in kilometer: "))
gift = check_gift(distance)

if gift == 0:
    print("You get an eSticker")
elif gift == 5:
    print("You get a $5 Cold Storage eVoucher")
elif gift == 10:
    print("You get a $10 Starbucks eVoucher")
else:
    print("You get a $20 Subway eVoucher")
