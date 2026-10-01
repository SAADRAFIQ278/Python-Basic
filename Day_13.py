# import json
# student = {
#     "name": "Saad",
#     "age": 19,
#     "course": "Python"
# }
# data = json.dumps(student)
# print(data)

# new_student = json.loads(data)
# print(new_student)

# import json

# student = {
#     "name": "Saad",
#     "age": 19,
#     "course": "Python",
#     "semester": "3rd"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)


# import json
# with open ("student.json","r") as file:
#     student = json.load(file)
#     print(student)

#     print(student["name"])
#     print(student["age"])
#     print(student["course"])
#     print(student["semester"])

import json
with open ("student.json","r") as file:
    student = json.load(file)
    student["age"] = 20
with open ("student.json","w") as file:
    json.dump(student,file,indent = 4)