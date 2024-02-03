from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def construct(current: str, wordDict, memo = {}):
            if current in memo:
                return memo[current]
            
            if not current:
                return True
            
            for word in wordDict:
                if current.startswith(word):
                    newCurrent = current[len(word):]
                    memo[current] = True

                    if construct(newCurrent, wordDict, memo):
                        return True
            
            memo[current] = False
            return False

        return construct(s, wordDict)