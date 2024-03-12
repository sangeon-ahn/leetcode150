from typing import List
from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        if len(word) > n * m:
            return False
        
        # 보드 내의 모든 알파벳 다 배열에 저장
        cnts = Counter(sum(board, []))

        for c, cnt in Counter(word).items():
            if cnts[c] < cnt:
                return False
        
        # 단어 맨 앞 알파벳이 맨 뒤알파벳보다 많으면 단어 뒤집기
        if cnts[word[0]] > cnts[word[-1]]:
            word = word[::-1]
        
        seen = set()

        def dfs(r, c, cnt):
            if cnt == len(word):
                return True
            
            if r < 0 or c < 0 or r >= n or c >= m or word[cnt] != board[r][c] or (r, c) in seen:
                return False
            
            seen.add((r, c))
            res = (
                dfs(r + 1, c, cnt + 1) or
                dfs(r, c + 1, cnt + 1) or
                dfs(r - 1, c, cnt + 1) or
                dfs(r, c - 1, cnt + 1)
            )
            seen.remove((r, c))

            return res

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

sol = Solution()
ans = sol.exist(board, word)
print(ans)