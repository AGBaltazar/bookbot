from stats import text_to_words, text_to_characters, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        file_contents = get_book_text(filepath)
        
        # Get word count
        word_count = text_to_words(file_contents)
        
        # Get character count
        letter_count = text_to_characters(file_contents)
        
        # Get sorted characters
        sorted_chars = sort_chars(letter_count)    
    
        # Print the formatted report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        for char_dict in sorted_chars:
            if char_dict["char"].isalpha():  # Only print alphabetical characters
                print(f"{char_dict['char']}: {char_dict['count']}")

main()