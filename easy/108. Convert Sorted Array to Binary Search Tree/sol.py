from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
            
        m = len(nums) // 2
        parent = TreeNode(nums[m])
        
        parent.left = self.sortedArrayToBST(nums[:m])
        parent.right = self.sortedArrayToBST(nums[m + 1:])

        return parent
        
