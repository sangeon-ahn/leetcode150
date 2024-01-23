"""

"""
from typing import List
from collections import defaultdict, deque
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        ans = []

        # dic 구조 짜기
        dic = defaultdict(deque)

        for i in range(len(letters)):
            dic[i//3 + 2].append(letters[i])
        
        dic[7].append(dic[8].popleft())
        dic[8].append(dic[9].popleft())
        dic[9] += dic[10]
        del dic[10]

        lst = []
        def backtracking(order, n):
            if order == len(digits):
                ans.append(''.join(lst))
                return

            dq = dic[int(digits[order])]

            for j in range(len(dq)):
                lst.append(dq[j])
                backtracking(order + 1, n) 
                lst.pop()
                    
        backtracking(0, len(digits))

        return ans
            

        
        # digits = "23"일 때, (a,b,c) * (d,e,f)
        

        

digits = "2"
sol = Solution()
ans = sol.letterCombinations(digits)
print(ans)
        

        