from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        multiplies = []
        multiply = 1

        for i in nums:
            multiply *= i
            multiplies.append(multiply)

        count = 0
        startIndex = endIndex = 0
        while endIndex < len(nums):
            while multiplies[endIndex] // (multiplies[startIndex - 1] if startIndex > 0 else 1) >= k:
                if startIndex >= endIndex:
                    break
                startIndex += 1

            print(startIndex, endIndex)
            count += (endIndex - startIndex + 1)
            endIndex += 1

        return count


print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
print(Solution().numSubarrayProductLessThanK(nums=[1, 2, 3], k=3))
