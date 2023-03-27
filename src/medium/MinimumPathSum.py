class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = []

        row_count = len(grid)
        column_count = len(grid[0])

        dp_row = []
        summation = 0
        for column in range(column_count):
            summation += grid[0][column]
            dp_row.append(summation)

        dp.append(dp_row)

        for row in range(1, row_count):
            dp_row = [grid[row][0] + dp[row-1][0]]

            for column in range(1, column_count):
                dp_row.append(min(dp_row[column - 1], dp[row - 1][column]) + grid[row][column])

            dp.append(dp_row)

        print(dp)
        return dp[-1][-1]
