# marks = [45, 72, 88, 56, 91, 67]
# for mark in marks:
#     if mark >= 60 :
#         print(mark)

# marks = [45, 72, 88, 56, 91, 67]
# def get_passed_count(marks):
#     count = 0
#     for mark in marks:
#         if mark >= 60:
#             count += 1
#     return count
# print(get_passed_count(marks))

# user = input("Enter your full name: ")
# print(user.strip().split()[0])


# numbers = [2, 4, 6, 8, 10]
# multiply = [num * 2 for num in numbers]
# print(multiply)

# numbers = [1, 2, 3, 4, 5]
# evenNumber = [num for num in numbers if num%2 == 0]
# print(evenNumber)

# marks = [45, 72, 88, 51, 90, 33]
# newArray = [mark for mark in marks if mark >= 60]
# print(newArray)


# numbers = [1, 2, 3, 4, 5, 6]
# square = [num * num for num in numbers if num % 2 == 0]
# print(square)


# names = ["saad", "ali", "ahmed", "usman", "hamza"]
# newName = [name for name in names if len(name) > 4]
# print(newName)

# prices = [100, 250, 80, 500, 150]
# newPrice = [price + price * 10 / 100 for price in prices ]
# print(newPrice)

# marks = [45, 67, 82, 39, 91, 55]
# newMark = [mark + 5 for mark in marks if mark >= 50]
# print(newMark)


# marks = [35, 50, 65, 42, 80, 90]
# newmark = [mark + mark * 10 / 100 for mark in marks if mark >= 50]
# print(newmark)


# prices = [100, 250, 80, 500, 150]
# newPrices = [price - price * 20 / 100 for price in prices if price > 100]
# print(newPrices)


# numbers = [10, 15, 20, 25, 30, 35]
# newNumber = [num + num for num in numbers if num % 2 == 0]
# print(newNumber)

# multiply = lambda num : num * 10
# print(multiply(5))

# number = lambda a,b : a + b
# print(number(10,20))

# square = lambda num : num * num 
# print(square(6))

# checkEvenNumber = lambda num : num % 2 == 0 
# print(checkEvenNumber(7))

# checkPositiveNumber = lambda num : num > 0 
# print(checkPositiveNumber(1))


# cube = lambda num : num * num * num
# print(cube(3))


# checkNumber = lambda num : num >= 50 
# print(checkNumber(49))

# checkNumber = lambda a , b : a if a > b else b
# print(checkNumber(10,8))


# checkMark = lambda mark : "Pass" if mark >= 50 else "Fail"
# print(checkMark(70))