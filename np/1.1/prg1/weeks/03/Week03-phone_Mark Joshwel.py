with open("Week03-StudentData_Mark Joshwel.txt", "r", encoding="utf-8") as data_fd:
    print(f"{'Name':<16} {'Mobile Contact':<14}")
    for idx, entry in enumerate(data_fd.read().splitlines()):
        if idx < 2:
            data = entry.split(",")
            print(f"{data[0]:<16} {data[-1]:<14}")
