class Solution:
    def __init__(self):
        self.mapping = dict()

    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        for i, char in enumerate(chars):
            self.mapping[char] = vals[i]

        nums = [self._get_cost(char) for char in s]

        # based on MaximumSubarray:
        last_max_sum = 0
        max_sum = last_max_sum

        for i in range(len(nums)):
            if last_max_sum < 0:
                last_max_sum = nums[i]
            else:
                last_max_sum += nums[i]

            max_sum = max(max_sum, last_max_sum)

        return max_sum

    def _get_cost(self, char: str):
        if char in self.mapping:
            return self.mapping[char]

        return ord(char) - ord('a') + 1
