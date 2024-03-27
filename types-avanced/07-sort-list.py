numbers = [1, 23, 2, 34, 2, 31, 3123, 4, 9]

sorted(numbers, reverse=True) # return new list
numbers.sort(reverse=True) # edit numbers
print(numbers)

users = [['Pepe', 4], ['Felipe', 1], ['Pulga', 2]]
users.sort(key=lambda el: el[1])
print(users)