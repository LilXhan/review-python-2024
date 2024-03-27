numbers = [1, 2, 3]

# ugly!
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, second, third = numbers
print(first)

first1, *others = numbers
print(first1, others)

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first11, second22, *others = numbers2
print(first11, second22)

first111, second111, *others, penul, last = numbers2
print(first111, second111, penul, last)