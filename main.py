from stats import get_num_words
from stats import get_num_letters
from stats import dictionary_to_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    print(f"{count_words} words found in the document")
    count_letters = get_num_letters(text)
    print(count_letters)
    print("=========")
    temp_list = dictionary_to_list(count_letters)
    print(temp_list)

def get_book_text(path):
     with open(path) as f:
        return f.read()

main()
