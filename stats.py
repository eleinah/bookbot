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

def get_char_count(book):
    words = get_book_text(book).split()
    chars = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    # Convert every word to lowercase:
    for index, word in enumerate(words):
        words[index] = word.lower()
    for word in words:
        for char in word:
            if char in chars:
                chars[char] += 1
    return chars
