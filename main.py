#!/usr/local/bin/python3

# imports
from stats import get_num_words, get_chars_dict, sort_dict_contents
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def analyze_book(filepath: str):
    print(f'Analyzing book found at {filepath}...')
    book_contents = get_book_text(filepath)
    print('----------- Word Count ----------')
    num_words = get_num_words(book_contents)
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    chars = get_chars_dict(book_contents)
    sorted_dict = sort_dict_contents(chars)
    for item in sorted_dict:
        print(f'{item["char"]}: {item["num"]}')

def main(book_filename: str):
    print('============ BOOKBOT ============')
    analyze_book(book_filename)
    print('============= END ===============')

if __name__ == "__main__":
    # check args
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_filename = sys.argv[1]

    main(book_filename)

