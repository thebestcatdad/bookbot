from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_num_words(text)
    print(f"{count_words} words found in the document")

def get_book_text(path):
     with open(path) as f:
        return f.read()

main()
