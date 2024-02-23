class Solution:
    def longestConsecutive(nums):
        nums = set(nums)
        ans = 0

        for num in nums:
            # 자신이 순열에서 가장 작은 숫자라면,
            if num - 1 not in nums:
                nextNum = num + 1
                while nextNum in nums:
                    nextNum += 1
                ans = max(ans, nextNum - num)
                
        return ans
