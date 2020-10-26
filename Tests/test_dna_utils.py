from dna_utils import *

class TestDnaUtils:
    def test_extend_ambiguous_dna(self):
        ambiguous_dna = "auk"
        res = extend_ambiguous_dna(ambiguous_dna)
        assert len(res) == 2
        assert "atg" in res
        assert "att" in res

    def test_is_purine(self):
        assert is_purine("a")
        assert is_purine("g")
        assert not(is_purine("c"))
        assert not (is_purine("t"))

    def test_is_pyrimidine(self):
        assert is_pyrimidine("c")
        assert is_pyrimidine("t")
        assert not (is_pyrimidine("a"))
        assert not (is_pyrimidine("g"))

    def test_is_transition(self):
        assert is_transition("a","g")
        assert is_transition("g","a")
        assert is_transition("c","t")
        assert is_transition("t","c")
        assert not(is_transition("a", "c"))
        assert not(is_transition("c", "a"))
        assert not(is_transition("t", "a"))
        assert not(is_transition("t", "g"))
