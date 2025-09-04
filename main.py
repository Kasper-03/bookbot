import sys
from stats import count_words
from stats import numbers_of_characters
from stats import raport
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]    
    text = get_book_text(book_path) 
 
    num_words = count_words(text)

    num_char = numbers_of_characters(text)
    r_raport = raport(num_char)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in r_raport:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
main()            

