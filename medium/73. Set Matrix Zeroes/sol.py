from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        col_flag = False

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_flag = True
                    if j == 0:
                        col_flag = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 
        
        if row_flag == 0:
            for i in range(m):
                matrix[0][i] = 0
        if col_flag == 0:
            for i in range(n):
                matrix[i][0] = 0