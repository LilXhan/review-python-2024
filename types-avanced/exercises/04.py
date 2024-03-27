def high_value(text):
    dictionary = {char: text.count(char) for char in text if char != ' '}
    list_tuples = [tuplee for tuplee in sorted(dictionary.items(), key=lambda tuplee: tuplee[1])]
    high_tuple = [tuplee for tuplee in filter(lambda tuplee: tuplee[1] >= list_tuples[-1][1], list_tuples)]
    return high_tuple


print(high_value("helloo world"))