def removeDuplicates(nums: list):
    k = len(list(set(nums)))

    # 개수가 2 이상인걸 1 될때까지 삭제
    idx = 0
    while (k < len(nums)):
        # 뒤랑 숫자 같으면 삭제
        if nums[idx] == nums[idx + 1]:
            nums.remove(nums[idx])
        
        # 다르면 idx + 1
        else: idx += 1
        
    return k


arr = [0,0,1,1,1,2,2,3,3,4]

removeDuplicates(arr)
print(arr)
