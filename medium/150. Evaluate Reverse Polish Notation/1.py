"""
    스택에 숫자를 넣다가 연산자 나오면 계산한 후 결과 넣어주고 하면 된다.
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                st.append(int(token))
            else:
                num1, num2 = st.pop(), st.pop()
                if token == "+":
                    st.append(num1 + num2)
                elif token == "-":
                    st.append(num1 - num2)
                elif token == "*":
                    st.append(num1 * num2)
                else:
                    st.append(int(num2 / num1))
        
        return st[-1]


    # print(int(6 / -132))