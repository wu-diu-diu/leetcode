
def test(nums, k):
    tmp = 0
    res = float('inf')
    flag = False
    left = 0
    for right, num in enumerate(nums):
        tmp += num
        while tmp >= k:
            tmp -= nums[left]
            res = min(res, right - left + 1)
            left += 1
            flag = True
    return res if flag else 0

nums = [2,3,1,2,4,3]
print(test(nums, 7))
        