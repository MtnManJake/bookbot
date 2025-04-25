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
    
def sort_char_counts(char_count):
    sorted_char_count = []
    for char, count in char_count.items():
        if char.isalpha():
            entry = {'char':char, 'num': count}
            sorted_char_count.append(entry)
            sorted_char_count.sort(key=lambda x: x['num'], reverse=True)
    return sorted_char_count
            



    
