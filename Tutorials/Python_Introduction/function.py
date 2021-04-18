###1
# print("Say Hi Game1 by Alex Bourg \n")
#
#
# def enterdata():
#     prenom = input("Enter your first name: ")
#     nom = input("Enter last name: ")
#     age = str(input("Enter your age: "))
#     print("\n" + "Hello " + prenom + " " + nom + "\n" + "You are " + age + "\n")
#
#
# enterdata()
#
#
# def cont():
#     answer = None
#     while answer not in ("y", "n"):
#         answer = input("Do you want to continue? y/n ").lower()
#         if answer == "y":
#             enterdata()
#             cont()
#         elif answer == "n":
#             exit()
#         else:
#             print("Please enter y or n")
#
#
# cont()


### 2 Cube
# print("Number Cubing Game by Alex Bourg \n")
# def cube(num):
#     return num*num*num
#
# def start():
#     num = float(input("Enter number: "))
#     result = cube(num)
#     print("Result= " + str(result) + "\n")
#     start()
#
# start()

### 3 Power
# print("Number powering Game by Alex Bourg \n")
# def raise_to_power(base_num, pow_num):
#     return base_num ** pow_num
#
# def start():
#     base_num = float(input("Enter number: "))
#     pow_num = float(input("Enter power: "))
#     result = raise_to_power(base_num, pow_num)
#     print("Result= " + str(result) + "\n")
#     start()
#
# start()


###4 Male/Female
# print("Gander Game by Alex Bourg \n")
# def enterdata():
#     answer = None
#     while answer not in ("y", "n"):
#         answer = input("Are you a male? y/n ").lower()
#         if answer == "y":
#             is_male = True
#         elif answer == "n":
#             is_male = False
#         else:
#             print("Please enter y or n")
#
#     if is_male:
#         print("You are a male!" + "\n")
#         enterdata()
#     else:
#         print("You are a female!" + "\n")
#         enterdata()
#
# enterdata()


###5 comparison

# print("Numbers Comparison Game by Alex Bourg \n")
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# print("\n" +
#       "The greatest number is " + str(max_num(num1, num2, num3)))



###6 number power using indexing

# print("Number powering Game by Alex Bourg \n")
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
#
# print(raise_to_power(float(input("Enter number: ")), int(input("Enter power: "))))