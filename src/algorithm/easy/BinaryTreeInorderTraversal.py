from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = []
        right = []

        if root.left:
            left = self.inorderTraversal(root.left)

        if root.right:
            right = self.inorderTraversal(root.right)

        return left + [root.val] + right


sample = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(Solution().inorderTraversal(sample))
