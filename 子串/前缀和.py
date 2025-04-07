## s[0] = 0 ，定义这个是为例
## s[1] = nums[1], s[2] = nums[1] + nums[2]
## 则nums一共有n + 1个前缀和，则任意子数组都可以判定为两个前缀和的差
## 如果不定义s[0] = 0,则s = [-2,-2,1,-4,-2,-3] [2,5]内所有元素之和为s[right] - s[left - 1]，那么当left = 0时
## 就需要特殊处理
class NumArray:
    def __init__(self, nums: list[int]):
        s = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            s[i + 1] = s[i] + v
        self.s = s
    def sunRange(self, left: int, right: int) -> int:
        return  self.s[right + 1] - self.s[left]
    
numarray = NumArray([-2,0,3,-5,2,-1])
print(numarray.sunRange(2, 5))