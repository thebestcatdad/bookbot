def get_num_words(text):
    word_count = text.split()
    return len(word_count)
    
def get_num_letters(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count