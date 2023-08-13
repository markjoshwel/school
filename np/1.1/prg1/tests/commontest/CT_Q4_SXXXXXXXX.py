# Mark Joshwel (SXXXXXXXX) - IM02

purchases = [
    ["Curry puff", "Apple tart", "Tuna puff", "Egg tart", "Custard tart"],
    [2.40, 2.00, 2.20, 1.80, 1.50],
    [2, 4, 5, 1, 2],
]

tart_total, puff_total = 0.0, 0.0

print(f"{'Item Name':<16} {'Unit Price':>10} {'Quantity':>10} {'Amount':>10}")
for item_name, unit_price, qty in zip(purchases[0], purchases[1], purchases[2]):  # type: ignore
    amount = qty * unit_price

    if "puff" in item_name.lower():
        puff_total += amount
    elif "tart" in item_name.lower():
        tart_total += amount

    print(f"{item_name:<16} {unit_price:>10.2f} {qty:>10} {amount:>10.2f}")

print(
    f"\nTotal cost of tarts: ${tart_total:.2f}\n"
    f"Total cost of puffs: ${puff_total:.2f}"
)
