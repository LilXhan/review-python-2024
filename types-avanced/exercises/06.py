def del_blank_spaces(text):
    return [char for char in text if char != ' ']

text_list = del_blank_spaces("helloo world")

def count_chars(text_list):
    return {char: text_list.count(char) for char in text_list}

dictionary = count_chars(text_list)

def sort_word(dictionary):
    return [count for count in sorted(dictionary.items(), key=lambda dictionary: dictionary[1])]

tuplee_sorted = sort_word(dictionary)

def high_value(tuplee_sorted):
    high_tuple = [tuplee for tuplee in filter(lambda tuplee: tuplee[1] >= tuplee_sorted[-1][1], tuplee_sorted)]
    return high_tuple

only_high_values = high_value(tuplee_sorted)

def print_high_char(only_high_values):
    info = f'The characters that high repeat with {only_high_values[-1][1]} are: '
    for char, _ in only_high_values:
        info += f'\n -{char.capitalize()}'
    return info


print(print_high_char(only_high_values))