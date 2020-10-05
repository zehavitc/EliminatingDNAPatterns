
def get_all_proper_prefixes(str):
    res = set()
    res.add("") #the empty string is always a proper prefix
    for j in range(1, len(str)):
        prefix = str[:j]
        res.add(prefix)
    return res



#print(get_all_strict_prefixes("abca"))#