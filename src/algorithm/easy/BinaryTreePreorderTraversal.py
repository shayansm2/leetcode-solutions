from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        queue = [root]

        while queue:
            node = queue.pop()
            ans.append(node.val)

            if node.right:
                queue.append(node.right)

            if node.left:
                queue.append(node.left)

        return ans
