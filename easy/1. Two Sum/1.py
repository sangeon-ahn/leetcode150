from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        
        for i in range(len(nums)):
            if target - nums[i] in dic:
                if nums[i] == target - nums[i]:
                    if len(dic[nums[i]]) >= 2:
                        return [dic[nums[i]][0], dic[nums[i]][1]]
                else:
                    return [dic[target - nums[i]][0], i]
            else:
                dic[nums[i]].append(i)


        