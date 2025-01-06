import os
import re
from collections import Counter

# path = str('books\\' + os.listdir('books')[0])

# txt = open(path, 'r', encoding='utf8')
# f = txt.read()
# # n_of_words = len(re.findall("[\w']+", f.lower()))
# f_n_of_words = len(f.split())

# # n_of_char = zip(dict([for i in len(re.findall("[\w']", f.lower()))]))
# char_dict = Counter(re.findall("(.)", txt.lower()))


# print(f"--- Begin report of {path} ---")
# print(f"{f_n_of_words} words found in the document")
# print()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
