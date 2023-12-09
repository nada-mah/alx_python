def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        a_dictionary.setdefault(k,value)
        if k == key:
           a_dictionary[k] = value
    a_dictionary[key] = value
    # a_dictionary.setdefault(key,value)
    return a_dictionary
