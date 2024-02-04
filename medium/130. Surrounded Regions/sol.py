from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(x, y, mark):
            nonlocal board

            # 경계와 맞닿아 있으면 False
            if x < 0 or x >= n or y < 0 or y >= m:
                return False
            
            # X거나 마킹값과 같으면 True
            elif board[x][y] == 'X' or board[x][y] == mark:
                return True
        
            # 그밖에
            else:
                res = True
                board[x][y] = mark
                
                for d in dir:
                    nx = x + d[0]
                    ny = y + d[1]

                    # 상하좌우 4방향에 대해 dfs 수행했을 때 하나라도 결과가 False면 res가 False임
                    # 그래서 만약 res를 and의 left operand로 두었으면 res가 False로 설정된 이후에는 dfs가 호출되지 않게 되면서 격자에 마킹되지 않는 문제 발생 -> res를 right operand로 두어야 함.
                    res = dfs(nx, ny, mark) and res
                
                return res
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        n, m = len(board), len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if dfs(i, j, '1'): # 경계와 맞닿아 있지 않으면,
                        dfs(i, j, 'X') # X로 마킹
        
        # 위 dfs에서 O를 1로 바꿔주다가 첫 dfs 결과가 True면 모두 X로 바꿔주는 코드이기 때문에, 위 dfs 다 끝났을 때 남겨진 1들은 경계를 만난 O군집들이다. 따라서 다시 O로 바꿔준다.
        for i in range(n):
            for j in range(m):
                if board[i][j] == '1':
                    board[i][j] = 'O'

board = [["X","O","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
ans = sol.solve(board)
print(board)