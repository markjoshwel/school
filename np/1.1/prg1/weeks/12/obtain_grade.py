# Obtain Grade
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def obtain_grade(grade: float) -> str:
    if grade < 49.5:
        return "F"
    elif grade < 54.5:
        return "D"
    elif grade < 59.5:
        return "D+"
    elif grade < 64.5:
        return "C"
    elif grade < 69.5:
        return "C+"
    elif grade < 74.5:
        return "B"
    elif grade < 79.5:
        return "B+"
    elif grade < 84.5:
        return "A"
    else:
        return "A+"


mark_list = [
    ["Mary", 90.5],
    ["Charles", 60.4],
    ["John", 70.5],
    ["Javier", 32.0],
    ["Luke", 46.7],
]
#      123456789012-_-1234-_-_-12345
print("Student Name   mark     Grade")
for name, grade in mark_list:
    print(f"{name:<12}   {grade:<5.1f}     {obtain_grade(grade)}")  # type: ignore
