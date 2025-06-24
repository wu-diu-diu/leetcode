from collections import defaultdict 

def test(nums: list[int], k: int):
    dic = defaultdict(int)
    tmp_res = 0
    res = 0
    left = 0
    for i, num in enumerate(nums):

        while dic[num] >= k:
            dic[nums[left]] -= 1
            tmp_res -= 1
            left += 1

        dic[num] += 1
        tmp_res += 1
        res = max(tmp_res, res)
    return res

nums = [1,2,3,1,2,3,1,2]
print(test(nums, 2))
