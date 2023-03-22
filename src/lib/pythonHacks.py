def sort_a_string(word: str):
    return ''.join(sorted(word))


def check_hashmap_keys(hashmap: dict, word: str):
    return word in dict  # the most simple one
    return word in dict.keys()
    return dict.__contains__(word)
