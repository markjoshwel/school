# Grades
#   Mark Joshwel, SXXXXXXXX
# ========================
# Displays corresponding alphabetical grade and comment based on
# entered marks


mark = float(input("Enter your marks: "))
grade, comment = "", ""


if mark >= 85:
    grade, comment = "A+", "Excellent!"

elif mark >= 80:
    grade, comment = "A", "Well done."

elif mark >= 75:
    grade = "B+"

elif mark >= 65:
    grade = "C+"

elif mark >= 60:
    grade = "C"

elif mark >= 55:
    grade = "D+"

elif mark >= 50:
    grade = "D"

else:
    grade, comment = "F", "See me."

print(f"Grade: {grade}", (f"\n{comment}" if (comment != "") else ""))
