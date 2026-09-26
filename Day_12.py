# with open("student.txt", "r")as file:
#     data = file.read()
#     print(data)

# with open("student.txt", "r") as file:
#    first = file.readline()
#    second = file.readline()
#    print(first)
#    print(second)

# with open("student.txt","r") as file:
#     students = file.readlines()
#     for student in students:
#         print(student.strip())


# with open("student.txt","w") as file:
#     file.write("Huziafa \n")
   
# with open("student.txt","w") as file:
#     file.write("saad\n")
#     file.write("Ahmad\n")
#     file.write("Ali\n")

# with open("student.txt","a") as file:
#     file.write("Huzaifa\n")

with open("student.txt","r") as file:
    data = file.read()
    data = data.replace("Ahmad","Bilal")
with open("student.txt","w") as file:
    file.write(data)