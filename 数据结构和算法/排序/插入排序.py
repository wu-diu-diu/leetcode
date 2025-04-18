# 插入排序
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# 稳定性：稳定，可能会改变相同元素的相对位置
def insertion_sort(nums: list[int]):
    n = len(nums)
    for i in range(1, n):
        base = nums[i] # 从第二个元素开始，第一个元素可视为已排序，比较base与其左侧的元素
        j = i - 1
        while j >= 0 and nums[j] > base:  ## 如果左侧的元素大于base，则将该元素右移一位
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = base
    return nums
