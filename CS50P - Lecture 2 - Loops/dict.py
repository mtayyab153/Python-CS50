students = {
    "joe": "Gryffindor",
    "jacks": "Gryffindor",
    "Ron": "Gryffindor",
    "mat": "Slytherin"
}

# print(students["joe"])
# print(students["jacks"])
# print(students["Ron"])
# print(students["mat"])

for student in students:
    print(student, students[student], sep=", ")