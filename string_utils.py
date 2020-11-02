
def get_proper_prefixes_of_str(str):
    if str == "":
        return None # no proper prefix for the empty string
    res = set()
    res.add("") #the empty string is always a proper prefix
    for j in range(1, len(str)):
        prefix = str[:j]
        res.add(prefix)
    return res

def get_proper_prefixes_of_list(strings):
    proper = set()
    for str in strings:
        proper = proper.union([pref for pref in get_proper_prefixes_of_str(str) if (
        not (pref in strings) and not (any(pref.endswith(str_) for str_ in strings)))])
    return proper



#print(get_all_strict_prefixes("abca"))#