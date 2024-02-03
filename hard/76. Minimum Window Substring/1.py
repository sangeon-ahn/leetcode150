"""
    1. 문제 분석
        s: 길이 m의 문자열
        t: 길이 n의 문자열
        답은 유일하다

        t에 속하는 문자들을 모두 포함하는 substring 중 최소길이의 문자열을 구하라.
    
    2. 풀이 방법
        전에 비슷한 문제 푼 적 있다.
        t를 일단 문자단위로 분해해서 딕셔너리에 추가
        이후, s를 순회하면서 t에 속하면 체크, 이미 존재하면 그거 pop 할때까지 pop
        cnts도 계산하고 있어야 함.
"""
from collections import defaultdict, deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1 = defaultdict(int)
        for ch in t:
            dic1[ch] += 1
        
        cnts = 0
        chars = deque()
        dic2 = defaultdict(int)
        minLen = float('inf')
        ans = ""

        for i in range(len(s)):
            # t에 있는건데 
            if s[i] in dic1:
                # 이미 존재하는 경우 해당 문자 이후에 
                while dic1[s[i]] <= dic2[s[i]]:
                    # chars에서 pop_front 하면서 cnts도 제거하고 dic2도 제거
                    ch = chars.popleft()

                    if ch in dic1 and dic1[ch] > 0:
                        cnts -= 1
                        dic2[ch] -= 1
                
                # 이제, 최소 t문자 나올 때까지 pop
                while chars and chars[0] not in dic2:
                    chars.popleft()
                    
                # 여기 오면 넣어도 됨
                cnts += 1
                chars.append(s[i])
                dic2[s[i]] += 1
            
            # t에 없는거면
            else:
                # chars에 추가
                chars.append(s[i])
            
            # cnts 체크
            if cnts == len(t) and minLen > len(chars):
                minLen = len(chars)
                ans = "".join(chars)
        
        return ans

s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"
sol = Solution()
ans = sol.minWindow(s, t)
print(ans)





        