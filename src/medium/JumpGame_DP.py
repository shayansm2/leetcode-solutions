from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJumps = [nums[0]]

        for i in range(1, len(nums)):
            if maxJumps[i - 1] < i:
                return False

            maxJumps.append(max(maxJumps[i - 1], i + nums[i]))

            if maxJumps[i] >= n:
                return True

        return maxJumps[-1] >= n - 1