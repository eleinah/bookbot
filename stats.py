from main import get_book_text

def get_word_count(book):
    words = get_book_text(book).split()
    count = 0
    for word in words:
        count += 1
    return f"{count} words found in the document"
