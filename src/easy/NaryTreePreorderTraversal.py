class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        visited = []

        if root is None:
            return visited

        nodes = [root]

        while nodes:
            node = nodes.pop()
            visited.append(node.val)
            nodes += list(reversed(node.children))

        return visited
