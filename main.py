def get_book_text(bookfile):
    file_contents = None
    with open(bookfile) as f:
        file_contents = f.read()
    return file_contents

def count_words(bookfile):
    book_text = get_book_text(bookfile)
    word_count = len(book_text.split())
    return word_count

def main():
    print(f"{count_words('books/frankenstein.txt')} words found in the document")
    
main()
