import sys

from stats import get_num_words, sort_characters
from stats import char_count

print("Usage: python3 main.py <path_to_book>")



path_to_file = sys.argv[1]
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    
def main():
#    print(get_book_text(path_to_file))
#    get_num_words(path_to_file)
    characters = char_count(path_to_file)
    def crunch_data():
        print("============ BOOKBOT ============")
        print("Analyzing book found at", path_to_file)
        word_count = get_num_words(path_to_file)
        print("----------- Word Count ----------")
        print(f"Found {word_count[1]} total words")

        characters = char_count(path_to_file)
        sorted_chars = sort_characters(characters)

        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")

        print("============= END ===============")
    
    crunch_data()
main()
