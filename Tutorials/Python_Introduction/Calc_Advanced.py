print("Advanced Calculator by Alex Bourg \n")


def enterdatax():
    global num1
    num1 = float(input("Enter first number: "))

    global op
    op = input("Operator (*/+-)? ")
    while op not in ("+", "-", "/", "*"):
        print("Invalid operator!")
        op = input("Operator (*/+-)? ")

    global num2
    num2 = float(input("Enter second number: "))
    while num2 == 0 and op == "/":
        print("You cannot divide by zero!")
        num2 = float(input("Enter second number: "))
    calc()


def plusx():
    y = (num1 + num2)
    print("Result is: " + str(y))
    enterdatax()


def dividex():
    y = (num1 / num2)
    print("Result is: " + str(y))
    enterdatax()


def minx():
    y = (num1 - num2)
    print("Result is: " + str(y))
    enterdatax()


def multix():
    y = (num1 * num2)
    print("Result is: " + str(y))
    enterdatax()


def calc():
    if op == "+":
        plusx()
    elif op == "/":
        dividex()
    elif op == "-":
        minx()
    elif op == "*":
        multix()


enterdatax()
