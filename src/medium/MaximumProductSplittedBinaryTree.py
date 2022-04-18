from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.leafSums = []
        self.modulo = 10 ** 9 + 7

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        rootSum = self.calculateLeafSum(root)

        bestNodeSum = 0
        minDifference = rootSum

        for i in self.leafSums:
            diff = abs((rootSum / 2) - i)
            if minDifference > diff:
                minDifference = diff
                bestNodeSum = i

        return ((bestNodeSum % self.modulo) * ((rootSum - bestNodeSum) % self.modulo)) % self.modulo

    def calculateLeafSum(self, root: TreeNode):
        leftSum = 0
        if root.left:
            leftSum = self.calculateLeafSum(root.left)

        rightSum = 0
        if root.right:
            rightSum = self.calculateLeafSum(root.right)

        nodeSum = root.val + leftSum + rightSum
        self.leafSums.append(nodeSum)
        return nodeSum


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
print(Solution().maxProduct(root))

root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), TreeNode(6))))
print(Solution().maxProduct(root))
