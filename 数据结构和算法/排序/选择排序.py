# 选择排序
# 时间复杂度是 O(n^2)，外循环是n-1次，内循环逐渐减少，平均是 n/2 次，所以是 O(n^2)
# 稳定性：不稳定，可能会改变相同元素的相对位置
# 空间复杂度是 O(1)
def selection_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

