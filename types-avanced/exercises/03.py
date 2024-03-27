def sort_word(text):
    dictionary = {char: text.count(char) for char in text if char != ' '}
    return [count for count in sorted(dictionary.items(), key=lambda dictionary: dictionary[1])]

print(sort_word("hello world"))