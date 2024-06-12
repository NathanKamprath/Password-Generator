import string
import random

Password = []
strings = string.printable[:94]
count = 0
Letters = strings[10:62]
Numbers = strings[:10]
Symbols = strings[62:]
creating = True
char = 1

while creating:
    print("Welcome to the Python Password Generator!")
    print('How long would you like your password to be?\n(between 5 and 24 characters)')
    length = int(input())

    if length < 5 or length > 24:
        print("Error, number of characters not allowed")
        creating = True
    else:
        pass

    print("How many symbols would you like?")
    symb = int(input())
    if symb < length:
        print("How many numbers would you like?")
        numb = int(input())

        if symb + numb < length:
            print("How many letters would you like?")
            lett = int(input())

            if symb + numb + lett <= length:
                break
            else:
                print("Error, too many characters for the number specified. Please try again")
                creating = True

        elif symb + numb > length:
            print("Error, too many characters for the number specified. Please try again")
            creating = True
        else:
            break

    elif symb > length:
        print("Error, too many characters for the number specified. Please try again")
        creating = True
    else:
        break

while char <= length:
    while symb > 0:
        Password.append(random.choice(Symbols))
        symb -= 1
    while lett > 0:
        Password.append(random.choice(Letters))
        lett -= 1
    while numb > 0:
        Password.append(random.choice(Numbers))
        numb -= 1
    char += 1

#2 shuffles for good measure
random.shuffle(Password)
random.shuffle(Password)

Password = ''.join(Password)
print(Password)