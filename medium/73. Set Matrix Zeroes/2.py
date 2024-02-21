from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for r in rows:
            for i in range(m):
                matrix[r][i] = 0
        
        for c in cols:
            for i in range(n):
                matrix[i][c] = 0
