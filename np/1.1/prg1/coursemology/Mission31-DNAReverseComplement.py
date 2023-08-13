base = "ACGT"
complement = "TGCA"


def calculate_DNAReverseComplement(dna1: str) -> str:
    dna2 = "".join([complement[base.find(c)] for c in dna1])[::-1]
    return dna2


# input
# dna1 = input("Enter a 7-base long DNA sequence: ").upper()

# process
# dna2 = calculate_DNAReverseComplement(dna1)

# output
# print(dna2)
