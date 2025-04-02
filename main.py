import sys
from stats import get_num_words
from stats import get_num_letters
from stats import dictionary_to_list

def main():
    book_path = get_book_path(sys.argv)
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    count_letters = get_num_letters(text)
    sorted_list = dictionary_to_list(count_letters)
    print_results(book_path, count_words, sorted_list)

def get_book_path(path):
    if len(path) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return path[1]


def get_book_text(path):
     with open(path) as f:
        return f.read()
     
def print_results(book_path, count_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words" )   
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")


main()
