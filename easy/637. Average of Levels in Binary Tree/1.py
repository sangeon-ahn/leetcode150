# Definition for a binary tree node.
"""
    루트노드부터 타고 내려가면서 level을 인자로 넘겨주는데 노드 개수가 최대 1만개인데 불균형 트리 감안해서 배열크기 1만으로 할당해주고
    각 노드가 속하는 레벨의 배열에 더해주면서 재귀호출 
    -> 그냥 딕셔너리로 하면 될듯
"""
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        valDic = defaultdict(list)

        def addValue(node: Optional[TreeNode], level):
            if level not in valDic:
                valDic[level].append(node.val)
                valDic[level].append(1)
            else:
                valDic[level][0] += node.val
                valDic[level][1] += 1

            if node.left:
                addValue(node.left, level + 1)
            if node.right:
                addValue(node.right, level + 1)
        
        addValue(root, 0)

        level = 0
        ans = []

        while level in valDic:
            ans.append(valDic[level][0] / valDic[level][1])
            level += 1
        
        return ans
            
            
            

        