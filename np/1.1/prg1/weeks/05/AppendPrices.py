# AppendPrices
#   Mark Joshwel, SXXXXXXXX
# =========================
# appends two price entries to prices.txt

with open("prices.txt", "a") as pfd:
    # question didnt say to use a list/use formatting/etc
    pfd.write("teh peng: $1.20\n" "milo peng: $1.40\n")
