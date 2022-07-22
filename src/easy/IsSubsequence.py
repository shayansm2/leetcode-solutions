class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        sIndex = 0

        for tIndex in range(len(t)):
            if s[sIndex] == t[tIndex]:
                sIndex += 1

            if sIndex == len(s):
                return True

        return False