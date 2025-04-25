def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for letter in text:
        letter = letter.lower()
        if letter in char_count:
            char_count[letter] += 1
        else:
            char_count[letter] = 1
    return char_count


