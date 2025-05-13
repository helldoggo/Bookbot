from stats import get_num_words
from stats import char_count

path_to_file = "books/frankenstein.txt"
    
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


    
def main():
    print(get_book_text(path_to_file))
    get_num_words(path_to_file)
    characters = char_count(path_to_file)
    print(characters)
main()
