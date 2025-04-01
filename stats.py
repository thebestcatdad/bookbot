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

def dictionary_to_list(totals):
    list_of_dictionaries = []
    for char, count in totals.items():
        list_of_dictionaries.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_of_dictionaries

