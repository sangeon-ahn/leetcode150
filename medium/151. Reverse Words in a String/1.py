"""
    1. 문제 분석
        문자열 s가 주어질 때, 문자열 속 단어들의 순서를 반대로 해라.
    
    2. 풀이 방법
        띄어쓰기 기준으로 split 해서 단어들 리스트 만들기
        이후, reverse 하고 띄어쓰기 기준 출력
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        sLen = len(s)
        p = -1
        ans = []

        for i in range(sLen - 1, -1, -1):
            if p == -1 and s[i] != ' ':
                p = i

            elif p != -1 and s[i] == ' ':
                ans.append(s[i + 1:p + 1])
                p = -1
        
        if p != -1:
            ans.append(s[0:p + 1])
        
        return ' '.join(ans)
                 


s = "a good   example"
sol = Solution()
ans = sol.reverseWords(s)

        