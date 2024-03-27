# group or conjunt

first = {1, 1, 2, 2, 3, 4} # remove duplicateds
second = [3, 4, 5]
second = set(second)
print(second)

print(first | second) # union {1, 2, 3, 4 , 5}
print(first & second) # interseccion {3, 4}
print(first - second) # diferencia {1, 2}
print(first ^ second) # diferencia simetrica {1, 2, 5}

if 5 in second:
    print("hello world")