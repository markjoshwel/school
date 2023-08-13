def process_file(path):
    with open(path, "r", encoding="utf-8") as dfd:
        data = dfd.read()

    nlines = len(data.splitlines())
    nwords = len(data.split())
    nchar = len(data)

    return [nlines, nwords, nchar]


# path = input("Enter filename : ")
# result = process_file(path)
# print()
# print("------------------------------------------------------------------------------------")
# print("Total number of lines      :", result[0])
# print("Total number of words      :", result[1])
# print("Total number of characters :", result[2])
