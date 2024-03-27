list1 = [1, 2, 3]
list2 = [4, 5]
print(*list1) # 1 2 3
print(1, 2, 3) # 1 2 3

new_list = [*list1, 5, *list2]
print(new_list)

point1 = {'x': 19, 'y': 25}
point2 = {'y': 15}

newPoint = {**point1, 'z': 10, **point2}

print(newPoint) # replaced point2['y'] to point1['y']
# {'x': 19, 'y': 25}

