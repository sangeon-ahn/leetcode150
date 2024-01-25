"""
    1. 문제 분석
    isomorphic Strings
    s -> t 문자열로 바꿀 수 있는지 묻는 문제
    s의 각 문자를 변환해서 t로 만들 수 있는지?

    2. 풀이 방법
    일단 길이 같은 지 체크
    같으면, set 생성 후 s, t 각각 각 알파벳 별 위치를 담는 리스트가 원소인 딕셔너리를 만들어 순회하며 삽입하기

    이후, 두 딕셔너리의 values가 같으면 true, 다르면 false 
"""
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        sDic = defaultdict(list)
        tDic = defaultdict(list)

        for i in range(n):
            sDic[s[i]].append(i)
            tDic[t[i]].append(i)
        
        # 두 dic values 같은지 체크
        a = list(sDic.values())
        b = list(tDic.values())
        
        return a == b

s = "egg"
t = "add"

sol = Solution()
ans = sol.isIsomorphic(s, t)
print(ans)