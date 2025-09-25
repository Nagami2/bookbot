# from collections import defaultdict

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    char_count = {}
    
    lowered_text = text.lower()
    
    for char in lowered_text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def sort_char_dict(char_dict):
    def sort_on(item):
        return item["num"]
    
    # convert the dictionary into a list of dictionaries
    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})

    # sort the list
    char_list.sort(reverse=True, key=sort_on)
    return char_list

