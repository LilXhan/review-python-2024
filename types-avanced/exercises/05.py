def print_high_char(text):
    dictionary = {char: text.count(char) for char in text if char != ' '}
    list_tuple = [tuplee for tuplee in sorted(dictionary.items(), key=lambda tuplee: tuplee[1])]
    high_tuple = [tuplee for tuplee in filter(lambda tuplee: tuplee[1] >= list_tuple[-1][1], list_tuple)]
    
    info = f'The characters that high repeat with {list_tuple[-1][1]} are: '

    for char, _ in high_tuple:
        info += f'\n -{char.capitalize()}'

    return info


print(print_high_char("hello woorlddd"))