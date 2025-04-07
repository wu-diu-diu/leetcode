## 给定一个有序数组，内包含重复元素，给定一个目标值之后，若目标值存在于序列中，返回目标值的起始索引，若没有目标值返回[-1,-1]
def searchRange(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    result = []
    flag = False
    for i in range(2):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:  ## 找到目标值
                flag = True  ## 标志位，标志找到目标值
                if i == 0:
                    right = mid - 1  ## 第一次让right向左移动，最终left的位置则为起始索引
                else:
                    left = mid + 1  ## 第二次让left向右移动，最终right的位置则为结束索引
        if flag:
            result.append(left) if i == 0 else result.append(right)
        else:  ## 没有找到则返回-1
            return [-1, -1]
    return result

nums = [5,7,7,8,8,10]##
target = 6
print(searchRange(nums, target))
    