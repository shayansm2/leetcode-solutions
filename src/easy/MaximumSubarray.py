from typing import List


class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        lastMaxSum = nums[0]
        maxSum = lastMaxSum

        for i in range(1, len(nums)):
            if lastMaxSum < 0:
                lastMaxSum = nums[i]
            else:
                lastMaxSum += nums[i]

            maxSum = max(maxSum, lastMaxSum)

        return maxSum
