# import json

# data = {
#     "students": [
#         {"name": "Saad", "age": 20},
#         {"name": "Ali", "age": 21},
#         {"name": "Ahmad", "age": 19}
#     ]
# }

# for student in data ["students"]:
#     print(student["name"])
# print(data["students"][0]["name"])
# print(data["students"][2]["age"])


# import json

# data = {
#     "students": [
#         {"name": "Saad" , "age": 20},
#         {"name": "Ali" , "age": 19},
#         {"name": "Ahmad" , "age": 21}

#     ]
# }

# with open ("student.json","w") as file:
#     json.dump(data,file,indent=4)

# with open ("student.json","r") as file:
#     data = json.load(file)

# for student in data ["students"]:
#     print(student["name"],"-",student["age"])


# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# print(response.status_code)

# data = response.json()

# print(data["name"])
# print(data["email"])


# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# print(response.status_code)

# data = response.json()
# print(data["name"])
# print(data["email"])

# import requests

# student = {
#     "name": "Saad",
#     "age": 20,
#     "course": "python",

# }
# response = requests.post(
#     "https://jsonplaceholder.typicode.com/users",
#     json = student
# )
# print(response.status_code)
# print(response.json())


# import requests

# student = {
#     "name": "Saad",
#     "age": 21,
#     "course": "Python",
# }
# response = requests.put(
#     "https://jsonplaceholder.typicode.com/users/1",
#     json = student
# )
# print(response.status_code)
# print(response.json())

# import requests

# student = {
#     "name": "Saad",
#     "age": 21,
#     "course": "python"
# }
# response = requests.delete(
#     "https://jsonplaceholder.typicode.com/users/1",
  
# )
# print(response.status_code)

# import requests

# student = {
#     "name": "Saad",
#     "age": 21,
#     "course": "python"
# }

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users",
   
# )
# print("Get",response.status_code)

# response = requests.post(
#     "https://jsonplaceholder.typicode.com/users",
#     json = student
# )
# print("Post",response.status_code)

# response = requests.put(
#     "https://jsonplaceholder.typicode.com/users/1",
#     json = student
# )
# print("Put",response.status_code)

# response = requests.delete(
#     "https://jsonplaceholder.typicode.com/users/1"
# )
# print("Delete",response.status_code)
# print(response.json())


import requests
student = {
    "name": "Saad",
    "age": 21,
    "Course": "Python"
}
response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)
data = response.json()
for user in data:
    print(user["name"],"-",user["email"])
print("Get : ",response.status_code)

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json = student
)
print("Post : ",response.status_code)

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/1",
     json=student
)
print("Put : ",response.status_code)

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/1"
)
print("Delete : ",response.status_code)