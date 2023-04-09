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
