from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2

        left = self.sortedArrayToBST(nums[:mid]) if mid > 0 else None

        right = self.sortedArrayToBST(nums[mid + 1:]) if mid < len(nums) - 1 else None

        return TreeNode(nums[mid], left, right)
