from typing import List
"""
    k는 nums보다 커질 수 있다. 그리고, len(nums)만큼 수행하면 원본이 된다.  
    따라서, k = 1일 때와 k = 1 + len(nums)일 때의 결과는 같다.
    modK = k % len(nums)
    이후, modK번 pop -> push_front
    이러면 근데 deque 써야함.
    공복 O(1)로 풀려면 스왑해야함.
    []
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        modK = k % n
        print(modK, k, n)
        # 1. modK 이전 수들 리버스
        # 2. modK 이후 수들 리버스
        # 3. st, en부터 좁히면서 스왑
        
        for i in range(n - modK):
            if i >= (n - modK) // 2:
                break

            temp = nums[i]
            nums[i] = nums[n - modK - (i + 1)]
            nums[n - modK - (i + 1)] = temp
        print(nums)

        for i in range(n - modK, n):
            if modK % 2 == 0:
                if i > (2*n - modK - 1) // 2:
                    break
            else:
                if i >= (2*n - modK - 1) // 2:
                    break
                

            temp = nums[i]
            nums[i] = nums[n - ((i-(n-modK)) + 1)]
            nums[n - ((i-(n-modK)) + 1)] = temp
        print(nums)

        for i in range(n):
            if i >= n // 2:
                break

            temp = nums[i]
            nums[i] = nums[n - i - 1];
            nums[n - i - 1] = temp

                
nums = [-1, -100, 3, 99]
sol = Solution()
ans = sol.rotate(nums, 2)
print(nums)
        
        