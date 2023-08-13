# Printer Charges
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def calculate_charge(npages: int) -> float:
    total = 0.0
    for page in range(1, npages + 1):
        if page <= 100:
            total += 0.03
        elif page <= 300:
            total += 0.02
        else:
            total += 0.01
    return total


def calculate_gst(excl_price: float) -> float:
    return excl_price * 0.07


print("Pages      Charge($)      Include gst($)")
for pages in range(0, 501, 50):
    charge = calculate_charge(pages)
    total = charge + calculate_gst(charge)
    print(f"{pages:<5}      {charge:>9.2f}      {total:>14.2f}")
