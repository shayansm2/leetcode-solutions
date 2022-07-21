from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.getPathToNode(root, p)
        qPath = self.getPathToNode(root, q)

        for i in range(min(len(pPath), len(qPath)) - 1, -1, -1):
            if pPath[i].val == qPath[i].val:
                return pPath[i]

        return pPath[0]

    def getPathToNode(self, start: 'TreeNode', target: 'TreeNode') -> List:
        path = []

        while start != target:
            path.append(start)

            if start.val > target.val:
                start = start.left
            else:
                start = start.right

        path.append(target)

        return path
