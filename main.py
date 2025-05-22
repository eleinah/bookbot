#!/usr/bin/env python3

from stats import get_word_count, sort_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book)} total words")
    print("--------- Character Count -------")
    sort_list = sort_chars(book)
    for dicts in sort_list:
        if dicts['char'].isalpha():
            print(f"{dicts['char']}: {dicts['num']}")
        else:
            continue
    print("============= END ===============")

if __name__ == "__main__":
    main()
