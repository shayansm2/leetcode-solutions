# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        treeDepth = 0
        node = root

        while node:
            node = node.left
            treeDepth += 1

        numberOfNodes = (2**treeDepth) - 1

        stack = [root]
        levels = [1]

        while stack:
            node = stack.pop()
            currentLevel = levels.pop()

            if currentLevel == treeDepth:
                break

            if node.right:
                stack.append(node.left)
                levels.append(currentLevel + 1)

                stack.append(node.right)
                levels.append(currentLevel + 1)
            elif node.left:
                stack.append(node.left)
                levels.append(currentLevel + 1)

                numberOfNodes -= 1
            else:
                numberOfNodes -= 2

        return numberOfNodes