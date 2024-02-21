"""
    격자 내에서 0을 발견했을 때, 해당 0이 속하는 행,열의 모든 숫자를 0으로 교체
    
    follow up
    - 공간복잡도 O(mn) 풀이법은 별로다.
    - 공간복잡도 O(m + n) 풀이법도 최선은 아니다. -> 격자 돌면서 채워야 할 행,열 파악 후 다시 격자 돌면서 다 채워주는 것.
    - 상수 공간복잡도를 사용해보라. -> 격자를 돌긴 돌아야 함. 돌면서 한번에 0으로 채워야 함. 그냥 0 만날 때까지 float('inf')로 채우면 되긴 함.
"""
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        dx = [1, 0, -1, 0]        
        dy = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # 상하좌우로 채우기
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        while nx >= 0 and nx < n and ny >= 0 and ny < m and matrix[nx][ny] != 0:
                            matrix[nx][ny] = float('inf')
                            nx += dx[k]
                            ny += dy[k]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0       
      

matrix = [[1,1,1],[1,0,1],[1,1,1]]
sol = Solution()
ans = sol.setZeroes(matrix)
                        



