#!/usr/bin/env python3

import stats
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage:\npython3 main.py <book.txt>")
        sys.exit(1)

    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}...")
    print("----------- Word Count ----------")
    print(f"Found {stats.get_word_count(book)} total words")
    print("--------- Character Count -------")
    sort_list = stats.sort_chars(book)
    for dicts in sort_list:
        if dicts['char'].isalpha() == True:
            print(f"{dicts['char']}: {dicts['num']}")
        else:
            continue
    print("============= END ===============")

if __name__ == "__main__":
    main()
