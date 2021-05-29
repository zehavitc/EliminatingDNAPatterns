
class Node:
    def __init__(self, letter, children = None, is_prefix = False):
        self.letter = letter
        self.is_prefix = is_prefix
        if children is None:
            self.children = [] ##Can't use empty list as a default parameter as it is being evaluated only once upon function definition
        else:
            self.children = children

class KMPTrie:
    #TODO document
    """

    """
    #metadata keeps track of if the suffix so far belongs to a pattern prefix
    def __init__(self):
        self.root = Node(letter='', children=[], is_prefix=False)

    def get_longest_prefix_that_is_a_suffix(self, str):
        res_suffix_len = 0
        index_of_letter_to_compare = len(str) - 1
        comparison_failed = False
        current_node = self.root
        while index_of_letter_to_compare >= 0 and not comparison_failed:
            comparison_failed = True
            for child in current_node.children:
                if child.letter == str[index_of_letter_to_compare]:
                    if child.is_prefix:
                        res_suffix_len = len(str) - index_of_letter_to_compare
                    comparison_failed = False
                    current_node = child
                    break
            index_of_letter_to_compare = index_of_letter_to_compare - 1
        if (res_suffix_len == 0):
            return ""
        return str[-res_suffix_len:]

    def add_prefix(self, pref):
        current_node = self.root
        index_of_letter_to_add = len(pref)  - 1
        while index_of_letter_to_add >= 0:
            found_node = False
            for child in current_node.children:
                if child.letter == pref[index_of_letter_to_add]:
                    current_node = child
                    found_node = True
                    break
            if not (found_node):
                new_node = Node(letter=pref[index_of_letter_to_add])
                current_node.children.append(new_node)
                current_node = new_node
            if (index_of_letter_to_add == 0):
                current_node.is_prefix = True  # This is the first letter of a prefix
            index_of_letter_to_add = index_of_letter_to_add - 1

