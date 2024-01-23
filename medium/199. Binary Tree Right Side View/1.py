"""
    tree를 bfs로 순회해서, 각 level을 인덱스로 가지는 리스트 생성 후, 자기 레벨에 해당하는 위치에 자기 값을 넣는다.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        values = []
        q.append([root, 0])
        maxLevel = 0

        while q:
            curNode, curLevel = q.popleft()

            if q and q[0][1] != curLevel or not q:
                values.append(curNode.val)

            if maxLevel < curLevel:
                maxLevel = curLevel

            if curNode.left:
                q.append((curNode.left, curLevel + 1))
            
            if curNode.right:
                q.append((curNode.right, curLevel + 1))
        
        return values
            


        