"""
    N <= 10만
    일단 부분배열이니까 연속적이어야 함.
    정렬 안되어있음.
    다 더했을 때 타겟보다 작으면 0 리턴

    부분합으로 구하기? -> 합배열: O(N), 부분배열 검사: O(N^2)
    또, 합이 target인 부분배열 중 최저길이를 구해야 함.
    그냥 투포인터로 0에서부터 시작해서 합이 target보다 작으면 right 포인터 증가시키고 크면 left포인터 증가시키는 방법?
"""

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        if sum(nums) < target:
            return 0
        
        left = 0
        right = 0
        
        s = nums[left]
        ans = float('inf')

        while left < n and right < n and left <= right:
            
            # 합이 더 작을 경우
            if target > s: 
                right += 1

                # right가 끝에 도달했으면 끝
                if right >= n:
                    break

                # 그밖엔 s에 더해주기
                s += nums[right]
            
            # 합이 더 클 경우
            elif target < s:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1

                # left가 끝에 도달한 경우,
                if left >= n:
                    break

            # 합이 같을 경우
            else:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
                right += 1

                if right >= n:
                    break

                s += nums[right]
                
        if ans == float('inf'):
            return 0
        return ans

target = 
nums = [1, 4, 4]
sol = Solution()
ans = sol.minSubArrayLen(target, nums)

print(ans)
                
        
        

        

        