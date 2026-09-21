# students = [
#     {"name": "Ali", "marks": 45},
#     {"name": "Saad", "marks": 78},
#     {"name": "Hamza", "marks": 62},
#     {"name": "Usman", "marks": 35}
# ]
# for student in students:
#     if student["marks"] >= 50:
#         print(student["name"])


# marks = [45, 72, 38, 90, 65, 49, 80]
# newMarks = [mark + mark * 10 / 100 for mark in marks if mark >= 50 ]
# print(newMarks)


# marks = [60, 70, 80, 90]
# def calculate_average(marks):
#     total = 0
#     for mark in marks :
#         total += mark

#     average = total / len(marks)
#     return average

# print(calculate_average(marks))
    

# email = "  SAAD@GMAIL.COM  "
# print(email.strip().lower())


# numbers = [2, 4, 6, 8]

# newNumber = list(map(lambda num : num + num,numbers))
# print(newNumber)
    

# marks = [35, 55, 72, 40, 90, 48]
# new_mark = list(filter(lambda mark : mark >= 50 , marks))
# print(new_mark)

# marks = [35, 55, 72, 40, 90, 48, 65]
# passing_marks = list(filter(lambda mark : mark >= 50 , marks))
# new_marks = list(map(lambda passing_marks : passing_marks + passing_marks * 10 / 100, passing_marks))
# print(new_marks)

# prices = [100, 200, 300, 400]
# greater_price = list(filter(lambda price : price >= 200 , prices))
# new_price = list(map(lambda newPrice : newPrice - newPrice * 20 / 100, greater_price))
# print(new_price)


