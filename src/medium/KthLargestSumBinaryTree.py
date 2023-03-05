# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        queue = [root]
        levels = [0]
        level_sums = dict()

        while queue:
            node = queue.pop()
            level = levels.pop()

            if level in level_sums.keys():
                level_sums[level] += node.val
            else:
                level_sums[level] = node.val

            if node.left:
                queue.append(node.left)
                levels.append(level + 1)

            if node.right:
                queue.append(node.right)
                levels.append(level + 1)

        sums = level_sums.values()

        sums = sorted(sums, reverse=True)

        if len(sums) < k:
            return -1

        return sums[k - 1]
