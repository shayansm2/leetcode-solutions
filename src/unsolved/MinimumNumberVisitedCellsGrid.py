import heapq


class Solution:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.dictionary = dict()

    def minimumVisitedCells(self, grid: list[list[int]]) -> int:
        self.add_to_priority_queue((0, 0), 1)
        visited_distance = dict()

        while not self.is_priority_queue_empty():
            node, distance = self.pop_from_priority_queue()
            visited_distance[node] = distance
            row, col = node

            # print(distance)

            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return distance

            for i in range(1, grid[row][col] + 1):
                if row + i < len(grid):
                    if (row + i, col) not in visited_distance or visited_distance[(row + i, col)] > distance + 1:
                        self.add_to_priority_queue((row + i, col), distance + 1)
                if col + i < len(grid[0]):
                    if (row, col + i) not in visited_distance or visited_distance[(row, col + i)] > distance + 1:
                        self.add_to_priority_queue((row, col + i), distance + 1)

        return -1

    def add_to_priority_queue(self, item, value):
        heapq.heappush(self.heap, value)
        if value in self.dictionary:
            self.dictionary[value].append(item)
        else:
            self.dictionary[value] = [item]

    def pop_from_priority_queue(self):
        min_element = heapq.heappop(self.heap)
        return self.dictionary[min_element].pop(0), min_element

    def is_priority_queue_empty(self):
        return len(self.heap) == 0


