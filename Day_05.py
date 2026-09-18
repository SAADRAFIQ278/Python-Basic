# marks = [45, 72, 88, 56, 91, 67]
# for mark in marks:
#     if(mark >= 60):
#         print(mark)


# marks = [45, 72, 88, 56, 91, 67]
# count = 0
# total = 0

# for mark in marks:
#     if(mark >= 60):
#         total += mark
#         count += 1
# average = total /count
# print(average)

# def show_marks():
#     print("My marks are 85")

# show_marks()
# show_marks()


# def show_marks(mark):
#     print("mark are : " , mark)

# show_marks(85)
# show_marks(75)

# def calculate_square(number):
#     print(number * number)

# calculate_square(5)
 
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(12,5)
# print(result)


# def check_pass(marks):
#     if(marks >= 60):
#         print ("Pass!")
#     else: print("Fail!") 

# check_pass(75)
# check_pass(45)

# marks = [45, 72, 88, 56, 91, 67]
# def average_marks(marks):
#         total = 0
#         count = 0
#         for mark in marks:
#                 total += mark
#                 count += 1 
#         average_marks = total / count
#         return average_marks
# result = average_marks(marks)
# print(result)

# def calculate_discount(price, discount=10):
#     total = price * discount /100
#     finalprice =  price - total
#     return finalprice
# result = calculate_discount(8000)
# print(result)

# def calculate_bill(bill,tax=5):
#     total = bill * tax / 100
#     finalPrice = bill + total
#     return finalPrice
# result = calculate_bill(1000,10)
# print(result)

# def calculate_salary(basic_salary, bonus=5000):
  
#     final_Salary = basic_salary + bonus
#     return final_Salary
# result = calculate_salary(30000,1200)
# print(result)

# marks = [70, 80, 90, 60]
# def calculate_total(marks):
#      total = 0
#      for mark in marks:
#           total += mark
#      return total 

# result = calculate_total(marks)
# print(result)

marks = [45, 72, 88, 56, 91, 67]    
def calculate_passed_average(marks):
    total = 0
    count = 0
    for mark in marks:
        if(mark >= 60):
            total += mark 
            count += 1
    average = total / count
    return average
result = calculate_passed_average(marks)
print(result)
