"""
    일단 딕셔너리에 t 문자 추가해놓고,
    이후, st, en 포인터 만든 후, en < len(nums)일 때까지 while 돌음

    그리고 t 채울 때마다 cnts 더해주다가 cnts == len(t) 되면 답을 갱신하는데, st가 가리키는 문자를 하나씩 빼주고 +1해주면서 답이 더이상 안 될때까지 계속 수행함.

    위 작업이 끝나면, end++ 하고 다시 기존 과정 수행. 
"""
from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for ch in t:
            dic[ch] += 1
        
        st = 0
        en = 0
        stAns = 0
        enAns = 0
        minLen = float('inf')
        sLen = len(s)
        tLen = len(t)
        cnts = 0

        while en < sLen:
            ch1 = s[en]

            # t에 속하는 문자이고 아직 추가해야하는 경우엔 cnts 더해주기
            if dic[ch1] > 0:
                cnts += 1

            # 모든 경우에서 dic에서 하나 빼고 다음 문자 확인하러 en 더해주기
            dic[ch1] -= 1
            en += 1

            # 이제 답인 경우에 답 갱신
            while cnts == tLen:
                if minLen > en - st:
                    minLen = en - st
                    stAns, enAns = st, en
                
                # st가 가리키는 문자를 제거
                ch2 = s[st]
                dic[ch2] += 1

                # 이 조건문을 만족하는 경우는 일단,
                # t에 없는 문자인 경우 무조건 false이고, t에 있는 문자는 t의 해당 문자가 만약 x개 있는 경우 x개를 초과한 경우엔 false이고, dic[ch2]에 1씩 더해지다가 0을 넘기는 순간 이제 true가 되면서 cnts가 1 감소한다.
                # 따라서, 만약 t에 2개의 c가 있고 총 4개의 c가 등장했다면, 현재 dic['c'] = -2이고, cccc 이렇게 나왔을 때, 3번째 c일 때 dic값이 1이므로 카운트가 감소된다.
                if dic[ch2] > 0:
                    cnts -= 1
                
                # st += 1 해줌으로써 다음 문자 보러 가기
                st += 1
    
        return "" if minLen == float('inf') else s[stAns:enAns]
    
s = "ab"
t = "a"
sol = Solution()
ans = sol.minWindow(s, t)                

print(ans)

