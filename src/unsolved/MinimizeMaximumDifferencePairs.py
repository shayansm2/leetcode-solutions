class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums = sorted(nums)

        diffs = []

        for i in range(len(nums) - 1):
            diffs.append(nums[i + 1] - nums[i])

        diffs = sorted(diffs)

        return diffs[p - 1]
