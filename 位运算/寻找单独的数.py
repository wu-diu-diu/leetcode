## 位运算 0 异或 任何数等于任何数
## 异或：同为0，异为1
## 1 ^ 2 ^ 2 = 1 
## 某个数异或两次另一个数，结果仍等于该数，使用这个特性可以找到数组中单独的数
def test(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res 