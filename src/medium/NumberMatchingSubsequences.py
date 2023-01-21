from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.letter_index_map = dict()

        for index, letter in enumerate(s):
            try:
                self.letter_index_map[letter].append(index)
            except:
                self.letter_index_map[letter] = [index]

        counter = 0
        for word in words:
            if self.isSubsequent(word):
                counter += 1

        return counter

    def isSubsequent(self, word) -> bool:
        max_index = -1

        for letter in word:
            try:
                indices = self.letter_index_map[letter]
            except:
                return False

            if max_index >= indices[-1]:
                return False

            for index in indices:
                if index > max_index:
                    max_index = index
                    break

        return True