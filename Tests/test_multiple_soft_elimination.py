from multiple_soft_elimination import MultipleSoftElimination
from constants import dna_alphabet
from constants import infinity
from Tests.test_utils import check_elimination

class SimpleCost:
    def __init__(self, seq, substitution_cost = 1):
        self.seq = seq
        self.substitution_cost = substitution_cost
    def get(self, index, letter):
        """
        1-based index
        :param index:
        :param letter:
        :return:
        """
        if self.seq[index-1] != letter:
            return self.substitution_cost
        return 0
    def get_cost_of_seq(self, seq):
        assert len(seq) == len(self.seq)
        res_cost = 0
        for i in range(0,len(seq)):
            res_cost += self.get(i+1, seq[i])
        return res_cost


class TestMultipleSoftElimination:
    def test_multiple_soft_elimination_simple_overlap(self):
        seq = "aacaaccaaaaaaccaacca"
        patterns = ["aacca"]
        cost = SimpleCost(seq)
        alg = MultipleSoftElimination(sequence=seq, patterns=patterns, cost=cost, alphabet=dna_alphabet)
        res = alg.eliminate()
        assert check_elimination(res, patterns), "result sequence should not contain any p match"
        assert cost.get_cost_of_seq(res) == 2, "result sequence cost should be equal to 2"


    def test_multiple_soft_elimination_two_patterns(self):
        seq = "aacaaccaaaaaaccaacca"
        patterns = ["caa", "aa"]
        cost = SimpleCost(seq)
        alg = MultipleSoftElimination(sequence=seq, patterns=patterns, cost=cost, alphabet=dna_alphabet)
        res = alg.eliminate()
        assert check_elimination(res, patterns), "result sequence should not contain any p match"
        assert cost.get_cost_of_seq(res) == 6, "result sequence cost should be equal to 6"

    def test_multiple_soft_elimination_not_feasible(self):
        seq = "aaa"
        patterns = ["a"]
        cost = SimpleCost(seq, infinity)
        alg = MultipleSoftElimination(sequence=seq, patterns=patterns, cost=cost, alphabet=dna_alphabet)
        res = alg.eliminate()
        assert res is None, "elimination should not be feasible"
