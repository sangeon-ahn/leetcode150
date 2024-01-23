from typing import List
from collections import deque
"""
    1. 문제 분석
    startGene -> endGene으로 가야 하고,
    한 번 변이할 때 단 하나의 알파벳만 변경 가능
    bfs로 풀 수 있을 것 같다.
    startGene 덱에 넣고 뱅크 for문 돌면서 1차이나면 방문체크하고 큐에 넣기, 이때 cnts값까지 넣기
    이렇게 해서 while 빠져나갈 때까지 계속함.
    while에서 endGene 만난경우 cnts 리턴
    안만난경우엔 while 빠져나오고 이때 -1 리턴

"""
class Solution:
    def check(self, curGene, nextGene):
        res = 0

        for i in range(len(curGene)):
            if curGene[i] != nextGene[i]:
                res += 1
        
        if res == 0 or res >= 2:
            return False
        return True

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 덱 생성
        q = deque()
        # 방문체크용 리스트 생성
        n = len(bank)
        vis = [False for _ in range(n)]

        # q에 startGene 넣기
        q.append((startGene, 0)) # (현재 상태, 변이 횟수)
        
        # q while 돌면서 bfs 수행
        while q:
            curGene, curCnts = q.popleft()

            # 바로 bank 확인
            for i in range(n):
                # 이미 방문한 gene이라면 패스
                if vis[i]:
                    continue
                
                # 유전자 차이 1개일 때,
                if self.check(curGene, bank[i]):
                    # 만약 답이면 끝
                    if bank[i] == endGene:
                        return curCnts + 1

                    vis[i] = True
                    # 답은 아니면 큐에 추가
                    q.append((bank[i], curCnts + 1))
                
                # 차이 0개 or 2개 이상이면 무시함.
        
        # while 빠져나왔는데도 아직 안끝났으면 -1 리턴
        return -1
        
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]       

sol = Solution()
ans = sol.minMutation(startGene, endGene, bank)
print(ans)