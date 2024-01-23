from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorNum = nums[0]
        cnts = 1

        for n in nums[1:]:
            if majorNum == n:
                cnts += 1
            else:
                cnts -= 1

                if cnts == 0:
                    majorNum = n
                    cnts = 1
        
        return majorNum

# nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
sol = Solution()
ans = sol.majorityElement(nums)
print(ans)
        

            