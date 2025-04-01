from stats import get_num_words
from stats import get_num_letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    print(f"{count_words} words found in the document")
    count_letters = get_num_letters(text)
    print(f"{count_letters} of each letter found in the document")

def get_book_text(path):
     with open(path) as f:
        return f.read()

main()
