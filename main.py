def get_book_text(book):
    with open(f"books/{book}.txt") as b:
        contents = b.read()
    return contents

def get_word_count(book):
    words = get_book_text(book).split()
    count = 0
    for word in words:
        count += 1
    return f"{count} words found in the document"

def main():
    print(get_word_count("frankenstein"))

if __name__ == "__main__":
    main()
