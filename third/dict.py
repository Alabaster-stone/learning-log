
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Draco", "house":"Slytherin", "patronus":None},
]

#遍历列表中的每一个字典，student是字典
for student in students:
    print(student["name"], student["house"], sep=",")



students2 = {"Hermione": "Gryffindor",
             "Harry" : "Gryffindor",
             "Ron" : "Gryffindor"
             }
#遍历字典中的每一个键，student是键
for student in students2:
    print(student, students2[student], sep=",")
print(students2)