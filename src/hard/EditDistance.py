from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.number_of_calls = 0
        result = self.get_levenshtein_edit_distance(word1, word2)
        print(self.number_of_calls)
        return result

    @lru_cache()
    def get_levenshtein_edit_distance(self, first: str, second: str) -> int:
        self.number_of_calls += 1

        if len(first) == 0:
            return len(second)

        if len(second) == 0:
            return len(first)

        prefix_word1 = first[:-1]
        prefix_word2 = second[:-1]

        return min(
            self.get_levenshtein_edit_distance(prefix_word1, second) + 1,  # delete
            self.get_levenshtein_edit_distance(first, prefix_word2) + 1,  # add
            self.get_levenshtein_edit_distance(prefix_word1, prefix_word2) + (first[-1] != second[-1])  # replace
        )


print(Solution().minDistance('horse', 'ros'))
print(Solution().minDistance('intention', 'execution'))
word1 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef'
word2 = 'bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg'
print(Solution().minDistance(word1, word2))
