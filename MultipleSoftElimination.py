import StringUtils
from KMP import *


class MultipleSoftElimination:
    def __init__(self, sequence, patterns, cost, alphabet):
        self._sequence = sequence
        self._patterns = patterns
        self._cost = cost
        self._alphabet = alphabet

    def eliminate(self):
        n = len (self._sequence)
        valid_prefixes = set()
        for p in self._patterns:
            valid_prefixes = valid_prefixes.union([pref for pref in StringUtils.get_all_proper_prefixes(p) if (not(pref in patterns) and not (any(pref.endswith(p) for p in patterns)))])
        A = {i:{prefix:float('inf') for prefix in valid_prefixes} for i in range(0,n+1)}
        traceback  = {i:{prefix:(None, None) for prefix in valid_prefixes} for i in range(0,n+1)}
        #initialization
        A[0][""] = 0.0
        #update
        kmp_update_function = KmpUpdateFunction(self._patterns, self._alphabet, valid_prefixes)
        for i in range(1,n+1):
            for p in valid_prefixes:
                min_cost = float('inf')
                min_source = []
                for source in kmp_update_function.get_source_set(p):
                    val = A[i-1][source[0]] + self._cost(i, source[1])
                    if val <= min_cost and val != float('inf'):
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
        min_cost = float('inf')
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


seq = "aabaa"
def cost(i, sigma):
    if seq[i-1] == sigma:
        return 0
    return 10
# cost = lambda i,sigma: 0 if seq[i] == sigma else 10
alphabet = ["a", "c", "g", "t"]
patterns = ["aab", "ab"]
alg = MultipleSoftElimination(seq, patterns, cost, alphabet)
print(alg.eliminate())



