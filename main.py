def report(book):
    print("--- Begin report of books/frankestein.txt ---")
    print(f"{get_word_count(book)} words found in the document\n")
    chars = get_char_count(book)
    sort = sorted(chars.items(), key=lambda x:x[1], reverse=True)
    for c in sort:
        letter, count = c
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def get_word_count(book):
    return len(book.split())

def get_char_count(book):
    book = book.lower()
    chars = {}

    for c in book:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars

def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        length = get_word_count(file_contents)
        # print(length)
        report(file_contents)


main()
