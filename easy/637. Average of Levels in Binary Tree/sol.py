# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        ans = []

        while q:
            avg = 0
            for i in range(len(q)):
                avg += q[i].val
            
            ans.append(avg / len(q))

            for i in range(len(q)):
                node = q.pop()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans

                
        