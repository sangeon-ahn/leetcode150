"""
    숫자를 만들어서 
"""
class Solution:
    def calculate(self, s: str) -> int:
        st = []
        sign = 1
        res = 0
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            elif s[i] == '+':
                res += num * sign
                num = 0
                sign = 1
            elif s[i] == '-':
                res += num * sign
                num = 0
                sign = -1
            elif s[i] == '(':
                st.append(res)
                st.append(sign)
                sign = 1
                res = 0
            elif s[i] == ')':
                res += sign * num
                num = 0
                res *= st.pop()
                res += st.pop()
        
        if num != 0:
            res += sign * num
        
        return res

s = "(1+(4+5+2)-3)+(6+8)"
sol = Solution()
ans = sol.calculate(s)
print(ans)
