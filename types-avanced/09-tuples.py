# not modified, not add elements, no delete elements

numbers = (1, 2, 3) + (4, 5, 6)
print(numbers)

point = tuple([1, 2])
print(point)

lowNumbers = numbers[:2]
print(lowNumbers)

first, second, *others = numbers

for n in numbers:
    print(n)

listNumbers = list(numbers)
listNumbers[0] = "Chanchito feliz"
print(listNumbers)

