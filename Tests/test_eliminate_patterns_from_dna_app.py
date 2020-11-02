from Tests import test_utils
from eliminate_patterns_from_dna_app import app
from sequence_reader import SequenceReader

class TestEliminatePatternsFromDnaApp:
    def test_simple(self):
        seq_path = test_utils.get_test_resource_path("test_seq_1.txt")
        patterns_path = test_utils.get_test_resource_path("test_patterns_1.txt")
        result_seq, result_cost = app(["-s", seq_path,"-p", patterns_path])
        assert result_seq is not None, "elimination should be feasible"
        assert 6 == result_cost, "cost of elimination is 6"
        assert test_utils.check_elimination(result_seq, ["caa", "aa"])

    def test_args(self):
        #TODO - test app with invalid args
        pass