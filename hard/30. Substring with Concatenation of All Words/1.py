"""
    우선, s길이<=1만
    단어 개수 <=5천
    단어길이 <=30
    
    후보 concat문자열 가지수 = 5000!
    각각 순회 = 1만
    시간복잡도 = O(len(Words)! * len(s)))
    -> 이 방법으로 안됨.

    words 순회: 5천
    s 순회: 1만
    O(WS) -> 5천만. 애매

    일단, s를 다 word 길이로 잘라서 deque1에 넣음
    이후, deque2를 만든 후, deque1 front에서부터 빼면서 이미 substring에 있는 단어인지 확인
    없으면 추가, 있으면 해당 단어가 pop될 때까지 pop_front하기
    deque2 크기 = len(words)이면 시작 단어의 인덱스를 answer리스트에 추가 + pop_front 한번 하고 다시 수행
    언제까지 수행? deque1 마지막 원소까지 갔을 때.
"""
from typing import List
from collections import deque, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        p1 = 0
        p2 = len(words[0])
        ans = []

        dic = defaultdict(int)
        for word in words:
            dic[word] += 1

        # p1~p2사이 부분문자열이 words에 속하는지 확인
        cnts = 0
        while p2 < len(s):
            # 일단, 해당 부분문자열이 valid하면,
            if s[p1:p2 + 1] in dic and dic[s[p1:p2 + 1]] > 0:
                # 사용하고 cnts 추가
                dic[s[p1:p2 + 1]] -= 1
                cnts += 1

                # 단어 다 사용했으면 ans에 추가
                if cnts == len(words):
                    ans.append(p1)
                # 포인터 이동



                    
                    
            
            

        