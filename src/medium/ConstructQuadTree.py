# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        if self.is_leaf(grid):
            return Node(grid[0][0], True, None, None, None, None)

        sub_matrices = self.get_sub_matrices(grid)

        return Node(
            grid[0][0],
            False,
            self.construct(sub_matrices['topLeft']),
            self.construct(sub_matrices['topRight']),
            self.construct(sub_matrices['bottomLeft']),
            self.construct(sub_matrices['bottomRight'])
        )

    def is_leaf(self, grid: list[list[int]]):
        for row in grid:
            for val in row:
                if val != grid[0][0]:
                    return False
        return True

    def get_sub_matrices(self, grid: list[list[int]]):
        top_left = []
        top_right = []
        bottom_left = []
        bottom_right = []

        length = len(grid)

        for i in range(length):
            right_row = []
            left_row = []

            for j in range(length):
                if j >= length / 2:
                    right_row.append(grid[i][j])
                else:
                    left_row.append(grid[i][j])

            if i >= length / 2:
                bottom_right.append(right_row)
                bottom_left.append(left_row)
            else:
                top_right.append(right_row)
                top_left.append(left_row)

        return {
            'topLeft': top_left,
            'topRight': top_right,
            'bottomLeft': bottom_left,
            'bottomRight': bottom_right,
        }


print(Solution().construct([[0, 1], [1, 0]]))
print(Solution().construct(
    [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]))
