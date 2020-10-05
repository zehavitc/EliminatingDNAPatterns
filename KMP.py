import StringUtils


class KmpUpdateFunction:
    debug = True
    def __init__(self, patterns, alphabet = ['a', 'c', 't', 'g'], validPrefixes = None, allowFullMatch = False):
        """

        :param patterns:
        :param allowFullMatch:
        """
        self._alphabet = alphabet
        self._patterns = patterns
        self._allowFullMatch = allowFullMatch
        if validPrefixes is None:
            self._prefixes = set()
            for p in patterns:
                self._prefixes = self._prefixes.union(StringUtils.get_all_proper_prefixes(p))
                self._prefixes = self._prefixes.union(patterns)
        else:
            self._prefixes = validPrefixes
        self._calc_update_function_table()


    # def calc_f_table(self, pattern, suffix_pattern):
    #     """
    #
    #     :param pattern: The pattern that we read
    #     :param suffix_pattern: The pattern that the longest suffix refers to
    #     :return:
    #     """
    #     i = 1
    #     longest_prefix_len = 0
    #     k = len(pattern)
    #     f = [0 for i in range(0,k)]
    #     while i < len(pattern):
    #         if pattern[i] == suffix_pattern[longest_prefix_len]:
    #             f[i] = longest_prefix_len + 1
    #             i = i + 1
    #             longest_prefix_len = longest_prefix_len + 1
    #         elif longest_prefix_len > 0:
    #             longest_prefix_len = f[longest_prefix_len - 1]
    #         else:
    #             i = i + 1
    #     return f

    def _kmp(self, sequence):
        res = ""
        res_len = 0
        for prefix in self._prefixes:
            prefix_len = len(prefix)
            if sequence.endswith(prefix) and prefix_len > res_len:
                res = prefix
                res_len = prefix_len

        return res

    def _calc_update_function_table(self):
        """

        :return:
        """
        self._update_function_table = {prefix:{sigma:"" for sigma in self._alphabet} for prefix in self._prefixes}
        self._sources_set = {prefix:[] for prefix in self._prefixes}
        for prefix in self._prefixes:
            for sigma in self._alphabet:
                new_seq_suffix = prefix + sigma
                if not self._allowFullMatch and any(new_seq_suffix.endswith(p) for p in self._patterns):
                    if self.debug:
                        print("state is not allowed: " + prefix + "+" + sigma)
                    continue #this extension creates a p match and therefore is not allowed
                kmp_val = self._kmp(new_seq_suffix)
                self._update_function_table[prefix][sigma] = kmp_val
                self._sources_set[kmp_val].append((prefix, sigma))
        if self.debug:
            print("sources:" + str(self._sources_set))


    def update(self, prefix, sigma):
        """

        :param sequence:
        :return:
        """
        return self._update_function_table[prefix][sigma]

    def get_source_set(self, prefix):
        return self._sources_set[prefix]

