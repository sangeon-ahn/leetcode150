import time
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]

        left, right, idx, n = 0, 0, 0, len(s)
        while idx < n:
            while idx < n and s[idx] != ' ':
                

s = "Hello World Man"
sol = Solution()
ans = sol.reverseWords(s)
        
