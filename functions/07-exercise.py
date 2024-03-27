# def is_palindrome(word: str):
#     word = word.replace(" ", "").strip().lower()
#     new_word = ""
#     for x in range(len(word)):
#         new_word += word[len(word) - (x + 1)]
#     condition = True if new_word == word else False
#     return condition

# new_word = is_palindrome("amo la paloma")
# print(new_word)


def is_palindrome(word: str):
    word = word.replace(" ", "").strip().lower()
    new_word = ""
    for char in reversed(word):
        new_word += char
    condition = True if new_word == word else False
    return condition

new_word = is_palindrome("pepe")
print(new_word)