class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        n_rows = len(grid)
        n_columns = len(grid[0])

        for i in range(n_rows):
            for j in range(n_columns):
                if '1' == grid[i][j]:
                    grid = self.perform_bfs(grid, (i, j))
                    counter += 1

        return counter


    def perform_bfs(self, grid: List[List[str]], location):
        queue = [location]

        while queue:
            loc = queue.pop()
            i = loc[0]
            j = loc[1]

            grid[i][j] = '0'

            if i > 0 and grid[i-1][j] == '1':
                queue.append((i-1, j))

            if j > 0 and grid[i][j-1] == '1':
                queue.append((i, j-1))

            if i < len(grid)-1 and grid[i+1][j] == '1':
                queue.append((i+1, j))

            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                queue.append((i, j+1))

        return grid

