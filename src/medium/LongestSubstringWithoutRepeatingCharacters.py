class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        maxLength = 1

        startIndex = 0
        for endIndex in range(1, len(s)):
            lastChar = s[endIndex]

            for i in range(endIndex - 1, startIndex - 1, -1):
                if s[i] == lastChar:
                    startIndex = i + 1
                    break

            length = endIndex - startIndex + 1

            if length > maxLength:
                maxLength = length

        return maxLength


print(Solution().lengthOfLongestSubstring("pwwkew"))
