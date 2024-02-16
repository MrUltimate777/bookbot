def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(word_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_text):
    word_list = book_text.split()
    count = len(word_list)
    return count

main()