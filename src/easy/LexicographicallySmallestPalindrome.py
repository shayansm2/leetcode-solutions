class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        length = len(s)
        mid = length // 2

        for i in range(mid):
            j = length - 1 - i
            if s[i] == s[j]:
                continue

            if ord(s[i]) < ord(s[j]):
                s[j] = s[i]
            else:
                s[i] = s[j]

        return "".join(s)


print(Solution().makeSmallestPalindrome("escape"))
