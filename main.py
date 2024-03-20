def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(word_count(text))
    #print(letter_map())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_text):
    word_list = book_text.split()
    count = len(word_list)
    return count

def letter_map():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_map = {}
    for char in alphabet:
        letter_map[char] = 0
    return letter_map

def letter_count(text):
    
    pass

main()