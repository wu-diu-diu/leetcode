def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1  # 从右向左找第一个小于pivot的元素
        while i < j and nums[i] <= pivot:
            i += 1  # 从左向右找第一个大于pivot的元素
        # 交换两个元素的位置
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    # 将基准数放在两个指针交汇的位置
    nums[left], nums[i] = nums[i], nums[left]
    return i  # 返回基准数的位置

def quick_sort(nums: list[int], left: int, right: int):
    if left >= right:
        return
    pivot_index = partition(nums, left, right)
    quick_sort(nums, left, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, right)
    return nums

nums = [5, 2, 9, 1, 5, 6]
print(quick_sort(nums, 0, len(nums) - 1))  # 输出: [1, 2, 5, 5, 6, 9]