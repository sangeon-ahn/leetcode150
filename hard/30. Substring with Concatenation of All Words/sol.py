from collections import defaultdict
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        wordLen = len(words[0])
        wordCount = defaultdict(int)

        for word in words:
            wordCount[word] += 1
        
        ans = []

        #wordLen 길이까지만 순회해도 되는 이유: 어차피 발견 못하면 wordLen만큼 추가한 인덱스에서부터 다시 체크하기 때문
        for i in range(wordLen):
            left = i
            count = 0
            tempWordCount = defaultdict(int)

            for j in range(i, len(s) - wordLen + 1, wordLen): #i부터 word길이만큼 점프하면서 확인
                word = s[j:j + wordLen]

                if word in wordCount:
                    tempWordCount[word] += 1
                    count += 1

                    # 초과한 단어를 모두 지우는 루프
                    # 초과하면, 해당 word가 leftWord가 되어 tempWordCount에서 pop될 때까지 while 수행한다.
                    while tempWordCount[word] > wordCount[word]:
                        leftWord = s[left: left + wordLen]
                        tempWordCount[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    # 정답이면 정답에 추가
                    if count == len(words):
                        ans.append(left)
                
                # 후보단어가 단어리스트에 없으면 지금까지 저장한거 초기화 
                # left를 다시 concat string의 시작지점으로 설정함.
                else:
                    tempWordCount.clear()
                    count = 0
                    left = j + wordLen

        return ans


