def word_counter(text):
    num_words = text.split()
    return len(num_words)

def character_counter(text):
    dict = {}

    for i in text:
        if i.lower() in dict:
            dict[i.lower()] = dict[i.lower()] + 1
        else:
             dict[i.lower()] = 1
        
    return dict


def sortHelp(key):
    return key["num"]

def full(dict):
    list = []
    for i, b in dict.items():
        dict = {}
        if i.isalpha():
            dict["char"] = i
            dict["num"] = b
            list.append(dict)

    list.sort(key=sortHelp)
    return(list[::-1])