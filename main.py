import sys
from stats import get_words, get_characters, sort_characters, print_characters

# Read in the file
def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    # Edge case where user doesnt input filepath to book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    text = get_book_text(file)
    characters = get_characters(text)
    sorted_list = sort_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_words(text)} total words")
    print("--------- Character Count -------")
    print_characters(sorted_list)
    print("============= END ===============")
       

main()
