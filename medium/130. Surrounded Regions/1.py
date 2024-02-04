"""
    격자를 2차원 for문 순회하면서 O 찾으면 bfs 하면서 주위가 하나도 경계에 없으면 flip
"""
from typing import List  
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        q = deque()

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' or visited[i][j]:
                    continue

                q.append((i, j))
                visited[i][j] = True
                flag = False
                poses = set()
                poses.add((i, j))

                while q:
                    curX, curY = q.popleft()

                    for k in range(4):
                        nx = curX + dx[k]
                        ny = curY + dy[k]

                        # cur에서 벽면과 맏닿아 있으면 flip 불가
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            flag = True
                            continue

                        if board[nx][ny] == 'X':
                            continue

                        if visited[nx][ny]:
                            continue

                        poses.add((nx, ny))
                        visited[nx][ny] = True
                        q.append((nx, ny))
                
                if not flag:
                    for pos in poses:
                        board[pos[0]][pos[1]] = 'X'

        
                
board = [["X"]]
sol = Solution()
ans = sol.solve(board)


                

        