import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        counter = 0
        last_level = 1
        queue = [root]
        levels = [1]

        while queue:
            node = queue.pop(0)
            level = levels.pop(0)

            counter += 1
            last_level = max(level, last_level)

            if node.left:
                queue.append(node.left)
                levels.append(level + 1)

            if node.right:
                queue.append(node.right)
                levels.append(level + 1)

        print(counter, math.ceil(math.log2(counter + 1)), last_level)
        return math.ceil(math.log2(counter + 1)) == last_level

    def isBalanced2(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = [root]
        levels = [0]
        last_levels = []

        while queue:
            node = queue.pop()
            nodeLevel = levels.pop()

            if node.left:
                queue.append(node.left)
                levels.append(nodeLevel + 1)
            else:
                for i in last_levels:
                    if i > nodeLevel + 1 or i < nodeLevel - 1:
                        return False
                last_levels.append(nodeLevel)

            if node.right:
                queue.append(node.right)
                levels.append(nodeLevel + 1)
            else:
                for i in last_levels:
                    if i > nodeLevel + 1 or i < nodeLevel - 1:
                        return False
                last_levels.append(nodeLevel)

        return True
