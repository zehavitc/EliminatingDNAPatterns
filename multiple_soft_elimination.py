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
        kmp_update_function = KmpUpdateFunction(patterns=self._patterns, alphabet=self._alphabet)
        for i in range(1,n+1):
            for p in valid_prefixes:
                min_cost = infinity
                min_source = []
                for source in kmp_update_function.get_source_set(p):
                    pref = source[0]
                    sigma = source[1]
                    val = A[i-1][pref] + self._cost.get(i, sigma)
                    if val <= min_cost and val != infinity:
                        if val == min_cost:
                            min_source.append(source)
                        else: #new minimum
                            min_cost = val
                            min_source = [source]
                A[i][p] = min_cost
                traceback[i][p] = min_source #list of pairs (pref, sigma)
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
        if min_prefix is None:
            return None
        while i > 0 :
            pointers = traceback[i][min_prefix][0] #TODO: randomize?
            res_seq.insert(0, pointers[1])
            min_prefix = pointers[0]
            i -= 1
        return ''.join(res_seq)




