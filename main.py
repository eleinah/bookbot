#!/usr/bin/env python3

import stats

def main():
    book = "frankenstein"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {stats.get_word_count(book)} total words")
    print("--------- Character Count -------")
    sort_list = stats.sort_chars(book)
    for dicts in sort_list:
        print(f"{dicts['char']}: {dicts['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
