from KMP import KmpUpdateFunction
from string_utils import get_proper_prefixes_of_list


class TestKMP:

    def test_kmp_simple_update(self):
        patterns = ["aca", "ac", "aga", "att"]
        for alg_option in [True,False]:
            print("kmp uses trie optimization: " + str(alg_option))
            kmp = KmpUpdateFunction(patterns, use_kmp_trie=alg_option)
            assert kmp.update("ag", "a") == "" , "creates a pattern"
            assert kmp.update("a", "g") == "ag"
            assert kmp.update("a", "c") == "" , "creates a pattern"
            assert kmp.update("a", "t") == "at"

    def test_kmp_get_sources(self):
        patterns = ["aca", "ac", "aga", "att"]
        for alg_option in [True,False]:
            print("kmp uses trie optimization: " + str(alg_option))
            kmp = KmpUpdateFunction(patterns, use_kmp_trie=alg_option)
            expected_sources = {'': [('', 'c'), ('', 'g'), ('', 't'), ('ag', 'c'), ('ag', 'g'), ('ag', 't'), ('at', 'c'), ('at', 'g')], 'a': [('', 'a'), ('a', 'a'), ('at', 'a')], 'ag': [('a', 'g')], 'at': [('a', 't')]}
            for valid_pref in get_proper_prefixes_of_list(patterns):
                actual_sources = kmp.get_source_set(valid_pref)
                assert len(expected_sources[valid_pref]) == len(actual_sources), "check actual sources length for " + valid_pref
                for pair in expected_sources[valid_pref]:
                    assert pair in actual_sources, "check actual sources item"

