class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        nums를 도는 인덱스와, nums에 채워주는 인덱스를 따로 만든 후, 비교할 값을 설정한 후, 같다면 넘어가고, 다르다면 nums에 채워준 후 nums에 채워주는 인덱스를 하나 올린다. nums를 도는 인덱스는 while문 돌 때마다 1씩 증가한다.
        """
        checked_num = nums[0]
        nums_idx = 1
        filled_idx = 1

        while nums_idx < len(nums):
            if nums[nums_idx] != checked_num:
                nums[filled_idx] = checked_num = nums[nums_idx]
                filled_idx += 1

            nums_idx += 1

        return filled_idx