"""
    1. 문제 분석
    시계방향으로 회전하면서 중앙까지 가는 문제

    2. 풀이 방법
    방문체크 리스트 만든 후, 오른쪽 방향으로 시작해서 시계방향으로 방향 바뀌고
    이미 방문한 곳이거나 보드 밖이면 방향 바뀐 후 가는 방식으로 구현
    모든 셀 방문시 종료(cnts 세기)
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 궅이 방문체크 배열 안만들고 matrix 재활용하기
        n = len(matrix)
        m = len(matrix[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dir = 0
        ans = []
        curX, curY = 0, 0
        cnts = 1
        while True:
            # 이동하기 전 해당 위치를 ans에 넣기
            ans.append(matrix[curX][curY]) 

            # 이동하기
            # 끝났는지 체크
            if cnts == n * m:
                return ans

            # 이동할 방향 설정
            nxtX = curX + dx[dir]
            nxtY = curY + dy[dir]

            if nxtX < 0 or nxtX >= n or nxtY < 0 or nxtY >= m:
                dir = (dir + 1) % 4 
            
            elif matrix[nxtX][nxtY] == 101:
                dir = (dir + 1) % 4
            
            # 현재 값은 101으로 초기화
            matrix[curX][curY] = 101
                
            # 해당 방향으로 이동
            curX += dx[dir]
            curY += dy[dir]

            # 방문횟수 1 추가
            cnts += 1
            

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol = Solution()
ans = sol.spiralOrder(matrix)
print(ans)

        