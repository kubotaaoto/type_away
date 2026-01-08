def count_num_chars(words):
    count = 0
    list_of_words = words.split(" ")
    for word in list_of_words:
        count += len(word)
    return count