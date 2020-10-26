from string_utils import get_proper_prefixes_of_list
from KMP import *
from constants import infinity


class MultipleSoftElimination:
    def __init__(self, sequence, patterns, cost, alphabet):
        self._sequence = sequence
        self._patterns = patterns
        self._cost = cost #cost class that exposes get method
        self._alphabet = alphabet

    def eliminate(self):
        n = len (self._sequence)
        valid_prefixes = get_proper_prefixes_of_list(self._patterns)
        A = {i:{prefix:infinity for prefix in valid_prefixes} for i in range(0,n+1)}
        traceback  = {i:{prefix:(None, None) for prefix in valid_prefixes} for i in range(0,n+1)}
        #initialization
        A[0][""] = 0.0
        #update
        kmp_update_function = KmpUpdateFunction(self._patterns, valid_prefixes, self._alphabet)
        for i in range(1,n+1):
            for p in valid_prefixes:
                min_cost = infinity
                min_source = []
                for source in kmp_update_function.get_source_set(p):
                    val = A[i-1][source[0]] + self._cost.get(i, source[1])
                    if val <= min_cost and val != infinity:
                        if val == min_cost:
                            min_source.append(source)
                        else: #new minimum
                            min_cost = val
                            min_source = [source]
                A[i][p] = min_cost
                traceback[i][p] = min_source
        #construct the modified sequence
        i = n
        res_seq = list()
        min_cost = infinity
        min_prefix = None
        for p in valid_prefixes:
            prefix_cost = A[i][p]
            if  prefix_cost < min_cost:
                min_cost = prefix_cost
                min_prefix = p
        while i > 0 :
            pointers = traceback[i][min_prefix][0] #TODO: randomize?
            res_seq.insert(0, pointers[1])
            min_prefix = pointers[0]
            i -= 1
        return ''.join(res_seq)




