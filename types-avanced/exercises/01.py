def del_blank_spaces(text):
    return [char for char in text if char != ' ']

print(del_blank_spaces(" hello world "))