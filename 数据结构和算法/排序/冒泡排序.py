# 冒泡排序
# 内层循环结束后，最大的元素已经排到最后
# 外层遍历次数为n-1次，内层遍历次数为n-1,n-2,...,1次，平均是 n(n-1)/2 次，所以是 O(n^2)
# 稳定性：稳定，可能会改变相同元素的相对位置
# 空间复杂度是 O(1)
def bubble_sort(nums: list[int]):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if nums[j] > nums[j +1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

nums = [5, 2, 9, 1, 5, 6]
print(bubble_sort(nums))  # 输出: [1, 2, 5, 5, 6, 9]
