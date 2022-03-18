from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            sortedWord = self.getSortedWord(word)
            if sortedWord in groups.keys():
                groups[sortedWord].append(word)
            else:
                groups[sortedWord] = [word]

        return list(groups.values())

    def getSortedWord(self, word: str) -> str:  # O(nlogn)
        return ''.join(sorted(word))


print(Solution().groupAnagrams([""]))
