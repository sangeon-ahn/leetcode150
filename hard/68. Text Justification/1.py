"""
    1. 문제 분석
        words, maxWidth
        maxWidth에 꽉 차게 문자 채우기
        greedy 접근법 사용해라 -> 한 라인에 가장 많은 단어 채우기
        단어 사이의 공백은 가능한 고르게 분배
        공백이 짝수개가 아니면 왼쪽 공백에 더 많이 할당하라.

        마지막 줄은 left justified(왼쪽으로 밀어버리기)
    2. 문제 풀이
        1. 일반적인 띄어쓰기 할 때, maxWidth에 몇 개 단어 들어가야 하는지 판단
        2. 판단 후,
            - 단어 1개 or 마지막 단어였으면 left-justified,
            - 2개 이상일 때, 각 단어 사이의 공백 개수 판단 로직 수행
            - 문자열 1줄 만들어 내고 정답에 추가
        3. 정답 반환
"""
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)

        def getStr(st, en, cumul):
            ans = words[st]

            if st == en:
                return ans + " " * (maxWidth - cumul)

            # 마지막 단어까지 다 들어온거면 정상 공백 추가
            # 근데 나머지 빈 공간 전부 공백으로 채워야 해서, 누적값 필요
            if en == n - 1:
                for i in range(st + 1, en + 1):
                    ans += " " + words[i]
                
                ans += " " * (maxWidth - cumul)
                return ans
            
            # 그 외엔 공백 골고루 추가
            
            # 단어 개수
            wordsCnt = en - st + 1

            # 공백 개수
            blankCnt = en - st + maxWidth - cumul

            # 단어 사이의 공백들
            blanks = [0 for _ in range(wordsCnt - 1)]
            
            idx = 0
            while blankCnt > 0:
                blanks[idx] += 1
                blankCnt -= 1
                idx = (idx + 1) % len(blanks)
            
            idx = 0
            for i in range(st + 1, en + 1):
                ans += (" " * blanks[idx]) + words[i]
                idx += 1
            
            return ans

        start = 0
        end = 0
        cumul = len(words[start])
        idx = 1
        while idx < n:
            # 누적 길이가 maxWidth보다 크면, 
            if cumul + len(words[idx]) + 1 > maxWidth:
                # 문자열 구해서 ans에 추가
                ans.append(getStr(start, end, cumul))
                
                # 리셋
                start = idx
                end = idx
                cumul = len(words[start])
                idx += 1
            
            # 들어갈 수 있으면,
            else:
                # 갱신
                end = idx
                cumul += (len(words[end]) + 1)
                idx += 1

        # 여기서 나머지 추가해야 함.
        ans.append(getStr(start, end, cumul))
        # print(ans)
        return ans

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

sol = Solution()
ans = sol.fullJustify(words, maxWidth)
                
        