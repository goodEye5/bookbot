def get_num_words(str):
    return len(str.split())



def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
    return chars

