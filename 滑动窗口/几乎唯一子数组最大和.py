# 几乎唯一子数组最大和
# 给你一个整数数组 nums 和两个正整数 m 和 k
# 你需要从 nums 中选择一个子数组，子数组的长度为 k ，并且子数组中至少有 m 个不同的值。
# 请你返回子数组的最大和。
# 如果没有这样的子数组，请你返回 0 。
# 示例 1：输入：nums = [1,2,3,4,5], m = 2, k = 3 输出：12
# 解释：子数组 [3,4,5] 中有 3 个元素，至少有 2 个不同的值。
def maxSum(nums: list[int], m: int, k: int) -> int:
        s = 0
        l = []
        ans = float('-inf')
        flag = 0
        for i, num in enumerate(nums):
            # 入
            s += num
            l.append(num)
            
            if i < k - 1:
                continue
            
            if len(set(l)) >= m:
                flag = 1
                ans = max(ans, s)
            
            # 出
            s -= nums[i + 1 - k]
            l.pop(0)

        return ans if flag else 0    