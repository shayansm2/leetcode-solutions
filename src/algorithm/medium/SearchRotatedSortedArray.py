from typing import List


class Solution:
    def __init__(self):
        self.target = None
        self.nums = None

    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.binary_search(0, len(nums) - 1, False)

    def binary_search(self, start: int, end: int, is_sorted: bool) -> int:
        if end < start:
            return -1

        mid = start + (end - start) // 2
        # print(self.nums[start:end + 1], self.nums[mid], self.target, is_sorted)

        if self.nums[mid] == self.target:
            return mid

        if is_sorted:
            if self.nums[mid] > self.target:
                return self.binary_search(start, mid - 1, True)

            return self.binary_search(mid + 1, end, True)

        if self.nums[start] <= self.target <= self.nums[mid]:
            return self.binary_search(start, mid - 1, True)

        if self.nums[mid] <= self.target <= self.nums[end]:
            return self.binary_search(mid + 1, end, True)

        if self.nums[start] <= self.nums[mid]:
            return self.binary_search(mid + 1, end, False)

        return self.binary_search(start, mid - 1, False)


print(Solution().search([6, 7, 8, 9, 10, 11, 13, 15, 0, 1, 2, 3, 5], 8))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(Solution().search(nums=[1], target=0))
print(Solution().search([1, 3], 0))
