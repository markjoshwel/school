# Christmas Tree
# Mark Joshwel - SXXXXXXXX

chr = input("Enter a character: ")
num = int(input("Enter a number: "))

for nchar in range(1, num + 1):
    nspace = num - nchar
    # print(nspace, nchar)
    print(" " * nspace, f"{chr} " * nchar, sep="")
