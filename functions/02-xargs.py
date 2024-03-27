# def sum(*xargs):
#     print(xargs)

def sum(*numbers): # transform parameters in iterables
    result = 0
    for number in numbers:
        result += number
    print(f"the result is: {result}")

sum(1, 2, 29, 59, 39)