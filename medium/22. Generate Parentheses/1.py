"""
    덮을 수도 있고, 왼쪽, 오른쪽에 있을 수도 있다.
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        memo = {}

        def recur(depth, remained, parenthese):
            if depth == n:
                ans.add(parenthese)
                return
            
            if depth + remained > n:
                return

            if depth + remained < n:
                recur(depth, remained + 1, parenthese + "(")

            if remained > 0:   
                recur(depth + 1, remained - 1, parenthese + ")")

        recur(0, 1, "(")
        # print(ans)
        return list(ans)