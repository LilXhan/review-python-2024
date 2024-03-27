def large(text):
    result = 0
    for _ in text:
        result += 1
    return result

l = large("hello world")
print(l)