class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre = None
        res = float('inf')

        # if not root:
        #     return 
        
        def dfs(node):
            if not node :
                return 
            dfs(node.left)
            nonlocal pre,res 

            if pre:
                res = min(res,node.val-pre.val)
            pre = node

            dfs(node.right)
        dfs(root)
        return res 