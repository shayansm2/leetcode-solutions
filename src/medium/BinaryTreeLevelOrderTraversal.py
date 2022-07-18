
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodesPerLevel = dict()

        if root is None:
            return []

        nodes = [root]
        levels = [0]

        while nodes:
            node = nodes.pop(0)
            level = levels.pop(0)

            try :
                nodesPerLevel[level] += [node.val]
            except:
                nodesPerLevel[level] = [node.val]

            if node.left:
                nodes.append(node.left)
                levels.append(level + 1)

            if node.right:
                nodes.append(node.right)
                levels.append(level+1)

        return nodesPerLevel.values()

