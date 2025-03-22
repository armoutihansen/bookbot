def count_nums(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict:
    text_lower = text.lower()
    dict_of_chars = {}
    for c in set(text_lower):
        dict_of_chars[c] = 0
        
    for c in text_lower:
        dict_of_chars[c] += 1
    
    return dict_of_chars

def sort_on(d):
    return d["count"]

def sorted_list(char_dict: dict) -> list:
    lst = []
    for key in char_dict:
        lst.append({"character": key, "count": char_dict[key]})
    
    lst.sort(reverse=True, key=sort_on)
    
    return lst