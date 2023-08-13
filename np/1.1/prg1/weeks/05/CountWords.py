# CountWords
#   Mark Joshwel, SXXXXXXXX
# =========================
# counts words in data.txt and outputs it to stdout and to output.txt
# using loose definition of space seperation to define a word
# (i mean that was valid for the baby shark example)

with open("data.txt", "r") as dfd:
    nwords = len(dfd.read().split())
    print(f"Number of words in data.txt: {nwords}")

    with open("output.txt", "w") as ofd:
        ofd.write(f"There are {nwords} words in the document.\n")
        print("Number of words successfully written to outut.txt")
