"""
    일단, 제약조건이 작다.
    단어 개수:1천개
    s길이:300
    단어길이:20이하
    그래서, 그냥 s랑 wordDict 2중for문 돌면 될 것 같다.
"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sLen = len(s)
        WdLen = len(wordDict)

        dp = [True] + [False for _ in range(sLen)]
        sm = 1

        while True:
            # dp값이 True인 지점 찾기
            for i in range(sLen, -1, -1):
                # True인 지점 찾았으면,
                if dp[i]:
                    # substring 확인
                    for w in wordDict:
                        if s[i-1:i-1 + len(w)] == w:
                            dp[i-1+len(w)] = True

            temp = sum(dp)                 

            if sm == temp:
                return False
            
            if dp[sLen]:
                return True

s = "leetcode"
wordDict = ["leet","code"]
sol = Solution()
ans = sol.wordBreak(s, wordDict)

print(ans)
                    
        