"""
    1. 문제 분석
    시작 단어는 wordList에 있을 필요가 없다.
    한번에 하나의 알파벳만 바꿀 수 있을 때, 몇번 바꿔야 endWord가 될 수 있을까?

    2. 풀이 전략
    일단 유전자문제처럼 한번에 1알파벳만 바꿀 수 있다. 그리고 해당 단어로 가장 빠른 스텝으로 도달하는 경우만 생각하면 되므로, bfs로 풀면 되겠다. 
    
    beats 7% 느린코드
"""
from typing import List
from collections import deque
class Solution:
    def check(self, curWord, nextWord):
        result = 0
        for i in range(len(curWord)):
            if curWord[i] != nextWord[i]:
                result += 1
        
        return result == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 일단, endWord가 wordList에 있는지 확인
        if endWord not in wordList:
            return 0

        # 덱 생성
        q = deque()

        # 방문체크
        n = len(wordList)
        vis = [False for _ in range(n)]

        # 덱에 시작단어 넣기
        q.append((beginWord, 1))
        
        # bfs 시작
        while q:
            curWord, curCnts = q.popleft()

            # 바로 wordList 순회해가며 조건 체크
            for i in range(len(wordList)):
                # 이미 방문한 단어면 패스
                if vis[i]:
                    continue

                # check 결과 1알파벳 차이만 나면,
                if self.check(curWord, wordList[i]):
                    # 일단 방문할 수 있으니까 방문체크하고,
                    vis[i] = True 
                    # endWord와 같다면 curCnts + 1 리턴
                    if wordList[i] == endWord:
                        return curCnts + 1
                    # endword랑 다르면 큐에 넣고 돌리기
                    else:
                        q.append((wordList[i], curCnts + 1))
                    
                    # 그 외에는 버림. 2개 이상 다르거나 같으면 버림
        
        # while 끝난 후, 리턴 안됐으면 답 없으므로 0 리턴
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

sol = Solution()
ans = sol.ladderLength(beginWord, endWord, wordList)
print(ans)