"""
    1. 문제 분석
        "PAYPALISHIRING"

        P   A   H   N
        A P L S I I G
        Y   I   R
        
        지그재그 모양으로 출력되고, numRows는 몇행으로 구성될건지 설정하는 역할.
        1 <= s.length <= 1000
    2. 풀이 방법
        일단, numRows 만큼 리스트 만들어 사용하는게 편함.
        문자열 순회하면서 각 리스트에 저장함. 인덱스는 012101210... 이런식으로 해서 넣기
        출력은 0번째 행부터 출력해야 함. 
        출력 규칙: 

        저런식으로 출력까지 하라는 문제가 아니라 그냥 각 줄에 속하는 문자를 다 합쳐 하나의 문자열로 만들면 되는 쉬운 문제였다.
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chars = [[] for _ in range(numRows)]

        def setIdx(idx, rows, dir):
            if idx + 1 == rows:
                return [idx - 1, -dir]
            
            if idx == 0 and dir == -1:
                return [idx + 1, -dir]
            
            return [idx + dir, dir]
                
        idx = 0
        dir = 1
        for i in range(len(s)):
            chars[idx].append(s[i])

            if 0 < idx < numRows - 1:
                # 내려가는 방향이면,
                if dir == 1:
                # i-idx <= x < i 까지 ' ' 추가
                    temp = idx - 1
                    while temp >= 0:
                        chars[temp].append(' ')
                        temp -= 1

                # 올라가는 방향이면,
                else:
                    temp = idx + 1
                    while temp < numRows:
                        chars[temp].append(' ')
                        temp += 1
                
            idx, dir = setIdx(idx, numRows, dir)
        
        
        ans = ""

        for arr in chars:
            ans += ''.join(arr)
            print(''.join(arr))

        return ans
s = "PAYPALISHIRING"
numRows = 3

sol = Solution()
ans = sol.convert(s, numRows)
        
        