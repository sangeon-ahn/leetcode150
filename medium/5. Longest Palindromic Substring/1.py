"""
    문자열 s가 팰린드롬이기 위해서는 s[1:-1]이 팰린드롬이어야 한다.
    dp[i][j]: s[i:j+1]이 팰린드롬이면 True, 아니면 False
    for i in
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        st = 0
        en = 0

        for i in range(1, n): # i = 0, 1, 2, 3, 4,
            for j in range(n - i): # n-i = 5, 4, 3, 2, 1
                x = j
                y = i + j
                
                # 팰린드롬 체크
    
                if y - x == 1:
                    dp[x][y] = s[x] == s[y]
                else:
                    dp[x][y] = dp[x + 1][y - 1] and s[x] == s[y]
                
                if dp[x][y] and en - st < y - x:
                    st = x
                    en = y
        
        # print(s[st:en + 1])
        return s[st:en + 1]
                
sol = Solution()
ans = sol.longestPalindrome("babad")
                

        