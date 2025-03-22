import sys
from stats import count_nums, count_characters, sorted_list

def main():
    # path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_nums(text)
    count_dict = count_characters(text)
    sorted_lst = sorted_list(count_dict)
    print_report(path, num_words, sorted_lst)
    

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        
    return file_contents

def print_report(path: str, num_words: int, sorted_lst: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_lst:
        if dict["character"].isalpha():
            print(f"{dict['character']}: {dict['count']}")
            
    print("============= END ===============")
    

main()