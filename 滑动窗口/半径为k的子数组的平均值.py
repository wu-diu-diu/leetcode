def getAverages(nums: list[int], k: int) -> list[int]:
        ans = []
        s = a = 0
        l = len(nums)
        if l == 1 and k == 0: return nums
        if l == 1 and k!= 0: return [-1]
        for i in range(l):
            if i < k or i + k >= l:
                ans.append(-1)
                continue
            s = sum(nums[i-k:i+k+1])  ## 这里的sum是O(n)的复杂度，时间复杂度会很高
            a = s // (2 * k + 1)
            ans.append(a)
        return ans

def getAverages(nums: list[int], k: int) -> list[int]:
        ans = [-1] * len(nums)
        s = 0
        if k == 0: return nums
        for i, n in enumerate(nums):
            # 入
            s += n
            if i < 2 * k:
                continue
            # 计算均值
            ans[i - k] = s // (2 * k + 1)
            # 出
            s -= nums[i - 2 * k]
        return ans