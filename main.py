from stats import get_book_text, get_num_words, get_char_count

path = "books/frankenstein.txt"
text = get_book_text(path)
word_count = get_num_words(text)
char_count = get_char_count(text)
print(char_count)