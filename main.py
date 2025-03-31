def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    print(f"{count_words} words found in the document")

def get_book_text(path):
     with open(path) as f:
        return f.read()

def get_count_words(text):
    word_count = text.split()
    return len(word_count)
    
main()
