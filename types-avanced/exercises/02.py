def count_chars(text: str):
    return {char: text.count(char) for char in text}

print(count_chars("hellossssss"))