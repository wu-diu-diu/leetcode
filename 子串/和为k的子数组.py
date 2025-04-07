## 暴力解法，当nums很长时，会非常耗时
## 时间复杂度为n2
def subarraySum(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        left, right = i, i + 1
        while right <= n:
            sub_sum = sum(nums[left:right])
            if sub_sum == k:
                count += 1
            right += 1
    return count

from collections import defaultdict
def subArraySum(nums: list[int], k: int) -> int:
    s = [0] * (len(nums) + 1)
    ## 前缀和
    for i, v in enumerate(nums):
        s[i + 1] = s[i] + v
    dic = defaultdict(int)  ## 当key在字典中不存在时，defaultdict会提供一个默认值，这里由于参数是int，所以默认值是0
    result = 0
    ## sj -si = k则si = sj - k 且i < j如果我们遍历sj，同时保存sj出现的次数，那么对于每一个sj，dic[sj-k]则为sj之前满足sj-si=k的si的次数
    ## 即为nums[j+1]之前所有子串之和满足k的个数
    for sj in s:
        ## 和两数之和很像，换成了两数之差
        ## 以下两行代码顺序不能互换是考虑到k=0时，nums=[2],互换则会发生错误
        result += dic[sj - k]  ## 如果sj-k在字典中，也即si，则会返回其出现的次数，有几次则说明有几个si满足sj-si = k,即sj左侧几个子数组之和为k
        dic[sj] += 1  ## 记录前缀和sj出现的次数

## 求两数之和，我们可以用双层循环暴力求解，但是如果使用哈希表，保存num之前所有的数，当target-num在哈希表中时，则说明二者之和满足要求
def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - nums
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i    
## defaultdict可以用来计数
def count_char(s: str, target: str) -> int:
    d = defaultdict(int)
    for char in s:
        d[char] += 1
    return d[target]
s = 'qwertyuiqwqwqw'
target = 'q'
print(f"{s} 有 {count_char(s, target)} 个 {target}")
nums = [1,1,1]
k = 2
print(subarraySum(nums, k))