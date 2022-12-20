def stringDistance(Woah):
    print(Woah[ ::-1])

stringDistance('Bull')
stringDistance('Chicken Nuggets')

def checkNumeral():
    newList = []
    Numeral = range(100, 401)
    for num in Numeral:
        if num % 2 == 0:
            newList.append(num)
    return (newList)

print(checkNumeral())
