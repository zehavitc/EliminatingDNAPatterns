from KMP_trie import KMPTrie

class TestKMPTrie:
    def test_kmp_trie(self):
        trie = KMPTrie()
        trie.add_prefix("a")
        trie.add_prefix("b")
        trie.add_prefix("abb")
        assert trie.get_longest_prefix_that_is_a_suffix("d") == "", "longest prefix of d should be the empty string"
        assert trie.get_longest_prefix_that_is_a_suffix("bb") == "b", "longest prefix of bb should be b"
        assert trie.get_longest_prefix_that_is_a_suffix("cabb") == "abb", "longest prefix of cabb should be abb"