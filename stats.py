def word_count(file_contents):
    num_words = len(file_contents.split())
    return num_words

def char_count(book_text):
    lowercase_text = book_text.lower()
    
    dict = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        dict[letter] = 0

    for char in lowercase_text:
        if char in dict:
            dict[char] += 1

    return create_list(dict)

def sort_on(dict):
    return dict["num"]

def create_list(dict):
    list = []
    for pair in dict:
        new_dict = {}
        key = pair
        num = dict[pair]
        new_dict = {"char": key, "num": num}
        list.append(new_dict)

    list.sort(reverse=True, key=sort_on)
    
    return list