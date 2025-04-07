## 数组按升序，没有重复值
## 在某一个索引处发生旋转，即该索引之前的子数组移动到最后，当前所有变为数组的第一个元素
## 二分法找到一个旋转数组的最小值的索引
def search_min(nums: list[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1
    ## 最终left会在right左边，此时left=mid，故left不再移动，所以while的结束条件要判断为left紧挨着right
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:  ## 中点大于最后一个值，则最小值在中点的右边，包括中点
            left = mid
        else:  ## 反之则在中点左边，包括中点
            right = mid
    return right
## 二分法找到目标值，找不到返回-1，找到返回目标值索引
def search_binary(nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

def search(nums: list[int], target: int) -> int:
    n = len(nums)
    index = search_min(nums)
    ## 如果目标值大于最后一个值，则目标值位于第一段
    if target > nums[-1]:
        return search_binary(nums[:index], target)
    ## 反之位于第二段
    else:
        result = search_binary(nums[index:], target)
        return -1 if result == -1 else result + index  ## 如果第二段内没有目标值则返回-1，有则需要返回索引同时加上index
        ## 因为题目要的是目标值在原数组的索引，二分法返回的是在第二段数组内的索引


nums = [4,5,6,7,8,9,0,1,2]
nums = [3,1]
target = 0
print(search(nums, target))