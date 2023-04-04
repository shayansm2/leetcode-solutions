class Solution:
    def partitionString(self, s: str) -> int:
        chars = dict()
        counter = 1
        for char in s:
            if char in chars:
                counter += 1
                chars = dict()
            chars[char] = 1

        return counter
