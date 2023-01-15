class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = []
        roadmap = []
        for i in range(n):
            matrix.append([0 for i in range(n)])
            roadmap.append([0 for i in range(n)])

        for query in queries:
            row1, col1, row2, col2 = query

            for i in range(row1, row2 + 1):
                roadmap[i][col1] += 1
                if col2 < n - 1:
                    roadmap[i][col2 + 1] -= 1

        for i in range(n):
            row_value = 0
            for j in range(n):
                row_value += roadmap[i][j]
                matrix[i][j] = row_value

        return matrix