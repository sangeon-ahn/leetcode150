from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        if len(word) > n * m:
            return False
            
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        def recur(curX, curY, vis, cnts):
            if cnts == len(word):
                return True
            
            for i in range(4):
                nx = curX + dx[i]
                ny = curY + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in vis and board[nx][ny] == word[cnts]:
                    vis.add((nx, ny))
                    if recur(nx, ny, vis, cnts + 1):
                        return True

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and recur(i, j, set([(i, j)]), 1):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

sol = Solution()
ans = sol.exist(board, word)
print(ans)
        
CAA
AAA
BCD
        
        
