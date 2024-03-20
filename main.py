def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    print(word_count(text))
    #print(letter_map())
    print(letter_count(text))

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
    count = letter_map()
    for char in text.lower():
        if (char not in count):
            continue
        else:
            count[char] += 1
    return count

def report(path):
    text = get_book_text(path)
    num_of_words = word_count(text)
    letter_report = letter_count(text)

    begining_section = f"--- Begin the Report of {path} ---\n"
    word_count_section = f"Total words in file: {num_of_words}\n"
    letter_count_section = ""
    for char in letter_report.keys():
        line = f"Character {char} appeared {letter_report[char]} times.\n"
        letter_count_section += line
    end_section = "--- End of Report ---"
    summary = begining_section + word_count_section + letter_count_section + end_section
    return summary

main()