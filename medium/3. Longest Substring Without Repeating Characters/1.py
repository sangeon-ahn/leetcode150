"""
    1. 문제 분석
    가장 긴 substring(붙어있어야 함)을 구하는 문제(subsequence와는 다름(떨어져 있어도 가능))

    2. 풀이 방법
        - 딕셔너리, deque를 이용한 풀이
            딕셔너리는 substring에 해당 문자가 있는지 여부를 판단하는 역할
            deque는 이미 문자가 있을 시 해당 문자를 발견할 때까지 pop_front() 하는 역할
            마지막 문자에 도달할 때까지 수행

"""
from collections import defaultdict, deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqchrs = set()
        substr = deque()

        idx = 0
        ans = 0
        while idx < len(s):
            ch = s[idx]

            # 만약 uniquechrs에 없으면 넣기
            if ch not in uniqchrs:
                uniqchrs.add(ch)
                substr.append(ch)
            
            # 이미 있으면 빼고 넣기
            else:
                # 기존의 ch 제거
                while substr and substr[0] != ch:
                    uniqchrs.remove(substr.popleft())
                substr.popleft()

                # 넣기
                substr.append(ch)

            ans = max(ans, len(substr))
            idx += 1
        
        return ans
                
            
                

        
        