# ToDoList
#   Mark Joshwel, SXXXXXXXX
# =========================
# prints first three lines of todolist.txt

with open("todolist.txt") as tfd:
    print(tfd.readline(), tfd.readline(), tfd.readline(), end="")
