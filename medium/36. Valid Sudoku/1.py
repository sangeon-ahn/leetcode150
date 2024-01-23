"""
    row, column, 3*3 grid 모두 중복없이 1~9로 채워져야 함.
    0~8까지 colsets, rowsets, gridsets 리스트로 만들어서 사용  
"""
from typing import List
class Solution:
    def getIdx(self, i, j):
        x = i // 3
        y = j // 3

        """
        (0, 0) -> 0
        (0, 1) -> 1
        (0, 2) -> 2
        (1, 0) -> 3
        (1, 1) -> 4
        """
        return 3 * x + y
        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colsets = [set() for _ in range(9)]
        rowsets = [set() for _ in range(9)]
        gridsets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                idx = self.getIdx(i, j)
                if num in colsets[j] or num in rowsets[i] or num in gridsets[idx]:
                    return False

                colsets[j].add(num)
                rowsets[i].add(num)
                gridsets[idx].add(num)
        
        return True


        

        