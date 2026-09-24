# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("please enter a valid value!")

# try:
#     user1 = int(input("Enter your value : " ))
#     user2 = int(input("Enter your value : "))
#     print(user1 + user2)
# except ValueError:
#     print("Please enter valid Value!")

# try:
#     user1 = int(input("Enter your Value : "))
#     user2 = int(input("Enter your value : "))
#     result = user1 / user2
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by Zero!")

# try:
#     user1 = int(input("Enter your value: "))
#     user2 = int(input("Enter your value: "))
#     result = user1 / user2
#     print(result)
# except ValueError:
#     print("Please enter valid value!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     value = int(input("Enter your value: "))
#     print("Your number is : ", value)
# except ValueError:
#     print("Please enter valid number!")


# try:
#     user1 = int(input("Enter your value:"))
#     user2 = int(input("enter your value:"))
#     result = user1 + user2

# except ValueError:
#     print("please enter valid value!")
# else:
#     print("Sum is : ",result)


# try:
#     user = int(input("Enter your value:"))

# except ValueError:
#     print("Please enter valid value!")
# else:
#     print("Your value is :",user)
# finally:
#     print("Program finished!")

try:
    mark = int(input("Enter your marks:"))
    if mark < 0 or mark > 100:
        raise ValueError("Marks shpuld be between 0 to 100!")
except ValueError:
    print("please enter valid number!")
else:
    print("Valid marks:",mark)