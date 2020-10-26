from constants import infinity
from dna_utils import *

class Cost:
    def __init__(self, sequence, cost_unit = 1, transition_transversion_propotion = 2):
        self._sequence = sequence
        self._cost_unit = cost_unit
        self._transition_transversion_propotion = transition_transversion_propotion

    def get(self, index, letter):
        original_letters = extend_ambiguous_dna(self._sequence[index].lower()) #sequence can have upper case letters
        if (letter in original_letters):
            return 0
        # check the cost of a substitution
        if (self._sequence[index].isupper()):
            return infinity
        has_transversion = contains_transversion(original_letters)
        if (has_transversion):
            return self._cost_unit
        #no transversuin in original letters, they are all of the same shape
        if (is_transversion(letter,original_letters[0])):
            return self._cost_unit * self._transition_transversion_propotion
        return self._cost_unit



