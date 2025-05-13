def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def char_count(path_to_file):
    lower_case_book = get_book_text(path_to_file).lower()
    counts = {}
    for ch in lower_case_book:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_characters(char_dict):
    char_list = []

    for ch, count in char_dict.items():
        char_list.append({"char": ch, "num": count})

    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list


    
def get_num_words(filepath):
    
    def split_into_words(fp):
        split_book = get_book_text(fp).split()
        return split_book

    def count_words(words: str):
        word_count = len(words)
        return word_count
    return split_into_words(filepath), count_words(split_into_words(filepath))