grid = [
    [13, 14, 1, 17, 8, 6, 17, 0, 15, 11, 14, 3, 16, 7, 10, 7, 12, 2, 12, 6, 2, 5, 9, 3, 2, 7, 1, 10, 1, 10, 7, 2, 0, 12,
     11, 2, 4, 8, 11, 12, 11, 13, 8, 7, 12, 9, 10, 7, 8, 9, 11, 12, 6, 7],
    [13, 12, 11, 16, 3, 8, 15, 6, 10, 16, 6, 2, 6, 14, 13, 14, 9, 16, 2, 6, 7, 9, 6, 2, 11, 13, 2, 5, 2, 14, 9, 2, 7,
     10, 14, 9, 7, 0, 5, 1, 8, 2, 7, 4, 12, 4, 11, 0, 5, 7, 0, 6, 6, 3],
    [17, 0, 14, 17, 8, 17, 6, 6, 1, 7, 1, 8, 3, 8, 4, 3, 1, 4, 5, 3, 12, 5, 4, 13, 11, 3, 0, 6, 4, 9, 8, 9, 13, 11, 0,
     7, 4, 1, 5, 1, 11, 3, 9, 4, 4, 12, 3, 2, 7, 7, 9, 10, 8, 5],
    [2, 13, 5, 13, 13, 4, 11, 11, 11, 6, 9, 4, 7, 13, 9, 14, 7, 7, 6, 12, 5, 15, 4, 5, 10, 1, 10, 4, 7, 14, 8, 5, 7, 12,
     13, 2, 10, 5, 3, 12, 9, 9, 5, 8, 5, 9, 12, 8, 11, 5, 4, 0, 0, 0],
    [1, 4, 7, 3, 2, 10, 7, 17, 5, 16, 2, 4, 2, 9, 10, 12, 5, 1, 15, 4, 12, 1, 14, 3, 1, 14, 1, 13, 3, 4, 2, 13, 11, 11,
     1, 10, 3, 5, 10, 10, 0, 11, 8, 10, 12, 10, 4, 2, 2, 4, 1, 3, 2, 8],
    [13, 7, 6, 5, 1, 5, 3, 11, 13, 3, 9, 7, 7, 7, 3, 2, 12, 14, 11, 5, 2, 15, 9, 1, 6, 12, 1, 13, 7, 13, 9, 6, 11, 13,
     12, 3, 4, 2, 12, 4, 4, 4, 6, 8, 8, 1, 12, 6, 7, 4, 7, 5, 11, 11],
    [13, 2, 17, 14, 8, 3, 16, 16, 3, 11, 14, 13, 7, 14, 11, 2, 10, 8, 11, 10, 15, 7, 6, 12, 11, 6, 7, 12, 8, 9, 13, 5,
     11, 13, 0, 6, 13, 6, 4, 10, 11, 11, 6, 11, 10, 10, 8, 3, 10, 11, 4, 11, 5, 11],
    [2, 8, 6, 3, 8, 7, 14, 16, 14, 13, 6, 4, 9, 2, 15, 9, 9, 7, 1, 11, 0, 7, 6, 2, 6, 14, 8, 14, 7, 8, 1, 5, 9, 4, 4, 2,
     9, 11, 5, 6, 2, 5, 12, 12, 8, 8, 11, 7, 10, 4, 8, 4, 10, 1],
    [6, 3, 9, 7, 4, 9, 13, 0, 15, 4, 1, 7, 3, 9, 4, 0, 0, 13, 0, 7, 5, 8, 6, 12, 9, 7, 14, 10, 6, 5, 8, 10, 3, 8, 9, 3,
     9, 6, 0, 6, 2, 4, 8, 4, 1, 7, 2, 9, 7, 11, 6, 0, 8, 2],
    [15, 11, 4, 10, 9, 15, 14, 13, 9, 0, 7, 6, 10, 0, 11, 1, 12, 4, 8, 10, 4, 14, 6, 14, 13, 5, 11, 9, 13, 1, 6, 2, 6,
     11, 5, 6, 2, 1, 6, 11, 11, 6, 11, 10, 0, 3, 10, 7, 1, 3, 6, 7, 2, 0],
    [11, 5, 4, 16, 13, 15, 6, 3, 15, 8, 4, 3, 9, 6, 2, 3, 6, 7, 10, 11, 14, 0, 4, 3, 12, 4, 7, 8, 0, 1, 4, 11, 0, 9, 10,
     2, 8, 5, 6, 10, 12, 0, 10, 11, 11, 2, 3, 9, 2, 10, 10, 2, 5, 3],
    [12, 11, 7, 5, 3, 13, 15, 6, 16, 6, 0, 10, 2, 15, 13, 5, 5, 9, 6, 4, 1, 0, 4, 12, 13, 3, 4, 6, 10, 3, 2, 12, 11, 9,
     3, 9, 0, 12, 1, 8, 6, 8, 7, 11, 10, 8, 1, 2, 9, 1, 1, 7, 10, 1],
    [12, 6, 1, 7, 12, 11, 6, 9, 8, 2, 2, 2, 5, 7, 10, 3, 12, 3, 4, 6, 2, 6, 14, 10, 13, 3, 5, 10, 6, 4, 12, 13, 11, 6,
     3, 9, 4, 0, 0, 12, 1, 2, 9, 10, 10, 11, 5, 8, 4, 5, 2, 10, 8, 6],
    [14, 9, 3, 11, 13, 14, 14, 0, 11, 11, 15, 9, 3, 10, 0, 8, 8, 8, 14, 7, 4, 0, 0, 12, 8, 3, 13, 0, 6, 5, 13, 7, 6, 12,
     6, 5, 10, 1, 1, 0, 10, 4, 10, 9, 1, 4, 2, 9, 10, 6, 6, 4, 9, 10],
    [11, 0, 10, 15, 6, 10, 5, 15, 2, 15, 13, 13, 7, 3, 9, 11, 1, 2, 14, 13, 7, 11, 6, 12, 3, 6, 4, 12, 10, 11, 8, 9, 3,
     2, 1, 9, 8, 6, 10, 6, 5, 2, 8, 6, 10, 0, 3, 7, 3, 5, 4, 4, 0, 0],
    [6, 15, 14, 13, 4, 4, 8, 6, 8, 12, 0, 4, 3, 14, 10, 10, 3, 11, 8, 6, 5, 5, 8, 10, 2, 13, 9, 1, 13, 11, 7, 5, 0, 6,
     1, 3, 1, 9, 3, 11, 4, 4, 2, 6, 4, 1, 10, 9, 10, 7, 10, 6, 6, 9],
    [10, 10, 4, 2, 5, 15, 14, 0, 9, 6, 13, 15, 10, 0, 8, 11, 1, 9, 5, 13, 12, 13, 6, 11, 9, 8, 7, 7, 12, 12, 7, 2, 0, 1,
     0, 5, 11, 8, 11, 0, 7, 11, 3, 8, 3, 10, 8, 6, 4, 5, 4, 1, 0, 7],
    [16, 7, 5, 11, 9, 13, 7, 1, 14, 1, 15, 14, 11, 12, 10, 13, 8, 10, 3, 2, 5, 4, 12, 5, 13, 11, 1, 6, 2, 0, 10, 2, 5,
     10, 3, 3, 8, 4, 4, 6, 8, 9, 5, 7, 3, 6, 3, 1, 9, 1, 8, 5, 8, 7],
    [2, 9, 13, 5, 7, 7, 3, 9, 8, 10, 0, 1, 8, 4, 11, 12, 14, 13, 2, 12, 7, 6, 7, 13, 7, 13, 12, 5, 12, 8, 8, 2, 2, 9, 6,
     5, 3, 2, 11, 2, 7, 6, 5, 6, 8, 3, 9, 3, 8, 3, 2, 1, 1, 3],
    [14, 4, 6, 9, 10, 7, 3, 12, 7, 0, 13, 14, 14, 14, 13, 9, 8, 12, 3, 11, 4, 6, 8, 5, 7, 10, 0, 4, 8, 6, 12, 7, 10, 4,
     9, 11, 2, 7, 6, 10, 5, 1, 9, 1, 7, 9, 6, 4, 10, 9, 6, 6, 1, 1],
    [10, 14, 12, 10, 14, 7, 15, 4, 9, 13, 12, 10, 12, 2, 1, 10, 4, 5, 5, 2, 0, 13, 2, 4, 10, 9, 4, 10, 7, 11, 11, 7, 0,
     9, 5, 3, 2, 8, 2, 7, 7, 5, 2, 4, 7, 10, 8, 0, 1, 6, 7, 0, 9, 7],
    [1, 6, 12, 3, 7, 6, 15, 7, 2, 11, 12, 11, 11, 2, 2, 2, 11, 9, 8, 11, 6, 0, 2, 1, 8, 10, 11, 6, 2, 7, 1, 4, 7, 11, 5,
     10, 1, 2, 6, 9, 6, 1, 9, 4, 1, 6, 9, 9, 2, 7, 2, 2, 7, 3],
    [4, 7, 6, 5, 14, 8, 6, 4, 11, 14, 7, 1, 13, 10, 11, 7, 12, 11, 6, 2, 2, 7, 8, 6, 7, 11, 11, 10, 3, 1, 6, 5, 2, 9, 1,
     8, 11, 6, 1, 4, 9, 2, 2, 9, 5, 5, 9, 9, 3, 8, 9, 9, 6, 6],
    [10, 5, 7, 9, 12, 0, 13, 2, 3, 10, 7, 1, 10, 7, 7, 13, 8, 11, 1, 2, 12, 0, 0, 1, 1, 12, 4, 1, 5, 8, 10, 2, 6, 8, 11,
     4, 7, 2, 10, 9, 4, 1, 10, 10, 7, 4, 7, 9, 7, 9, 0, 0, 1, 0],
    [13, 14, 15, 6, 7, 4, 4, 9, 1, 6, 0, 9, 2, 5, 13, 0, 10, 11, 8, 1, 3, 8, 7, 11, 11, 12, 3, 9, 2, 11, 0, 11, 9, 10,
     4, 1, 5, 4, 1, 6, 0, 5, 7, 1, 3, 7, 2, 7, 5, 0, 1, 6, 6, 3],
    [7, 0, 10, 12, 2, 7, 9, 6, 14, 5, 2, 4, 2, 3, 10, 11, 1, 7, 9, 8, 10, 2, 7, 0, 12, 12, 4, 4, 3, 0, 10, 6, 6, 5, 2,
     9, 8, 7, 0, 9, 3, 7, 8, 3, 5, 1, 2, 2, 8, 5, 4, 1, 2, 5],
    [14, 0, 2, 11, 10, 13, 3, 7, 6, 5, 1, 6, 9, 0, 1, 6, 7, 3, 8, 4, 12, 8, 12, 8, 3, 7, 9, 9, 2, 0, 4, 7, 3, 3, 7, 5,
     2, 10, 4, 6, 1, 7, 1, 6, 2, 8, 4, 8, 3, 5, 6, 1, 2, 3],
    [5, 2, 2, 5, 1, 0, 2, 14, 6, 9, 6, 2, 13, 13, 1, 13, 12, 5, 10, 8, 6, 12, 4, 6, 2, 9, 11, 0, 11, 0, 6, 9, 5, 8, 5,
     5, 8, 7, 10, 9, 7, 1, 0, 5, 7, 2, 7, 5, 5, 4, 0, 2, 4, 0],
    [10, 11, 10, 1, 2, 0, 7, 12, 1, 5, 11, 0, 7, 7, 2, 1, 0, 2, 6, 3, 4, 6, 1, 7, 2, 6, 10, 4, 4, 8, 0, 4, 9, 3, 0, 10,
     1, 10, 3, 5, 8, 7, 4, 4, 7, 4, 5, 1, 4, 5, 4, 4, 5, 2],
    [0, 11, 10, 13, 4, 3, 12, 6, 4, 5, 2, 1, 3, 9, 8, 12, 10, 1, 11, 11, 11, 5, 11, 7, 5, 1, 2, 5, 7, 3, 8, 10, 0, 7, 6,
     5, 5, 4, 10, 5, 7, 8, 0, 0, 2, 9, 0, 1, 2, 2, 0, 5, 6, 5],
    [13, 6, 3, 6, 8, 5, 2, 0, 6, 1, 11, 13, 10, 13, 11, 9, 0, 3, 0, 1, 3, 1, 7, 6, 4, 6, 0, 8, 2, 5, 4, 5, 4, 4, 5, 1,
     2, 4, 9, 7, 4, 9, 1, 4, 3, 6, 8, 0, 6, 7, 1, 2, 3, 1],
    [0, 5, 8, 1, 10, 0, 6, 8, 3, 12, 11, 0, 7, 4, 5, 8, 11, 5, 10, 9, 6, 2, 9, 0, 9, 0, 1, 3, 9, 5, 9, 7, 2, 8, 3, 0, 1,
     3, 7, 4, 3, 3, 3, 1, 4, 3, 6, 0, 1, 3, 5, 1, 3, 6],
    [11, 14, 7, 11, 8, 2, 5, 12, 13, 10, 7, 5, 12, 6, 5, 0, 9, 11, 5, 7, 9, 0, 2, 9, 11, 7, 4, 5, 0, 0, 7, 8, 2, 10, 2,
     4, 8, 7, 1, 8, 8, 7, 8, 3, 6, 4, 7, 3, 2, 6, 0, 3, 0, 6],
    [1, 11, 3, 8, 9, 13, 6, 13, 0, 3, 5, 6, 6, 10, 4, 10, 2, 10, 2, 10, 11, 10, 1, 3, 1, 10, 6, 0, 5, 1, 2, 5, 0, 5, 10,
     9, 1, 5, 9, 2, 6, 7, 5, 3, 2, 2, 4, 1, 8, 4, 6, 7, 6, 5],
    [3, 10, 7, 11, 1, 7, 8, 12, 2, 0, 1, 1, 11, 5, 8, 3, 0, 9, 1, 9, 5, 8, 6, 10, 7, 3, 5, 8, 5, 9, 8, 0, 9, 5, 8, 7, 7,
     2, 7, 7, 0, 6, 6, 8, 3, 2, 8, 1, 5, 8, 0, 7, 5, 2],
    [8, 3, 10, 5, 6, 13, 6, 12, 2, 8, 7, 7, 10, 9, 10, 6, 2, 4, 2, 5, 11, 4, 0, 2, 10, 6, 7, 10, 6, 2, 0, 7, 5, 8, 4, 5,
     0, 1, 8, 5, 1, 1, 5, 2, 5, 3, 4, 6, 6, 0, 6, 3, 0, 3],
    [13, 2, 6, 5, 2, 13, 13, 13, 11, 0, 3, 12, 3, 9, 3, 5, 2, 4, 0, 4, 4, 8, 4, 0, 9, 1, 4, 3, 6, 9, 1, 8, 6, 3, 4, 2,
     4, 4, 0, 1, 7, 2, 1, 5, 8, 2, 4, 6, 0, 3, 1, 2, 4, 0],
    [1, 9, 3, 7, 8, 11, 3, 6, 1, 5, 4, 8, 8, 9, 6, 5, 8, 0, 9, 11, 2, 11, 1, 4, 0, 0, 4, 10, 8, 0, 10, 9, 2, 1, 7, 9, 9,
     8, 1, 7, 4, 6, 3, 5, 5, 2, 6, 1, 3, 1, 4, 1, 6, 7],
    [6, 11, 1, 11, 2, 7, 0, 0, 2, 9, 3, 7, 3, 6, 6, 11, 10, 4, 10, 7, 11, 10, 4, 1, 7, 4, 8, 6, 7, 1, 1, 7, 1, 1, 3, 4,
     5, 6, 2, 8, 8, 4, 6, 3, 7, 1, 1, 4, 2, 2, 4, 6, 2, 2],
    [7, 8, 12, 5, 2, 9, 6, 5, 12, 6, 2, 6, 2, 5, 5, 7, 10, 0, 0, 6, 4, 6, 0, 10, 9, 3, 7, 2, 8, 4, 6, 6, 6, 0, 1, 6, 5,
     7, 3, 0, 4, 0, 5, 8, 6, 0, 6, 2, 6, 1, 0, 5, 2, 6],
    [1, 9, 12, 0, 7, 2, 7, 9, 5, 11, 12, 0, 4, 10, 8, 9, 1, 11, 10, 3, 6, 3, 6, 6, 9, 1, 2, 4, 6, 5, 1, 9, 0, 7, 7, 2,
     0, 4, 0, 2, 2, 5, 2, 3, 7, 0, 0, 6, 2, 1, 5, 4, 0, 2],
    [12, 5, 2, 10, 0, 12, 4, 5, 1, 12, 12, 10, 5, 10, 4, 6, 8, 0, 6, 7, 10, 6, 6, 8, 4, 7, 1, 2, 4, 7, 6, 6, 2, 9, 1, 2,
     0, 6, 5, 0, 2, 1, 0, 0, 4, 6, 0, 7, 2, 3, 6, 3, 5, 5],
    [12, 8, 11, 6, 6, 10, 8, 0, 4, 2, 7, 10, 11, 3, 3, 8, 4, 9, 1, 7, 9, 1, 4, 9, 2, 5, 1, 8, 5, 6, 1, 2, 3, 1, 1, 0, 1,
     6, 8, 0, 4, 2, 4, 6, 7, 5, 4, 7, 7, 7, 3, 5, 4, 5],
    [10, 2, 11, 9, 1, 0, 4, 9, 9, 4, 4, 1, 10, 2, 5, 3, 9, 4, 7, 7, 8, 0, 6, 7, 0, 7, 0, 0, 9, 8, 7, 0, 6, 1, 5, 5, 1,
     3, 6, 0, 2, 1, 2, 7, 6, 6, 3, 4, 2, 4, 3, 5, 3, 0],
    [9, 6, 10, 8, 10, 11, 12, 9, 8, 6, 10, 6, 0, 5, 7, 10, 0, 2, 1, 1, 0, 5, 6, 3, 7, 9, 1, 0, 6, 2, 6, 5, 6, 8, 8, 2,
     2, 8, 3, 3, 5, 7, 4, 5, 7, 5, 1, 2, 1, 4, 0, 6, 4, 5],
    [11, 9, 6, 9, 11, 7, 7, 2, 8, 8, 4, 7, 8, 8, 4, 5, 8, 8, 5, 3, 10, 10, 2, 1, 2, 2, 9, 5, 1, 6, 5, 5, 1, 5, 6, 8, 6,
     3, 4, 6, 1, 3, 4, 3, 6, 5, 6, 1, 6, 5, 2, 6, 1, 4],
    [3, 5, 11, 0, 1, 4, 0, 1, 11, 8, 11, 2, 9, 2, 7, 5, 1, 1, 9, 2, 1, 9, 1, 7, 8, 3, 5, 9, 0, 3, 7, 0, 6, 0, 7, 1, 6,
     6, 5, 3, 7, 3, 4, 6, 2, 7, 5, 4, 6, 3, 5, 3, 4, 6],
    [4, 6, 1, 7, 4, 2, 4, 7, 8, 5, 2, 9, 3, 9, 1, 6, 3, 1, 6, 6, 7, 1, 8, 1, 7, 8, 4, 4, 8, 0, 1, 2, 2, 3, 0, 5, 6, 3,
     5, 3, 5, 5, 6, 3, 2, 0, 3, 1, 1, 1, 2, 0, 5, 4],
    [0, 8, 11, 7, 5, 6, 1, 2, 7, 1, 9, 5, 2, 4, 3, 4, 4, 5, 7, 10, 4, 7, 5, 0, 3, 6, 1, 0, 5, 8, 5, 0, 7, 2, 6, 7, 4, 6,
     6, 2, 2, 7, 3, 0, 3, 2, 6, 4, 1, 1, 0, 3, 4, 1],
    [10, 10, 6, 9, 4, 1, 1, 6, 3, 7, 1, 10, 5, 7, 8, 0, 5, 4, 7, 3, 8, 3, 8, 1, 8, 6, 5, 7, 0, 1, 3, 5, 6, 6, 7, 4, 5,
     7, 2, 2, 7, 5, 1, 3, 3, 4, 6, 0, 3, 5, 4, 1, 5, 3],
    [1, 5, 2, 7, 6, 2, 1, 2, 3, 2, 10, 8, 10, 10, 0, 1, 10, 10, 9, 5, 4, 8, 0, 1, 0, 4, 6, 4, 3, 2, 2, 7, 1, 3, 2, 0, 7,
     1, 4, 5, 7, 4, 4, 1, 0, 1, 2, 1, 0, 2, 3, 1, 1, 5],
    [2, 0, 0, 9, 6, 3, 10, 5, 4, 6, 8, 6, 6, 7, 10, 0, 7, 2, 3, 9, 4, 8, 9, 3, 3, 1, 0, 3, 4, 6, 2, 0, 8, 5, 7, 3, 1, 5,
     6, 5, 5, 4, 6, 6, 6, 0, 3, 0, 1, 2, 2, 2, 1, 3],
    [6, 7, 10, 7, 2, 5, 8, 3, 6, 8, 8, 3, 4, 4, 5, 8, 1, 8, 8, 8, 4, 8, 8, 8, 5, 7, 2, 5, 3, 1, 6, 6, 6, 2, 7, 6, 6, 3,
     5, 3, 6, 6, 2, 4, 0, 1, 4, 2, 3, 4, 3, 4, 0, 5],
    [8, 11, 7, 10, 5, 10, 5, 4, 9, 9, 6, 6, 4, 6, 10, 4, 6, 4, 5, 8, 9, 8, 7, 4, 7, 5, 0, 1, 7, 0, 4, 7, 3, 0, 3, 4, 4,
     3, 2, 1, 5, 4, 4, 2, 2, 1, 0, 5, 3, 1, 1, 3, 5, 3],
    [4, 8, 5, 11, 8, 10, 9, 1, 5, 10, 4, 3, 8, 1, 4, 9, 5, 5, 9, 1, 2, 7, 8, 5, 1, 7, 8, 3, 2, 4, 7, 0, 4, 6, 7, 3, 1,
     7, 2, 6, 1, 1, 1, 2, 1, 5, 2, 4, 3, 5, 1, 4, 4, 0],
    [9, 10, 3, 0, 7, 0, 8, 2, 7, 9, 8, 5, 3, 0, 8, 7, 7, 9, 8, 0, 2, 3, 2, 6, 6, 7, 0, 5, 3, 7, 6, 4, 2, 7, 4, 0, 7, 4,
     1, 0, 6, 1, 2, 4, 3, 3, 2, 1, 5, 3, 5, 3, 2, 1],
    [9, 4, 0, 6, 5, 6, 6, 10, 9, 3, 6, 1, 3, 2, 1, 8, 0, 0, 7, 7, 4, 0, 5, 0, 3, 2, 5, 1, 0, 5, 1, 2, 0, 1, 4, 0, 2, 5,
     3, 1, 1, 3, 2, 1, 4, 1, 3, 3, 3, 2, 0, 3, 4, 3],
    [5, 10, 10, 10, 9, 7, 1, 2, 9, 3, 0, 6, 4, 5, 7, 1, 8, 3, 2, 4, 8, 6, 6, 0, 4, 1, 5, 3, 7, 2, 5, 4, 3, 2, 5, 1, 4,
     0, 0, 4, 6, 2, 6, 5, 5, 3, 5, 0, 0, 3, 3, 4, 1, 2],
    [2, 0, 6, 2, 6, 2, 2, 4, 8, 10, 1, 2, 5, 0, 2, 3, 6, 4, 6, 4, 3, 4, 5, 2, 2, 2, 6, 6, 1, 1, 0, 7, 1, 6, 1, 1, 4, 2,
     4, 6, 5, 3, 3, 0, 4, 1, 0, 1, 1, 1, 1, 0, 1, 3],
    [11, 4, 3, 7, 1, 8, 6, 2, 8, 5, 1, 3, 0, 0, 1, 9, 7, 5, 2, 7, 8, 6, 2, 1, 2, 4, 2, 0, 5, 6, 6, 0, 4, 2, 0, 1, 2, 5,
     1, 1, 3, 3, 0, 2, 1, 2, 3, 1, 0, 3, 2, 0, 4, 0],
    [5, 5, 5, 2, 8, 1, 10, 4, 8, 0, 9, 0, 9, 6, 2, 1, 0, 0, 6, 6, 8, 8, 8, 0, 0, 4, 4, 0, 5, 2, 7, 2, 5, 3, 2, 1, 2, 3,
     4, 5, 1, 5, 4, 2, 5, 4, 1, 2, 3, 4, 1, 4, 1, 1],
    [5, 7, 1, 4, 7, 2, 9, 9, 1, 9, 3, 4, 1, 6, 4, 5, 8, 5, 2, 1, 3, 8, 2, 1, 5, 6, 1, 0, 1, 4, 1, 1, 3, 2, 6, 3, 6, 4,
     2, 1, 3, 4, 4, 5, 1, 5, 5, 1, 1, 2, 3, 2, 1, 4],
    [2, 8, 8, 1, 7, 9, 3, 0, 9, 7, 3, 2, 4, 9, 6, 4, 2, 4, 8, 6, 8, 2, 2, 1, 2, 0, 6, 7, 3, 1, 1, 3, 6, 6, 3, 4, 2, 5,
     1, 2, 1, 0, 2, 2, 5, 1, 4, 4, 0, 3, 2, 4, 2, 0],
    [3, 5, 7, 1, 1, 8, 9, 2, 7, 7, 0, 4, 1, 7, 1, 5, 2, 5, 3, 1, 0, 6, 1, 1, 1, 4, 6, 7, 3, 6, 6, 3, 0, 2, 4, 1, 4, 5,
     5, 5, 4, 2, 3, 2, 0, 4, 2, 1, 0, 4, 0, 4, 1, 1],
    [7, 6, 3, 10, 0, 8, 6, 4, 4, 8, 1, 1, 3, 8, 2, 8, 5, 5, 8, 1, 2, 2, 5, 7, 2, 0, 5, 7, 0, 4, 2, 0, 5, 6, 5, 3, 0, 0,
     4, 3, 2, 2, 2, 5, 3, 0, 1, 4, 3, 2, 3, 4, 2, 0],
    [3, 3, 8, 6, 9, 1, 1, 4, 4, 3, 2, 8, 8, 1, 3, 8, 4, 6, 1, 0, 3, 2, 2, 4, 1, 5, 6, 4, 1, 6, 5, 3, 5, 6, 0, 0, 0, 4,
     3, 4, 1, 3, 1, 0, 4, 4, 2, 1, 4, 0, 1, 3, 0, 2],
    [2, 5, 1, 2, 9, 2, 8, 9, 4, 2, 3, 0, 1, 3, 5, 5, 0, 0, 5, 7, 1, 5, 2, 6, 5, 3, 5, 5, 6, 3, 0, 0, 4, 6, 4, 4, 3, 1,
     4, 4, 4, 5, 4, 2, 1, 4, 0, 4, 3, 2, 1, 0, 1, 2],
    [1, 1, 7, 7, 9, 6, 2, 5, 5, 7, 7, 8, 7, 8, 6, 6, 1, 6, 3, 3, 6, 1, 3, 7, 5, 0, 1, 0, 4, 1, 2, 6, 2, 5, 4, 0, 4, 4,
     5, 3, 3, 2, 3, 4, 0, 3, 2, 3, 2, 3, 1, 3, 0, 1],
    [6, 8, 0, 5, 5, 8, 0, 7, 5, 3, 5, 1, 8, 3, 7, 1, 7, 5, 4, 3, 7, 7, 6, 0, 0, 3, 0, 1, 3, 2, 5, 2, 0, 2, 2, 5, 4, 1,
     3, 1, 1, 2, 3, 4, 0, 3, 3, 2, 2, 3, 0, 3, 1, 1],
    [5, 4, 2, 6, 0, 8, 8, 5, 1, 7, 1, 4, 2, 2, 7, 4, 2, 4, 4, 5, 3, 4, 4, 4, 0, 5, 5, 4, 4, 6, 1, 5, 1, 4, 5, 3, 5, 1,
     3, 1, 0, 2, 1, 0, 4, 4, 0, 1, 2, 3, 3, 1, 1, 0],
    [2, 9, 6, 0, 0, 6, 2, 8, 1, 0, 3, 6, 7, 3, 6, 1, 3, 6, 6, 1, 0, 0, 6, 3, 4, 5, 6, 1, 1, 1, 4, 1, 2, 1, 5, 0, 1, 1,
     1, 1, 4, 2, 0, 4, 0, 3, 1, 3, 3, 3, 1, 3, 1, 1],
    [6, 2, 6, 0, 0, 4, 7, 2, 5, 1, 8, 4, 7, 0, 7, 3, 7, 3, 3, 0, 2, 6, 0, 1, 6, 6, 2, 1, 1, 5, 2, 1, 4, 2, 4, 4, 0, 0,
     0, 0, 2, 3, 2, 0, 3, 1, 2, 0, 3, 2, 0, 2, 1, 2],
    [9, 7, 4, 1, 0, 8, 7, 7, 2, 0, 1, 5, 0, 5, 7, 1, 1, 6, 5, 2, 4, 0, 0, 2, 4, 1, 0, 2, 0, 1, 3, 4, 4, 1, 0, 3, 3, 3,
     2, 3, 1, 1, 0, 4, 3, 3, 0, 2, 1, 1, 2, 3, 2, 2],
    [9, 7, 7, 1, 1, 1, 8, 7, 2, 3, 5, 0, 1, 7, 5, 5, 0, 1, 2, 1, 0, 2, 3, 2, 3, 5, 4, 0, 1, 3, 0, 1, 3, 5, 1, 2, 0, 2,
     2, 1, 4, 1, 0, 1, 3, 1, 1, 1, 0, 2, 3, 0, 1, 0],
    [1, 9, 6, 5, 1, 6, 7, 4, 8, 4, 4, 2, 5, 3, 7, 6, 0, 2, 0, 5, 3, 5, 1, 4, 1, 2, 2, 2, 1, 4, 3, 3, 5, 0, 0, 4, 3, 2,
     3, 2, 3, 1, 1, 3, 0, 0, 2, 0, 3, 3, 0, 2, 0, 1],
    [6, 1, 5, 0, 5, 0, 1, 8, 6, 7, 7, 3, 1, 5, 6, 2, 2, 4, 6, 2, 3, 4, 6, 1, 6, 4, 3, 3, 2, 1, 5, 3, 1, 1, 0, 2, 3, 3,
     0, 1, 4, 0, 3, 2, 1, 2, 2, 1, 1, 2, 1, 0, 1, 2],
    [2, 6, 3, 5, 2, 3, 2, 0, 1, 0, 3, 6, 0, 2, 7, 7, 1, 0, 4, 5, 1, 5, 4, 6, 4, 4, 5, 5, 2, 1, 5, 4, 1, 3, 3, 3, 1, 3,
     2, 2, 0, 0, 3, 0, 3, 1, 3, 0, 0, 2, 0, 1, 1, 0],
    [3, 4, 5, 4, 0, 2, 4, 2, 2, 5, 5, 5, 6, 6, 0, 5, 3, 6, 4, 5, 3, 1, 0, 5, 2, 0, 2, 2, 4, 3, 1, 1, 3, 1, 3, 1, 4, 1,
     2, 3, 1, 3, 3, 1, 3, 1, 3, 1, 1, 2, 2, 1, 0, 2],
    [8, 3, 6, 0, 3, 0, 4, 0, 4, 6, 1, 4, 6, 4, 2, 0, 2, 4, 6, 4, 6, 6, 1, 5, 4, 4, 0, 1, 0, 2, 2, 1, 2, 4, 4, 4, 0, 4,
     2, 0, 3, 1, 1, 2, 3, 2, 2, 1, 2, 1, 2, 2, 0, 2],
    [8, 1, 0, 0, 4, 6, 1, 3, 2, 0, 7, 7, 5, 1, 4, 1, 1, 3, 6, 4, 0, 3, 0, 1, 3, 4, 4, 2, 0, 1, 1, 3, 4, 4, 0, 4, 0, 2,
     3, 3, 2, 1, 3, 1, 2, 2, 2, 0, 0, 2, 2, 1, 0, 0],
    [6, 0, 0, 7, 0, 1, 2, 1, 1, 3, 3, 6, 4, 5, 5, 2, 2, 0, 2, 0, 1, 4, 3, 3, 1, 5, 3, 3, 2, 4, 4, 2, 1, 3, 0, 1, 1, 2,
     1, 1, 1, 1, 3, 3, 1, 0, 2, 0, 1, 1, 2, 1, 0, 1],
    [0, 3, 8, 0, 5, 7, 2, 6, 7, 3, 1, 1, 1, 4, 1, 3, 6, 2, 3, 1, 2, 1, 5, 1, 3, 2, 1, 0, 1, 1, 0, 3, 2, 3, 4, 1, 3, 3,
     1, 1, 1, 3, 0, 1, 0, 2, 2, 2, 0, 1, 0, 2, 2, 0],
    [8, 6, 7, 2, 5, 5, 2, 4, 3, 7, 5, 5, 4, 5, 5, 0, 3, 3, 5, 3, 1, 5, 3, 0, 3, 3, 1, 3, 3, 2, 2, 1, 3, 4, 0, 1, 3, 2,
     3, 1, 2, 2, 2, 0, 2, 0, 2, 0, 1, 2, 0, 2, 0, 0],
    [1, 6, 7, 5, 6, 5, 1, 1, 6, 1, 5, 0, 0, 2, 1, 2, 2, 1, 2, 3, 4, 0, 0, 4, 0, 3, 4, 1, 3, 0, 4, 3, 2, 3, 2, 0, 0, 1,
     3, 0, 1, 0, 2, 0, 2, 1, 1, 0, 0, 2, 2, 2, 0, 2],
    [6, 1, 1, 6, 1, 6, 4, 5, 6, 4, 4, 3, 2, 0, 5, 1, 3, 2, 2, 2, 5, 3, 2, 0, 4, 0, 1, 1, 2, 3, 0, 2, 1, 2, 1, 3, 0, 3,
     1, 1, 2, 1, 1, 0, 2, 0, 1, 2, 2, 2, 1, 2, 1, 2],
    [6, 6, 5, 6, 2, 6, 6, 6, 5, 6, 4, 1, 0, 2, 2, 1, 5, 2, 5, 5, 1, 4, 1, 1, 4, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 2, 3, 2,
     2, 1, 2, 2, 0, 2, 1, 1, 1, 1, 2, 0, 2, 2, 1, 2],
    [5, 6, 1, 2, 5, 4, 2, 4, 2, 0, 0, 5, 6, 3, 2, 0, 3, 4, 5, 4, 3, 1, 0, 3, 0, 3, 0, 2, 0, 0, 2, 1, 1, 2, 3, 1, 3, 3,
     2, 0, 1, 1, 2, 0, 2, 0, 1, 0, 2, 2, 1, 2, 2, 2],
    [4, 5, 5, 6, 5, 2, 3, 1, 1, 5, 4, 4, 5, 5, 3, 4, 4, 1, 0, 4, 1, 0, 0, 2, 1, 0, 1, 4, 4, 0, 0, 1, 3, 0, 2, 0, 0, 1,
     2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 1, 1, 0, 0, 1, 2],
    [4, 7, 5, 6, 2, 0, 3, 1, 2, 6, 2, 2, 2, 5, 1, 4, 3, 2, 0, 2, 1, 3, 3, 1, 0, 1, 4, 4, 1, 3, 3, 3, 1, 3, 3, 2, 0, 1,
     0, 2, 2, 2, 0, 2, 2, 2, 1, 0, 1, 1, 2, 0, 2, 0],
    [4, 2, 2, 6, 0, 6, 3, 1, 6, 5, 3, 0, 5, 5, 4, 0, 2, 1, 2, 3, 1, 1, 4, 3, 0, 4, 2, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1,
     1, 2, 0, 1, 2, 2, 2, 0, 1, 0, 1, 2, 2, 0, 1, 1],
    [6, 2, 0, 6, 1, 3, 0, 6, 2, 6, 3, 4, 3, 0, 2, 4, 2, 5, 0, 1, 4, 0, 2, 0, 3, 1, 0, 3, 3, 2, 2, 2, 3, 2, 2, 0, 0, 2,
     2, 2, 2, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 0],
    [1, 5, 1, 1, 6, 1, 5, 3, 5, 4, 2, 1, 3, 4, 5, 1, 2, 3, 4, 2, 4, 2, 0, 0, 2, 1, 0, 2, 0, 2, 1, 3, 3, 1, 2, 2, 2, 2,
     2, 1, 2, 0, 0, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 0],
    [0, 3, 4, 1, 0, 6, 6, 3, 3, 0, 5, 5, 5, 4, 5, 1, 0, 4, 2, 1, 2, 3, 4, 3, 2, 2, 0, 0, 1, 0, 0, 0, 1, 1, 2, 2, 2, 2,
     2, 1, 0, 1, 0, 2, 1, 0, 0, 2, 1, 2, 2, 1, 1, 2],
    [5, 0, 6, 6, 2, 4, 1, 1, 0, 1, 5, 2, 3, 4, 3, 0, 2, 3, 3, 3, 1, 4, 1, 3, 3, 0, 2, 0, 0, 2, 2, 1, 2, 0, 0, 0, 2, 2,
     2, 1, 0, 0, 1, 0, 1, 1, 2, 2, 0, 1, 0, 2, 1, 1],
    [3, 1, 5, 0, 1, 6, 0, 2, 2, 5, 5, 1, 2, 5, 0, 1, 1, 0, 2, 1, 3, 3, 3, 0, 0, 0, 1, 3, 2, 0, 2, 0, 1, 2, 1, 2, 1, 0,
     1, 0, 2, 2, 0, 1, 2, 1, 0, 2, 1, 0, 0, 0, 0, 0]]

print(Solution().minimumVisitedCells(grid))
