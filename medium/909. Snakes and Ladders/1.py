"""
    n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.
n <= 20이라서 비트연산으로 방문체크.
해당 셀 방문했는데 이미 더 낮은 방문횟수로 방문한 적 있으면 해당 상태 버림.
arr[vis]: vis상태일 때 방문횟수
어떻게 풀 것인가: 각 상태일 때 6가지 경우의 수 따져보기
사용 알고리즘: bfs -> 이러면 그냥 vis[i][j]만 해줘도 될듯
"""
from typing import List
from collections import deque
class Solution:
    def converToAxis(self, pos, sz):
        x = (pos - 1) // sz
        y = 0

        if x % 2 == 0:
            y = (pos - 1) % sz
        else:
            y = (sz - 1) - (pos - sz * x - 1)
        
        return x, y

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        n = len(board)
        q = deque()
        vis = [False for _ in range(n*n + 1)]
        vis[1] = True
        q.append((1, 0)) # cur, cnts
        ans = float('inf')

        while q:
            curPos, curCnts = q.popleft()
            print(curPos, curCnts)
            if curPos == n**2:
                ans = min(ans, curCnts)
                continue
            
            curX, curY = self.converToAxis(curPos, n)
            if board[curX][curY] != -1 and not vis[board[curX][curY]]:
                vis[board[curX][curY]] = True
                q.append((board[curX][curY], curCnts + 1))

            for nextPos in range(curPos + 1, min(curPos + 6, n**2) + 1):
                if vis[nextPos]:
                    continue

                vis[nextPos] = True

                # 넘겼으면 답
                if nextPos >= n**2:
                    ans = min(ans, curCnts + 1)
                    continue

                # 안 넘겼을 때,
                nextX, nextY = self.converToAxis(nextPos, n)

                # 아무것도 없으면 그냥 가기
                if board[nextX][nextY] == -1:
                    q.append((nextPos, curCnts + 1))
                
                # 사디리거나 뱀이면 타기
                else:
                    newNextPos = board[nextX][nextY]
                    vis[newNextPos] = True

                    # n**2이면 답으로 갱신
                    if newNextPos == n**2:
                        ans = min(ans, curCnts + 1) 
                        continue

                    # 그 외의 경우 넣기
                    q.append((newNextPos, curCnts + 1))

        if ans == float('inf'):
            return -1
        return ans
    
board = [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]]
sol = Solution()
ans = sol.snakesAndLadders(board)

print(ans)



        
        
        