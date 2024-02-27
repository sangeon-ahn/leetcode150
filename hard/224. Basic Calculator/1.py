"""
    1. 문제 분석
        유효한 표현식 s가 주어질 때, 그걸 잘 평가하는 계산기 구해라.
        eval()같은 빌트인 함수 사용하면 안된다.

        제약조건
        1 <= s길이 <=30만
        s는 +-()' '으로 이루어져 있다.
        +는 unary operation으로 사용되지 않는다.
        -도 마찬가지다.
        두 개의 연속적인 연산 입력은 안들어온다.
        32비트 signed 정수 계산기
    2. 풀이 방법
        일단, 띄어쓰기는 무시한다.
        (도 넣고 )도 넣는데 ) 나오는 순간 ( 나올 때까지 스택 pop 해가며 계산한다.
        함수 하나 만든다.
        - ( 나오는 순간 호출돼서 () 결과 알려주는 함수
        
"""
class Solution:
    def calculate(self, s: str) -> int:
        def calSubExp(idx):
            nextIdx = idx + 1
            res = 0
            subSt = []
            dir = 1
            flag = False
            st = 0
            en = 0

            while nextIdx < len(s) and s[nextIdx] != ')':
                if s[nextIdx] == ' ':
                    nextIdx += 1
                    continue

                if s[nextIdx] == '(':
                    val, resIdx = calSubExp(nextIdx)
                    res += val * dir
                    nextIdx = resIdx
                    dir = 1
                elif s[nextIdx] == '+':
                    if flag:
                        subSt.append(int(s[st:en + 1]) * dir)
                        flag = False
                        dir = 1
                    # dir = 1
                elif s[nextIdx] == '-':
                    if flag:
                        subSt.append(int(s[st:en + 1]) * dir)
                        flag = False
                    dir = -1
                else:
                    if not flag:
                        st = nextIdx
                        en = nextIdx
                        flag = True
                    else:
                        en = nextIdx
                    
                nextIdx += 1

            if flag:
                subSt.append(int(s[st:en+1]) * dir)
            for x in subSt:
                res += x

            return res, nextIdx

        st = []
        dir = 1
        i = 0
        ans = 0
        flag = False
        start = 0
        end = 0

        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i] == '(':
                res, i = calSubExp(i)
                st.append(res * dir)
                dir = 1
            elif s[i] == '+':
                if flag:
                    st.append(int(s[start:end + 1]) * dir)
                    flag = False
                    dir = 1
                None
            elif s[i] == '-':
                if flag:
                    st.append(int(s[start:end + 1]) * dir)
                    flag = False
                dir = -1
            else:
                if not flag:
                    flag = True
                    start = i
                    end = i
                else:
                    end = i
            i += 1

        if flag:
                st.append(int(s[start:end+1]) * dir)
        for x in st:
            ans += x

        return ans
            
s = "1 + 1"
sol = Solution()
ans = sol.calculate(s)
print(ans)


        