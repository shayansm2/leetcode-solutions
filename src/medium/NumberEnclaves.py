class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.visited_areas = dict()
        number_of_lands = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    continue

                if self.is_visited(i, j):
                    continue

                queue = [[i, j]]
                is_closed_land = True
                land_counter = 0

                while queue:
                    row, column = queue.pop(0)

                    if self.is_visited(row, column):
                        continue

                    land_counter += 1
                    self.visited_areas[self.get_area_key(row, column)] = True

                    is_closed_land = is_closed_land and self.is_closed_area(row, column)

                    queue += self.get_neighbours(row, column)

                if is_closed_land:
                    # print(i,j)
                    number_of_lands += land_counter

        return number_of_lands

    @staticmethod
    def get_area_key(i, j) -> str:
        return str(i) + '-' + str(j)

    def is_visited(self, i: int, j: int):
        return self.get_area_key(i, j) in self.visited_areas

    def is_closed_area(self, row: int, column: int):
        if row == 0 or column == 0:
            return False

        if row == len(self.grid) - 1 or column == len(self.grid[0]) - 1:
            return False

        return True

    def get_neighbours(self, row: int, column: int) -> list:
        neighbours = []

        if row > 0 and self.grid[row - 1][column] == 1 and not self.is_visited(row - 1, column):
            neighbours.append([row - 1, column])

        if column > 0 and self.grid[row][column - 1] == 1 and not self.is_visited(row, column - 1):
            neighbours.append([row, column - 1])

        if row < len(self.grid) - 1 and self.grid[row + 1][column] == 1 and not self.is_visited(row + 1, column):
            neighbours.append([row + 1, column])

        if column < len(self.grid[0]) - 1 and self.grid[row][column + 1] == 1 and not self.is_visited(row, column + 1):
            neighbours.append([row, column + 1])

        return neighbours
