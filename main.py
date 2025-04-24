from stats import get_book_text, get_num_words

path = "books/frankenstein.txt"
text = get_book_text(path)
word_count = get_num_words(text)

print(f"{word_count} words found in the document")