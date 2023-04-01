class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        intersect = set(nums1).intersection(set(nums2))

        if len(intersect) > 0:
            return min(intersect)

        min1 = min(nums1)
        min2 = min(nums2)

        return min(min1, min2) * 10 + max(min1, min2)