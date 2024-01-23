"""
    <이거 아님>
    이진탐색트리에서 두 노드값의 차이의 절대값이 가장 작은 경우를 구해라.
    부모-자식간 차이만 따져보면 된다.
    이유: 자식-자식간엔 부모가 사이에 있고, 무조건 자식-자식 차이가 더 클 수밖에 없다.
    조상-손자간 차이: 부모-손자간 차이가 더 작을 수밖에 없다.

    왼쪽 서브트리, 오른쪽 서브트리, root

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def inorder(self, root, nums):
        if root.left:
            self.inorder(root.left)
        
        if root.right:
            self.inorder(root.right)
        
        if root:
            nums.append(root.val)
        

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = float('inf')
        nums = []
        
        self.inorder(root, nums)

        for i in range(1, len(nums)):
            val = nums[i + 1] - nums[i]
            if minDiff > val:
                minDiff = val

        return minDiff
        

        







        