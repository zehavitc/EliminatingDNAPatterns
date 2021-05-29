from constants import infinity
from dna_utils import *

class Cost:
    default_cost_unit = 1
    default_transition_transversion_proportion = 1
    def __init__(self, sequence, cost_unit = default_cost_unit, transition_transversion_proportion = default_transition_transversion_proportion):
        self._sequence = sequence
        self._cost_unit = cost_unit if (cost_unit is not None) else self.default_cost_unit
        self._transition_transversion_propotion = transition_transversion_proportion if (transition_transversion_proportion is not None) \
            else self.default_transition_transversion_proportion

    def get(self, index, letter):
        """

        :param index: 1-based index
        :param letter:
        :return:
        """
        zero_based_idx = index - 1
        original_letters = extend_ambiguous_dna(self._sequence[zero_based_idx].lower()) #sequence can have upper case letters
        if (letter in original_letters):
            return 0
        # check the cost of a substitution
        if (self._sequence[zero_based_idx].isupper()):
            return infinity
        has_transversion = contains_transversion(original_letters)
        if (has_transversion):
            return self._cost_unit
        #no transversuin in original letters, they are all of the same shape
        if (is_transversion(letter,original_letters[0])):
            return self._cost_unit * self._transition_transversion_propotion
        return self._cost_unit

    def get_cost_of_seq(self, seq):
        if seq is None:
            return infinity #TODO - raise exception?
        if len(seq) != len(self._sequence):
            return infinity #TODO - raise exception?
        cost = 0
        for i in range(0, len(seq)):
            cost += self.get(i+1, seq[i]) #1-based index
        return cost




