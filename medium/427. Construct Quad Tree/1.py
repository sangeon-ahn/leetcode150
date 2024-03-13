
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
4개로 나눈 각각에 대해 모두 0인지 1인지 파악
모두 1이거나 0이면 isLeaf=1이고, val은 1이거나 0이다.
모두 1이 아니면, 또 재귀호출해서 4등분 한다.

recur(topleftPosition, width)

반환값? -> topLeft, topRight, bottomLeft, bottomRight에 해당하는 노드
재귀 탈출 조건 = 다 1,0이면 바로 노드 생성해서 반환하며 탈출, 아니면 4개로 나눈거 반환받아 연결하고 자기 반환하면서 탈출
"""
from typing import List
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recur(x, y, width):
            # 크기 1이면
            if width == 1:
                return Node(grid[x][y], 1, None, None, None, None)
            
            # 그 외엔 검사

            allSame = True
            for i in range(x + width):
                for j in range(y + width):
                    if grid[x][y] != grid[i][j]:
                        allSame = False
                        break

                if not allSame:
                    break
            
            if allSame:
                return Node(grid[x][y], 1, None, None, None, None)
            
            topLeft = recur(x, y, width//2)
            topRight = recur(x, y + width//2, width//2)
            bottomLeft = recur(x + width//2, y, width//2)
            bottomRight = recur(x + width//2, y + width//2, width//2)

            return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
            
        return recur(0, 0, len(grid))
        