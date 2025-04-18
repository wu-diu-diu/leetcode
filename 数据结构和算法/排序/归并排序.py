# 归并排序
# 归并排序是一种有效的排序算法，采用分治法（Divide and Conquer）策略来排序。
# 它将数组分成两半，递归地对每一半进行排序，然后将两个已排序的半数组合并在一起。
# 归并排序的时间复杂度为O(n log n)，空间复杂度为O(n)。
# 归并排序是稳定的排序算法，适用于大规模数据的排序。
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid]) # 递归地对左半部分进行排序
    right_half = merge_sort(nums[mid:])

    return merge(left_half, right_half)

def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

nums = [5, 2, 9, 1, 5, 6]
print(merge_sort(nums))  # 输出: [1, 2, 5, 5, 6, 9]