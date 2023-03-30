from functools import lru_cache


class Solution:
    @lru_cache()
    def isScramble(self, s1: str, s2: str) -> bool:
        print(s1, s2)
        if s1 == s2:
            return True

        if len(s1) != len(s2):
            return False

        length = len(s1)

        if length < 2:
            return False

        s1hm = dict()
        s2hm = dict()
        s2hmr = dict()

        straight_potential_pivots = []
        reversed_potential_pivots = []

        for i in range(length):
            if s1[i] in s1hm:
                s1hm[s1[i]] += 1
            else:
                s1hm[s1[i]] = 1

            if s2[i] in s2hm:
                s2hm[s2[i]] += 1
            else:
                s2hm[s2[i]] = 1

            if s2[-i - 1] in s2hmr:
                s2hmr[s2[-i - 1]] += 1
            else:
                s2hmr[s2[-i - 1]] = 1

            if s1hm == s2hm and i < length - 1:
                straight_potential_pivots.append(i)

            if s1hm == s2hmr and i < length - 1:
                reversed_potential_pivots.append(i)

        if s1hm != s2hm:
            return False

        for i in straight_potential_pivots:
            if self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]):
                return True

        for i in reversed_potential_pivots:
            if self.isScramble(s1[:i + 1], s2[-1: -2 - i: -1]) and self.isScramble(s1[i + 1:], s2[-i - 2::-1]):
                return True

        return False


# print(Solution().isScramble('abcdefg', 'acbfgde'))
# print(Solution().isScramble('great', 'rgeat'))
# print(Solution().isScramble('abcde', 'caebd'))
# print(Solution().isScramble('a', 'a'))
print(Solution().isScramble('eebaacbcbcadaaedceaaacadccd', 'eadcaacabaddaceacbceaabeccd'))
