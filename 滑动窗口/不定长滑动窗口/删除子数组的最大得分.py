from typing import List
## for循环负责窗口左边界的移动，while循环负责窗口右边界的移动
## 方法1其实是暴力枚举，每个元素都要作为窗口的左边界区开始滑动，时间复杂度是O(n2)
def test(nums: List[int]):

    max_result = float('-inf')
    length = len(nums)
    for i in range(length):
        added = set()
        sub_sum = 0
        j = i
        while nums[j] not in added:
            sub_sum += nums[j]
            added.add(nums[j])
            j += 1
            if j == length:
                break
        if sub_sum > max_result:
            max_result = sub_sum

    return max_result

nums = [5,2,1,2,5,2,1,2,5]

## 方法2的时间复杂度更低
## 右边界不断向前移动，左边界只在需要的时候向前移动
## 每个元素都只被操作常数次，即滑入窗口和滑出窗口
def test2(nums: list[int]):
    seen = set()
    tem_res = 0
    res = float('-inf')
    l = 0
    ## for循环控制右边界，while循环控制左边界
    ## i标记了窗口的右边界
    for i, num in enumerate(nums):
        while num in seen:
            seen.remove(nums[l])
            tem_res -= nums[l]
            ## l标记了滑动窗口的左边界
            l += 1
        tem_res += num
        seen.add(num)
        res = max(res, tem_res)
    return res
nums = [5,2,1,2,5,2,1,2,5]
print(test2(nums))
        
        
        


