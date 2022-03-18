from typing import Optional


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


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class PathSum:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        nodesStack = [root]
        pathSums = [0]

        while nodesStack:
            node = nodesStack.pop()
            nodeSum = pathSums.pop() + node.val

            if nodeSum == targetSum and not node.left and not node.right:
                return True

            if node.left:
                nodesStack.append(node.left)
                pathSums.append(nodeSum)

            if node.right:
                nodesStack.append(node.right)
                pathSums.append(nodeSum)

        return False


testCases = [
    {
        'input': {
            'root': '[5,4,8,11,null,13,4,7,2,null,null,null,1]',
            'targetSum': 22
        },
        'output': True
    },
    {
        'input': {
            'root': '[1,2,3]',
            'targetSum': 5
        },
        'output': False
    },
    {
        'input': {
            'root': '[1,2]',
            'targetSum': 0
        },
        'output': False
    },
    # {
    #     'input': {
    #         'root':'[]',
    #         'targetSum': 1
    #     },
    #     'output': False
    # },
    {
        'input': {
            'root': '[1,2]',
            'targetSum': 1
        },
        'output': False
    },
]

if __name__ == '__main__':
    #     drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    #     drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    for test in testCases:
        root = deserialize(test['input']['root'])
        targetSum = test['input']['targetSum']
        expectedOutput = test['output']

        output = (PathSum()).hasPathSum(root, targetSum)

        if output == expectedOutput:
            print('TEST WEND OKAY')
        else:
            print(test['input']['root'], targetSum, expectedOutput, output)
