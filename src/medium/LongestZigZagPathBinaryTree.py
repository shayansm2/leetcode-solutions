# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max_length = 0

        self.post_order_traverse(root)

        return self.max_length

    def post_order_traverse(self, node: TreeNode) -> tuple:
        left_length, right_length = 0, 0

        if node.left:
            left_length = self.post_order_traverse(node.left)[1] + 1

        if node.right:
            right_length = self.post_order_traverse(node.right)[0] + 1

        self.max_length = max(self.max_length, left_length, right_length)

        return left_length, right_length
