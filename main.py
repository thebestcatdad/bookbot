def get_book_text(bookfile):
    file_contents = None
    with open(bookfile) as f:
        file_contents = f.read()
    return file_contents

def count_words(bookfile):
    word_count = 0
    book_text = get_book_text(bookfile)
    for i in book_text.split():
        word_count += 1
    return word_count

def main():
    print(f"{count_words("books/frankenstein.txt")} words found in the document")
    
main()
