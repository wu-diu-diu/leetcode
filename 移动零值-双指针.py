from typing import List
## my method 双指针
## i指向要检查的数，flag标志是为例确保删除和插入元素时不会导致跳过遍历某个元素
## j保证遍历完length长度的数即停止，防止i在数组尾部不停的循环删除和插入无法结束程序
def movezero(nums: List[int]) -> None:
    flag = False
    length = len(nums)
    i = 0
    j = 0
    while i < length and j < length:
        if flag:
            flag = False
            i -= 1
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            flag = True
        i += 1
        j += 1

## 另一种方法，第一个for循环将所有非零值都按照出现顺序移动到左边，index是移动的索引
## 第二个for循环将数组剩下的右边都填充为0
def movezero2(nums: List[int]) -> None:
    length = len(nums)
    index = 0
    for i in range(length):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, length):
        nums[i] = 0

## 官方解法
## 当右指针遇到非零，则和左指针互换数值，右指针一直往前移动，左指针只有和右指针互换值之后才会向右移动一格
## 则左指针左边都为非0值，右指针左边直到左指针都为0
def movezero3(nums: List[int]) -> None:
    n = len(nums)
    left = right = 0
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

nums = [0,0,1,5,0,12]
movezero3(nums)
print(nums)
