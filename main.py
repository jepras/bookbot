from stats import word_count, char_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file = get_book_text(filepath)
    
    num_words = word_count(file)
    char_list = char_count(file)

    print_report(filepath, num_words, char_list)    
    

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(filename, word_count, char_list):
    print(f"""============ BOOKBOT ============
Analyzing book found at {filename}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for dict in char_list:
        char = dict["char"] + ":"
        num = dict["num"]
        print(char, num)

main()