users = [
    ["Chanchito", 4],
    ["Felipe", 2],
    ["Pulga", 1]
]

# names = []

# for user_name, user_id in users:
#     names.append(user_name)

names = [user_name for user_name, user_id in users]

filter_names = [user[0] for user in users if user[1] > 2]

names = list(map(lambda user: user[0], users))
names = list(filter(lambda user: user[1] > 2, users))

print(names)