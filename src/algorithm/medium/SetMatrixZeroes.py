from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroColumns = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    zeroRows.add(row)
                    zeroColumns.add(column)

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row in zeroRows:
                    matrix[row][column] = 0
                elif column in zeroColumns:
                    matrix[row][column] = 0
