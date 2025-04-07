def test(lst: list[int], target: int) -> int:
    n = len(lst)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            return mid
    return left

nums = [1,3,5,6]
target = 8
print(test(nums, target))