with open("Week02-StudentData_Mark Joshwel.txt", "r", encoding="utf-8") as data_fd:
    data = data_fd.read()
    entries = data.splitlines()
    print(entries[0], entries[2], entries[4], sep="\n")
