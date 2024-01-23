# Definition for a binary tree node.
"""
    못품
"""
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[len(nums) // 2])

        st = 0
        en = len(nums) - 1
        mid = (st + en) // 2

        stack = [(st, mid - 1, 0, root), (mid, en, 1, root)]
        
        while stack:
            s, e, dir, node = stack.pop()
            if s > e:
                continue

            if s == e:
                if dir == 0:
                    node.left = TreeNode(nums[s])
                else:
                    node.right = TreeNode(nums[e])
                continue
            
            # 루트노드 생성하고 연결하고 나눠서 다시 스택에 넣기
            m = (s + e) // 2
            child = TreeNode(nums[m])
            
            if dir == 0:
                node.left = child
            else:
                node.right = child
            
            stack.append((s, m - 1, 0, child))
            stack.append((m + 1, e, 1, child))

        return root
nums = [-10,-3,0,5,9]
sol = Solution()
ans = sol.sortedArrayToBST(nums)
print(ans)

        

        