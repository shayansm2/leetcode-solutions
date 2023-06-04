class Solution:
    def minimizedStringLength(self, s: str) -> int:
        mapping = {}
        for char in s:
            mapping[char] = True
        return len(mapping.keys())
