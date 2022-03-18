class Solution:
    def validPalindrome(self, s: str) -> bool:
        arr = list(s)

        return self.checkIfPalindrome(arr, True)

    def checkIfPalindrome(self, arr: list, can_delete: bool) -> bool:
        # print(arr)
        startIndex = 0
        endIndex = len(arr) - 1

        while startIndex <= endIndex:
            if arr[startIndex] == arr[endIndex]:
                startIndex += 1
                endIndex -= 1
                continue
            else:
                if not can_delete:
                    return False

                # print(startIndex, endIndex)
                if self.checkIfPalindrome(arr[startIndex + 1: endIndex + 1], False):
                    return True
                return self.checkIfPalindrome(arr[startIndex: endIndex], False)

        return True


s = Solution()
print(s.validPalindrome("abc"))

print(s.validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
