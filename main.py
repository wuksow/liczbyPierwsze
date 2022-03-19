numbers = range(0, 100)


def checkNumber(liczba):
    checkbool = False
    if liczba <= 1:
        return checkbool
    for elements in range(2, liczba):
        if liczba % elements == 0:
            return checkbool
    return True


for elements in numbers:
    if checkNumber(elements):
        print(elements)
