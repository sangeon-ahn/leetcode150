from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, node, arr, dir):
        if not node:
            arr.append('null')
        else:
            arr.append(node.val)
            if dir == 1:
                self.inorder(node.left, arr, dir)
                self.inorder(node.right, arr, dir)
            else:
                self.inorder(node.right, arr, dir)
                self.inorder(node.left, arr, dir)
                
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []
        self.inorder(root.left, arr1, 1)
        self.inorder(root.right, arr2, -1) 

        if arr1 == arr2:
            return True
        return False
    
        
        
        


        