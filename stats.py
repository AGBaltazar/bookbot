def text_to_words(file_contents):
    word_count = file_contents.split()
    total_words = len(word_count)
    return total_words

def text_to_characters(file_contents):
    character_dict = {}
    for letter in file_contents:
        letter = letter.lower()
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict

def sort_chars(char_dict):
    sorted_char = []
    for char, count in char_dict.items():
        # Use dictionary syntax, not set syntax
        sorted_char.append({"char": char, "count": count})
    
    # Use a function for the sorting key
    def sort_on(dict_item):
        return dict_item["count"]
    
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char