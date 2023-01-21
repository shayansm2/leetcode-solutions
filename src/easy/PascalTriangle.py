from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1 for i in range(numRows)]]

        for i in range(1, numRows):
            row = [1]
            
            for j in range(1, numRows - i):
                row.append(row[j-1] + pascals[i-1][j])
            
            pascals.append(row)
        
        output = []
        
        for i in range(1, numRows+1):
            row = []
            for j in range(i):
                row.append(pascals[j][i-j-1])
            output.append(row)
        
        return output
