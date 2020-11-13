from cost import Cost
from constants import infinity
class TestCost:

    def test_cost(self):
        seq = "aaAr"
        cost = Cost(sequence=seq, cost_unit=1, transition_transversion_proportion=2)
        assert 0 == cost.get(1, "a"), "cost is 0 for not changing the letter"
        assert 0 == cost.get(4, "a"), "cost is 0 for not changing the letter (r is a or g)"
        assert infinity == cost.get(3, "g"), "index 2 is not allowed to be changed (uppercase)"
        assert 1 == cost.get(1, "g"), "transition cost"
        assert 2 == cost.get(1, "t"), "transversion cost"
        assert 2 == cost.get(1, "c"), "transversion cost"
        assert 2 == cost.get(4, "t"), "transversion cost with IUPAC"