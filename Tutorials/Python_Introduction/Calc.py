print("Basic Calculator by Alex Bourg \n")

num1 = float(input("Enter first number: "))

op = input("Operator (*/+-)? ")
while op not in ("+", "-", "/", "*"):
    print("Invalid operator!")
    op = input("Operator (*/+-)? ")

num2 = float(input("Enter second number: "))

while num2 == 0 and op == "/":
    print("You cannot divide by zero!")
    num2 = float(input("Enter second number: "))


#num3 = float(input("Enter third number: "))

if op == "+":
    y = (num1 + num2)
    print("Result is: " + str(y))

elif op == "/":
        y = (num1 / num2)
        print("Result is: " +str(y))

elif op == "-":
    y = (num1 - num2)
    print("Result is: " +str(y))

elif op == "*":
    y = (num1 * num2)
    print("Result is: " +str(y))


# if y > num3:
#     print(str(y) + " is greater than " + str(num3))
# elif y < num3:
#     print(str(y) + " is smaller than " + str(num3))
# else:
#     print(str(y) + " is equal to " + str(num3))