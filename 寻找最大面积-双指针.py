## nums内每个数是一个高度为nums[i]的线条，求这个数组内能构成的最大的面积
## 暴力解法，时间复杂度是O(n²)
from typing import List
def test(nums: List[int]) -> int:
    result = []
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            height = min(nums[i], nums[j])
            longth = j - i
            area = height * longth
            result.append(area)
    return max(result)


## 双指针法，左指针从左边往右边移动，右指针从右边往左边移动，直到左右指针相遇则停止循环
## 计算每个指针对应的值的面积
## 移动值较小的那个指针，因为两个指针都是向内移动，则底边也就是宽必定会减小
## 此时若移动长板，长板增大，不变，减小都会导致面积减小
## 若移动短板，虽然底边变小，但若短板边长，则面积有可能会增大，所以移动短板是正确的
## 木桶能装多少水是由短板决定的
def test_1(nums: List[int]) -> int:
    left = 0
    length = len(nums)
    right = length - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(nums[left], nums[right])
        if area > max_area:
            max_area = area
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return max_area

nums = [1,8,6,2,5,4,8,3,7]
nums2 = [1,1]
print(test_1(nums))