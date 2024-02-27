from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        
        # 이제 root의 양 자식 있다.
        def same(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            # p와 q 값이 같으면 
            flag = True
            if p.val == q.val:
                # p.left와 q.right에 해대 same() 진행
                flag = same(p.left, q.right) and same(p.right, q.left)
            else:
                return False
            return flag
                # p.right와 q.left

        return same(root.left, root.right)
        
            
            