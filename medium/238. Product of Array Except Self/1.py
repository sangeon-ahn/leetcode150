from typing import List
"""
    O(N), 나누기 연산 금지

"""
class Solution:
    # O(N^2)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     answer = [1 for _ in range(len(nums))] 

    #     for i in range(len(nums)):
    # #         for j in range(len(answer)):
    # #             if i == j:
    # #                 continue

    # #             answer[j] *= nums[i]

    # #     return answer
    
    # # O(N)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     ans = [1 for _ in range(n)]
    #     lefts = [1 for _ in range(n)]
    #     rights = [1 for _ in range(n)]

    #     for i in range(n):
    #         if i == 0:
    #             continue

    #         lefts[i] = lefts[i - 1] * nums[i - 1]
        
    #     for i in range(n - 1, -1, -1):
    #         if i == n - 1:
    #             ans[i] = lefts[i]
    #             continue

    #         rights[i] = rights[i + 1] * nums[i + 1]
    #         ans[i] = lefts[i] * rights[i]
        
    #     return ans
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
        
        
    


nums = [1, 2, 3, 4]
# nums = [-1, -1, 0, -3, 3]
sol = Solution()
ans = sol.productExceptSelf(nums)
print(ans)
        