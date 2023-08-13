def calculate_average(student_list, mark_list):
    marks = []

    # "i must do a while loop"
    i = 0
    while i < len(mark_list):
        print(f"{i+1}) {student_list[i]} - {mark_list[i]}")
        marks.append(mark_list[i])
        i += 1

    average = sum(marks) / len(marks)  # ok lol

    return average


student_list = ["John", "Tom", "Jane", "Jim", "Mary", "Steve", "Anne"]
mark_list = [100, 75, 80, 20, 50, 70, 95]
average = calculate_average(student_list, mark_list)
print(f"Average mark is {average}.")
