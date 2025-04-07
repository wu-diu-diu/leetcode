## 将两个有序的数组合并，然后找出中位数
## 思路，将一个数组的每个数作为一个目标值，使用二分法插入到另一个数组中
def search_binary_insert(nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:  ## 如果找到了目标值，则直接将其插入，不用考虑最左边还是最右边，反正插入后数组还是有序的
            return nums[:mid] + [target] + nums[mid:]
    ## 没找到此时left的索引是第一个大于目标值的值，所以目标值应该插入到这里
    return nums[:left] + [target] + nums[left:]

def search_median(nums1: list[int], nums2: list[int]) -> float:
    n2 = len(nums2)
    n1 = len(nums1)
    if n1 > n2:  ## 如果n1更长，则遍历n2，逐步将n2的值插入n1
        for i in range(n2):
            nums1 = search_binary_insert(nums1, nums2[i])
        n1 = len(nums1)  ## 插入后n1的长度要重新计算
        ## 如果是奇数则直接返回中间的值，如果是偶数长度，则需要返回中间两个值的平均值
        return nums1[n1 // 2] if n1 % 2 != 0 else (nums1[n1 // 2] + nums1[n1 // 2 - 1]) / 2
    else:
        for i in range(n1):
            nums2 = search_binary_insert(nums2, nums1[i])
        n2 = len(nums2)
        return nums2[n2 // 2] if n2 % 2 != 0 else (nums2[n2 // 2] + nums2[n2 // 2 - 1]) / 2

nums1 = [1,3]
nums2 = [2]
print(search_median(nums1, nums2))