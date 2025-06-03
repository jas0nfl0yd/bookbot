#!/usr/local/bin/python3

def get_num_words(contents: str) -> int:
    num_words = 0
    for word in contents.split():
        num_words += 1
    return num_words

def get_chars_dict(contents: str) -> int:
    chars = {}
    for char in contents:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num(item):
    return item['num']

def sort_dict_contents(contents: dict) -> dict:
    unsorted_dict = []
    for char, count in list(contents.items()):
        if char.isalpha():
            unsorted_dict.append({'char': char, 'num': count})
    sorted_dict = sorted(unsorted_dict, key=get_num, reverse=True)
    return sorted_dict
