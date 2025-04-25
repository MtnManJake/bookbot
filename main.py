from stats import get_book_text, get_num_words, get_char_count, sort_char_counts

path = "books/frankenstein.txt"
text = get_book_text(path)
word_count = get_num_words(text)
char_count = get_char_count(text)
sorted_chars = sort_char_counts(char_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")