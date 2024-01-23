from collections import defaultdict
from collections import deque
from typing import List
"""
    이 코드가 내 코드보다 더 빠른 이유
    1. 내 코드는 큐에서 원소 뽑을 때마다 wordList를 순회해서 O(N)이 소요되는데, 정답코드는 하나만 다른 것들 중 정답이 있는지 보기 때문에,
    정답 후보들 중 하나 뽑기 vs 모든 후보들을 1개 차이 나는지 확인해가며 확인
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        n = len(beginWord)
        allCombDict = defaultdict(list)

        # 모든 단어에 대해서,
        for word in wordList:
            # 시작단어의 문자를 하나하나 확인
            for i in range(n):
                # word에서 각 문자에 *를 붙인 key에 값은 리스트로 word를 추가함.
                allCombDict[word[:i] + "*" + word[i+1:]].append(word)
        """
        wordList = ["hot","dot","dog","lot","log","cog"]
        change_map ={ *ot : hot, dot, lot
                    h*t : hot
                    ho* :hot
                    d*t : dot
                    do* : dot, dog
                    *og : dog, log, cog
                    d*g : dog
                    l*t : lot
                    lo* : lot, log
                    l*g : log
                    c*g: cog
                    co* : cog 
                    }
        
        """
        q = deque([beginWord, 1])
        
        # 방문체크를 배열로 하지않고 set으로 하는 것도 생각해보자.
        visited = set()
        visited.add(beginWord)

        while q:
            curWord, curLevel = q.popleft()

            for i in range(n):
                interWord = curWord[:i] + "*" + curWord[i + 1:]

                # 해당 키에 있는 리스트속 word들 중에
                for word in allCombDict[interWord]:
                    if word == endWord: # 정답 찾았으면 리턴.
                        return curLevel + 1
                    
                    # 정답 아닌데 아직 방문하지 않은 단어면,
                    if word not in visited:
                        # 방문체크하고 큐에 삽입
                        visited.add(word)
                        q.append((word, curLevel + 1))

        return 0