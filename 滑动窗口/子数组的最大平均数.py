# 寻找子数组的最大平均数
# 给定一个由 N 个整数组成的数组 nums 和一个整数 k，返回 nums 中长度为 k 的子数组的最大平均数。任何多个整数的平均值（包括整数本身）都可以用浮点数表示。
# 示例 1:
# 输入: nums = [1,12,-5,-6,50,3], k = 4
# 输出: 12.75000
# 解释: 最大平均数是 (12 -5 -6 +50) / 4 = 51 / 4 = 12.75
def findMaxAverage(nums: list[int], k: int) -> float:
        average = 0
        sub_sum = 0
        ans = float('-inf')  # 有时候average会是负数，所以ans初始化为负无穷
        if len(nums) == 1: return nums[0]
        for i, num in enumerate(nums):
            # 进入
            sub_sum += num
            if i < k - 1:
                continue
            # 更新答案
            average = sub_sum / k
            ans = max(average, ans)

            # 出
            sub_sum -= nums[i + 1 - k]
        
        return ans