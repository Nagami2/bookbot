from stats import get_word_count, get_character_count, sort_char_dict

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        # reads the content of the file and returns it as a string
        return file.read()
    


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    dict_char = get_character_count(text)
    
    sorted_char_list = sort_char_dict(dict_char)
    for item in sorted_char_list:
        char, num = item["char"], item["num"]
        # only print characters that are letters
        if char.isalpha():
            print(f"{char}: {num}")



main()