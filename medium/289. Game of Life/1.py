"""
    1. 문제 분석
        n * m 격자: 1=live, 0=dead
        이웃=8개
        이웃 룰
        1. live 셀은 이웃이 x<2 면 dead
        2. live 셀은 이웃이 2<= x <=3 이면 다음 세대에도 live
        3. live 셀은 이웃이 3<x 면 dead
        4. dead 셀은 이웃이 3개 있으면 live 셀 됨
        
        live와 dead는 동시에 일어남(모든 셀 평가한 후 동시에 전부 반영됨)
    
    
    2. 풀이 방법
        0으로 되어야 할 셀=-1
        1로 되어야 할 셀=2

        전부 진행한 후,
        다시 돌면서 바꿔주기

"""
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        for i in range(n):
            for j in range(m):
                # 1이 3개면
                cnts = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue

                    if board[nx][ny] == 1 or board[nx][ny] == -1:
                        cnts += 1
                
                if board[i][j] == 0 and cnts == 3:
                    board[i][j] = 2
                
                elif board[i][j] == 1:
                    if cnts < 2 or 3 < cnts:
                        board[i][j] = -1
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol = Solution()
ans = sol.gameOfLife(board)
                        
                        
                    
