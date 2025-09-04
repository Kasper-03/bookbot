def count_words(text):        
    return len(text.split())

def numbers_of_characters(text):
    lower_text = text.lower()
    d = {}
    for ch in lower_text:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d


def sort_on(items):
    return items["num"]

def raport(text):

    table = []
    for k, v in text.items():
        new_d = {"char": k, "num": v}
        table.append(new_d)
    table.sort(reverse=True, key=sort_on)    
    return table    