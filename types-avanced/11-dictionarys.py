point = {'x': 25, 'y': 50}

print(point['x'])

point["z"] = 45 # add
print(point)

if "lala" in point:
    print("found lala!", point["lala"])


print(point.get("x")) # 25
print(point.get("lala")) # None
print(point.get("lala", 97)) # 97
del point["x"]
del (point["y"])
 
print(point)

point["x"] = 25

for key in point:
    print(key, point[key])


for key, value in point.items(): # (x, 25)
    print(f"{key}, {value}")


users = [
    {
        'id': 1,
        'name': 'Chanchito',
    },
    {
        'id': 2,
        'name': 'Feliz',
    },
    {
        'id': 3,
        'name': 'Pepe',
    },
    {
        'id': 4,
        'name': 'Felipe',
    },
    {
        'id': 5,
        'name': 'Corzo',
    }
]

for user in users:
    print(user['name'])