## 给定一个数组，寻找所有的和为0的三元组，可以是不连续的
## 三循环当然可以求解可是时间复杂度太高
## 我们可以用空间换时间，将数组排序后得到一个新的数组。这样三指针求和之后，可以根据和的大小来决定指针移动的方向
## 最外面一个for循环遍历数组的每一个元素，即试图为为每一个元素都找一个满足要求的三元组，这样只遍历一次数组。
from typing import List
## 双指针法，或者叫三指针法，要得到三数之和，先将数组排序后再移动指针
## i是从0开始遍历数组， left和right分别指向i之后的第一个数和数组末尾
## 
def test(nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    length = len(sorted_nums)
    left = right = 0
    result = []
    for i in range(length - 2):
        left = i + 1
        right = length - 1
        ## 避免i出现重复，若i出现重复，则left和right两个指针会指向相同的值，从而得到相同的三元组
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]: continue
        while left < right:
            sum_nums = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

            if sum_nums == 0:
                result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                left += 1
                right -= 1
                ## 避免left和right移动后出现重复
                while left < right and sorted_nums[left] == sorted_nums[left - 1]: left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]: right -= 1
            ## 由于数组是从小到大排好序的，则三数之和若小于0，则左指针向右移，寻找更大的数
            elif sum_nums < 0:
                left += 1
            ## 同理，右指针向左移寻找更小的数
            elif sum_nums > 0:
                right -= 1
    return result
## 三循环暴力解法  有bug
def test2(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    length = len(nums)
    result = []
    for i in range(length - 2):
        if i == 0 or nums[i] != nums[i - 1]:
            for j in range(i + 1, length - 1):
                if j == 0 or nums[j] != nums[j - 1]:
                    for x in range(j + 1, length):
                        if x == 0 or nums[x] != nums[x - 1]:
                            sum_nums = nums[i] + nums[j] + nums[x]
                            if sum_nums == 0:
                                result.append([nums[i], nums[j], nums[x]])
    return result


nums = [-1,0,1,2,-1,-4]
nums2 = [0,0,0,0,0,0,0,0,0,0,0,0]
nums3 = [0,0,0]
print(test2(nums))