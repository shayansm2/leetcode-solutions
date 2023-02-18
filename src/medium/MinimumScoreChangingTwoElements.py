class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums = sorted(nums)

        return min(
            nums[-3] - nums[0],
            nums[-2] - nums[1],
            nums[-1] - nums[2]
        )