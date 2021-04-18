from random import randint

y = randint(1, 110)
print('--> Welcome to the age guessing game! (Max age: 110)')

# We create an empty list, for the wrong guess... to avoid guessing the same number again
wrongguess = []


def run():
    global y
    print('*** is your age = ', y, '?')
    x = input("Enter '+', '-', or '=': ")
    print('\n')
    if x == '+':
        if y != 110:
            wrongguess.append(y)
            while y in wrongguess:
                y = randint(wrongguess[-1], 110)
            run()
            # print(wrongguess[-1])
        else:
            print('   Error, age cannot be more than 110!')
            run()

    elif x == '-':
        if y != 1:
            wrongguess.append(y)
            while y in wrongguess:
                y = randint(1, wrongguess[-1])
            run()
        else:
            print('   Error, age cannot be less than 1!')
            run()

    elif x == '=':
        print('\n')
        print('*** YOU WON! ***')
        print('Your age is: ', y)

    else:
        print("Error! Please enter only '+', '-', or '='", '\n')
        run()


run()