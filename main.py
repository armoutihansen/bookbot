import sys
from stats import count_nums, count_characters, sorted_list

def get_book_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        
    return file_contents

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
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path, "...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for dict in sorted_lst:
        if dict["character"].isalpha():
            print(dict["character"],":",dict["count"])
    print("============= END ===============")

main()