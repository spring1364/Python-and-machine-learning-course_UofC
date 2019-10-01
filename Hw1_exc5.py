#Authors: Nikoo Sabzevar, Sara Ghandehari

import random

def two_word_password():
    lines = open('words.txt', 'r').read().splitlines()
    random_words = random.sample(lines, 2)
    first_word = random_words[0]
    second_word = random_words[1]
    password = first_word.title() + second_word.title()

    while len(password) < 8 or len(password) > 10 or len(first_word) < 3 or len(second_word) < 3:
        random_words = random.sample(lines, 2)
        first_word = random_words[0]
        second_word = random_words[1]
        password = first_word.title() + second_word.title()
    return password

print(two_word_password())
