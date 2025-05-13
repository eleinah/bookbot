def get_book_text(book):
    with open(f"{book}") as b:
        contents = b.read()
    return contents

def get_word_count(book):
    words = get_book_text(book).split()
    count = 0
    for word in words:
        count += 1
    return count

def get_char_count(book):
    words = get_book_text(book).split()
    chars = {}
    # Convert every word to lowercase:
    for index, word in enumerate(words):
        words[index] = word.lower()
    for word in words:
        for char in word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def sort_on(dict):
    return dict['num']

def sort_chars(book):
    chars_dict = get_char_count(book)
    sorted = []
    for chars in chars_dict:
        value = chars_dict[chars]
        new_dict = {}
        new_dict['char'] = chars
        new_dict['num'] = value
        sorted.append(new_dict)
    sorted.sort(reverse=True, key=sort_on)
    return sorted
