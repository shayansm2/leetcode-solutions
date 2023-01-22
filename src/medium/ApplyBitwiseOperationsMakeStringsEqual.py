class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True

        zeroToOnes = 0
        oneToZeros = 0
        for i in range(len(s)):
            if s[i] == target[i] == '1':
                return True

            elif s[i] == '0' and target[i] == '1':
                zeroToOnes += 1

            elif s[i] == '1' and target[i] == '0':
                oneToZeros += 1

        if not oneToZeros:
            return False

        if not zeroToOnes:
            return False

        return True
