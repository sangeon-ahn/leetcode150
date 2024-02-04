from collections import deque
from typing import List
class Solution:
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    def solve(self, board: List[List[str]]) -> None:
        def markUncaptured(x, y):
            q = deque((x, y))
            while q:
                curX, curY = q.popleft()

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if board[x][y] == 'X' or board[x][y] == 'U':
                    continue

                board[x][y] = 'U'
                for d in self.dir:
                    q.append((curX + d[0], curY + d[1]))
        
        n, m = len(board), len(board[0])

        for i in range(n):
            if board[i][0] == 'O':
                markUncaptured(i, 0)
            if board[i][m - 1] == 'O':
                markUncaptured(i, m - 1)
        
        for i in range(m):
            if board[0][i] == 'O':
                markUncaptured(0, i)
            if board[n - 1][i] == 'O':
                markUncaptured(n - 1, i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'
                


