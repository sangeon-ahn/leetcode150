from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])

        q = deque()
        visited = set()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    ans += 1
                    visited.add((i, j))
                    q.append((i, j))
                    
                    while q:
                        curX, curY = q.popleft()

                        for k in range(4):
                            nx, ny = curX + dx[k], curY + dy[k]

                            if nx < 0 or nx >= n or ny < 0 or ny >= m: 
                                continue

                            if (nx, ny) in visited:
                                continue

                            if grid[nx][ny] == "1":
                                visited.add((nx, ny))
                                q.append((nx, ny))
        
        return ans

                                


grid = [["1","0"]]
sol = Solution()
ans = sol.numIslands(grid)
print(ans)

        