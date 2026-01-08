from english_1k import english_1k
import random

def generate_words():
    res = ""
    for i in range(15):
        random_index = random.randrange(0, len(english_1k) - 1)
        res += english_1k[random_index] + " "
    res += "\n"
    return res