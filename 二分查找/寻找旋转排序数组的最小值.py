## 对于一个升序数组，旋转一次则将数组最后一个数移动到第一位
## [1,2,3,4,5] 旋转三次变为：[3,4,5,1,2]
## 如果一个升序数组没有旋转，或者旋转了长度n词，则最小值则为第一个数
def search_min(nums: list[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid
        else:
            right = mid
    return min(nums[right], nums[left])  ## 这里加一个min则是考虑上述没有旋转或者旋转n次的情况
    ## 如果是旋转数组，最终left在right的前一位，此时right则为最小值
    ## 如果是特殊情况，left在right前一位，此时left是最小值

nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
print(search_min(nums))