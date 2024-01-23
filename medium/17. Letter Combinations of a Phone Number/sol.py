from typing import List
from collections import defaultdict, deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        ans = []
        def backtracking(order, temp: List):
            if order == len(digits):
                ans.append("".join(temp.copy()))
                return
            
            letters = dic[digits[order]]

            for i in range(len(letters)):
                temp.append(letters[i])
                backtracking(order + 1, temp)
                temp.pop()
        
        backtracking(0, [])
        
        return ans


digits = "23"
sol = Solution()
ans = sol.letterCombinations(digits)
print(ans)
                
