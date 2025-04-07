from typing import List

def test(nums:List[int]) -> int:
    num_set = set(nums)
    first_num = None
    final_len = 0
    for num in nums:
        if num - 1 not in num_set:
            first_num = num
            consutitive_len = 0
            while first_num in num_set:
                first_num += 1
                consutitive_len += 1

        result = max(final_len, consutitive_len)
        final_len = result
    return result

def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_len = 0
    for num in nums_set:
        if num -1 not in nums_set:
            first_num = num
            consutitive_len = 1
            while first_num + 1 in nums_set:
                consutitive_len += 1
                first_num += 1
            max_len = max(max_len, consutitive_len)
    return max_len

nums = [22,23,24,25,26,27,28,29,100,4,200,1,3,2, 8, 9, 10, 11, 12]
nums2 = [1,0,1,2]
print(longestConsecutive(nums))