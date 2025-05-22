def get_book_text(book):
    with open(f"{book}") as b:
        contents = b.read()
    return contents

def get_word_count(book):
    words = get_book_text(book).split()
    count = 0
    for _ in words:
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


def sort_chars(book):
    chars_dict = get_char_count(book)
    sorted_list = []
    for chars in chars_dict:
        value = chars_dict[chars]
        new_dict = {'char': chars, 'num': value}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=lambda sort_on: sort_on["num"])
    return sorted_list
