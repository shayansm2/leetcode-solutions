# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        if root is None:
            return []

        queue = [root]
        paths = [[str(root.val)]]

        counter = dict()
        subtree_map = dict()

        while queue:
            node = queue.pop()
            node_path = paths.pop()
            is_leaf = True

            if node.left:
                queue.append(node.left)
                paths.append(node_path + [str(node.left.val)])
                is_leaf = False

            if node.right:
                queue.append(node.right)
                paths.append(node_path + [str(node.right.val)])
                is_leaf = False

            if is_leaf:
                for i in range(len(node_path)):
                    key = '-'.join(node_path[i:])
                    if key in counter.keys():
                        counter[key] += 1
                    else:
                        counter[key] = 1

        print(counter)
