from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = self.find_rotation_pivot(nums)
        if k != -1:
            nums = nums[k + 1:] + nums[:k + 1]
        position = self.binary_search(nums, target)

        return (position + k + 1) % len(nums) if position != -1 else -1

    def find_rotation_pivot(self, nums) -> int:
        start = 0  # inclusive
        end = len(nums)  # exclusive

        while start + 1 < end:
            mid = start + ((end - start) // 2)

            if mid + 1 >= end:
                return -1

            if nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[end - 1]:
                start = mid + 1
                continue

            end = mid

        if start + 1 == end:
            if start + 1 >= end:
                return -1

            if nums[start] > nums[start + 1]:
                return start

        return -1

    def binary_search(self, nums, target) -> int:
        start = 0  # inclusive
        end = len(nums)  # exclusive

        while start + 1 < end:
            mid = start + ((end - start) // 2)

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
                continue

            end = mid

        if start + 1 == end and nums[start] == target:
            return start

        return -1


print(Solution().search([6, 7, 8, 9, 10, 11, 13, 15, 0, 1, 2, 3, 5], 8))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(Solution().search(nums=[1], target=0))
print(Solution().search([1, 3], 0))
