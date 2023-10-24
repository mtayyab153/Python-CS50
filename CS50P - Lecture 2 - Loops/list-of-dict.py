students = [
    {"name": "joe", "age": 23, "gender": "male"},
    {"name": "riya", "age": 33, "gender": "female"},
    {"name": "jacks", "age": 13, "gender": "male"},
    {"name": "nun", "age": 14, "gender": "female"},
]

for student in students:
    print(student["name"], student["age"], student["gender"], sep=", ")