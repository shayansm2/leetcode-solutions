from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = [root]
        levels = [1]
        rightSide = {1: root.val}

        while queue:
            node = queue.pop(0)
            currentLevel = levels.pop(0)
            # print('DEBUG level of', node.val, 'is', currentLevel)

            if currentLevel not in rightSide.keys():
                rightSide[currentLevel] = node.val

            if node.right:
                # print('DEBUG right of ', node.val, 'is' , node.right.val)
                queue.append(node.right)
                levels.append(currentLevel + 1)

            if node.left:
                # print('DEBUG left of ', node.val, 'is' , node.left.val)
                queue.append(node.left)
                levels.append(currentLevel + 1)

        # print('DEBUG', rightSide)
        return list(rightSide.values())


testCases = [
    {
        'input': '[1,2,3,null,5,null,4]',
        'output': [1, 3, 4]
    },
    {
        'input': '[1,null,3]',
        'output': [1, 3]
    }
]

for testCase in testCases:
    input = deserialize(testCase['input'])
    expectedOutput = testCase['output']
    output = Solution().rightSideView(input)

    if output == expectedOutput:
        print('TEST WENT FINE')
    else:
        print(testCase['input'], expectedOutput, output)
