from stats import get_word_count

def get_book_text(book):
    with open(f"books/{book}.txt") as b:
        contents = b.read()
    return contents

def main():
    print(get_word_count("frankenstein"))

if __name__ == "__main__":
    main()
