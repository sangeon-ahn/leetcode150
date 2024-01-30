"""
    1. 문제 분석
        문자열 s가 주어지고, 같은 길이의 단어들로 구성된 words 배열이 주어질 때,
        모든 words 속 단어들로 만들 수 있는 모든 concatenated string에 대해, s에서 해당 string을 찾을 수 있는 시작 지점을 answer 배열에 전부 넣어 반환해라.
    
    2. 풀이 방법
        - s가 word와 같은 길이 단위로 잘라진다는 가정이 없다 -> len(word)만큼 for문 순회하며 처음에 건너뛰기 해줘야 함.
        - 이후, 해당 substring이 concat string에 속하는지 판단
        - 근데, 단어길이만큼 점프하면서 확인할 것이기 때문에, 딕셔너리로 존재유무 체크해야 함
        - 내부에서 cnt 변수 만든 후, cnt == len(words)인 경우 정답에 초기인덱스 추가 
        - 이후, 중복된 단어 나온 경우, 해당 단어를 없앨 때까지 딕셔너리에서 제거하며 cnts도 낮춤

"""
from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        wLen = len(words[0])
        sLen = len(s)
        ans = []

        # 1. 단어 존재유무 확인용 딕셔너리 생성 및 세팅
        dic1 = defaultdict(int)
        for w in words:
            dic1[w] += 1

        # 1. for문 돌기
        for i in range(wLen):
            initIdx = i
            cnts = 0
            dic2 = defaultdict(int)
            
            for j in range(i, sLen, wLen):
                # 해당 substring이 words에 속하면 추가
                substr = s[j:j+wLen]

                if dic1[substr]:
                    # words에 있는데 아직 추가 안된 경우.
                    if dic1[substr] > dic2[substr]:
                        dic2[substr] += 1 
                        cnts += 1
                    # 이미 추가되었으면,
                    else:
                        # 해당 단어가 pop될 때까지 cnts와 dic2 갱신
                        while dic2[substr] >= dic1[substr]:
                            dic2[s[initIdx:initIdx + wLen]] -= 1
                            cnts -= 1
                            initIdx += wLen
                        dic2[substr] += 1
                        cnts += 1
                        
                # 없는 단어면 초기화
                else:
                    while cnts > 0:
                        dic2[s[initIdx:initIdx + wLen]] -= 1
                        initIdx += wLen
                        cnts -= 1
                    initIdx = j + wLen

                # concat string 만들었으면 답에 추가.
                if cnts == n:
                    ans.append(initIdx)
            
        return ans

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

sol = Solution()
ans = sol.findSubstring(s, words)

print(ans)