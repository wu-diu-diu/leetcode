## 时间复杂度为O(n2)
def test(nums: list[int]) -> list[int]:
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j+1] < nums[j]:
                tmp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tmp
    return nums

nums = [6,3,1,2,5,9,8,4,7]
print(test(nums))
            
            