# marks = [45, 72, 88, 56, 91, 67]
# for mark in marks:
#     if(mark >= 60):
#         print(mark)

# marks = [45, 72, 88, 56, 91, 67]
# count = 0
# total = 0
# for mark in marks :
#     if(mark >= 60):
#         total += mark
#         count += 1

# average = total/count
# print(average)


# marks = [45, 72, 88, 56, 91, 67]

# def get_passed_count(marks):
#     count = 0
#     for mark in marks:
#         if mark >= 60:
#           count += 1
#     return count 

# result = get_passed_count(marks)
# print(result)

# name = "    Saad rafiq  "

# print(name.strip().upper())

# text = "Saad Rafiq Peshawar"
# part = text.split()
# print(part[0])


# name = input('Enter your Name : ')
# part = name.strip().split()
# print(part[0])


# name = input('Enter your email : ')
# part = name.strip().split("@")
# print(part[0])

# name = input("Enter your email : ")
# part = name.strip().split("@")
# print(part[1])


# name = input("Enter your Name : ")
# city = input("Enter your city : ")
# name = name.strip()
# city = city.strip()
# print("Name : ", name)
# print("City : ", city)

# user = input("Enter your email : ")
# userEmail = user.strip().lower()
# print(userEmail)

# text = "I love Python"
# print(text.replace("Python" , "JavaScript"))

# user =   " SAAD@GMAIL.COM  " 

# print(user.strip().lower().replace("gmail","outlook"))



# text = "I love Python"
# print(text.find("Python"))

# text = "I love Python and Python is easy"
# print(text.count("Python"))

# text = "Python is easy"
# print(text.startswith("Python"))

# text = "myfile.pdf"
# print(text.endswith("pdf"))

# text =   input("Enter your email : ") 
# text = text.strip().lower()
# if(text.endswith("@gmail.com")):
#     print("This is a Gmail account")
# else: print("This is not a Gmail account ")


# user = input("Enter your name : ")
# text = user.strip().upper()
# if "SAAD" in text:
#     print("Welcome Saad!")
# else: print("Welcome User!")

text = "I love Python"
text.split()
result = "-".join(text.split())
print(result)
