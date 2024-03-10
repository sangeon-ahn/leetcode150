"""
    1. 문제 분석
    비어있지 않은 n 크기의 arr을 받음. 문자열로 이루어짐
    answer 배열 구하라
    - answer[i]는 arr[i] 문자열의 부분문자열 중 다른 arr 구성원들의 substring으로 속하지 않은 가장 짧은 substring이다.

    조건
    n 100 이하
    문자열 길이 20 이하
    소문자로만 이루어짐

    2. 풀이
    arr 순회하면서, 각 문자열의 부분문자열 짧은 것부터 구한다.
    있는지 확인법: s1 in s2 하면 된다.

    부분문자열 구하는 법
    - 반복문 돌면서 사이즈 변수로 범위 지정해서 사용
    

"""
from typing import List
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = ["" for _ in range(len(arr))]

        def check(sz, i):
            flag1 = False
            for j in range(len(arr[i])):
                if j + sz > len(arr[i]):
                    break

                flag2 = True
                # 나머지 문자열 검사
                for k in range(len(arr)):
                    if i == k:
                        continue

                    if arr[i][j:j + sz] in arr[k]:
                        flag2 = False
                        break
                
                # 검사 결과 부분문자열 없으면 갱신.
                if flag2:
                    flag1 = True
                    if ans[i] == "":
                        ans[i] = arr[i][j:j + sz]
                    else:
                        ans[i] = min(ans[i], arr[i][j:j + sz])
                        
            return flag1

        # 문자열 하나에 대해
        for i in range(len(arr)):
            sz = 1
            
            while sz <= len(arr[i]) and not check(sz, i):
                sz += 1
        
        return ans
                    
                        
arr = ["abc","bcd","abcd"]
sol = Solution()
ans = sol.shortestSubstrings(arr)
