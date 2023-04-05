import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        summation = 0
        result = 0

        for i, num in enumerate(nums):
            summation += num
            result = max(result, math.ceil(summation / (i + 1)))

        return result
