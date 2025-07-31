import sys
from stats import get_word_count, get_letter_count, get_letter_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    book = get_book_text(file_path)
    print("="*10, "BOOKBOT", "="*10)
    print(f"Analyzing book found at {file_path}...")
    print("-"*8, "Word Count", "-"*8)
    print(f"Found {get_word_count(book)} total words")
    print("-"*6, "Character Count", "-"*6)
    characters = get_letter_count(book)
    char_dict = get_letter_dict(characters)

    for char in char_dict:
        if char['name'].isalpha():
            print(f"{char['name']}: {char['count']}")

    print("="*12, "END", "="*12)










main()
