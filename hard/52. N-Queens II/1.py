class Solution:
    def totalNQueens(self, n: int) -> int:
        horizon = [False for _ in range(n)]
        vertical = [False for _ in range(n)] 
        diagonal1 = [False for _ in range(2*n)]
        diagonal2 = [False for _ in range(2*n)]

        ans = 0

        def recur(order):
            nonlocal ans
            if order == n:
                ans += 1
                return
            
            for i in range(n): # 수직 검사
                if not horizon[i] and not vertical[order] and not diagonal1[order - i] and not diagonal2[order + i]:
                    horizon[i] = True
                    vertical[order] = True
                    diagonal1[order - i] = True
                    diagonal2[order + i] = True
                    recur(order + 1)
                    horizon[i] = False
                    vertical[order] = False
                    diagonal1[order - i] = False
                    diagonal2[order + i] = False

        recur(0)
        print(ans)
        return ans

sol = Solution()
ans = sol.totalNQueens(7)
                    