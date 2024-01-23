from typing import List
"""
    그냥, 각 점프 횟수때마다 가장 멀리 갈 수 있는 지점을 구한 후, 그 이전까지는 모두 다 같은 횟수만에 도달할 수 있으므로 그 지점 방문시 어디까지 갈 수 있나 계산하면서 farthest 갱신함
    이후, i가 end에 도달할 시 end = farthest로 해줌으로써 다음 점프할 때의 상태로 갱신해줌.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        ans = 0
        
        for i in range(len(nums) - 1):
            if farthest < i + nums[i]:
                farthest = i + nums[i]
                        
                if i + nums[i] >= n - 1:
                    ans += 1
                    break
            
            # i가 end에 도달했을 때,
            if i == end:
                # end를 새롭게 갱신된 farthest로 업데이트
                end = farthest
                ans += 1
        
        return ans

nums = [2, 3, 0, 1, 4]
sol = Solution()
ans = sol.jump(nums)
print(ans)

