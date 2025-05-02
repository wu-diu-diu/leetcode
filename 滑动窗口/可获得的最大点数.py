from typing import List
## 给定一个整数数组 cardPoints 和一个整数 k ，表示从数组的两端取出 k 张牌。
## 你的目标是最大化从中获得的点数。
## 你可以从数组的开头或末尾取牌，具体情况如下：
## 1. 从数组的开头取牌
## 2. 从数组的末尾取牌
## 3. 你不能从数组中间取牌
## 4. 你必须从数组的两端取出 k 张牌。

## 逆向思维，因为只能从开头和末尾取牌，取出k张牌之后，剩余的牌一定是连续的，则找到k张牌的最大值，等价于找到所有剩余连续的牌的最小值。
def maxScore_1(cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = 0
        min_sum = float('inf')
        if n == k: return sum(cardPoints)
        for i, num in enumerate(cardPoints):

            # 1.入
            s += num

            if i < n - k - 1:
                continue

            # 2.找到最小值
            if s < min_sum:
                min_sum = s

            # 3.出
            s -= cardPoints[i + 1 - n + k]
        
        a = sum(cardPoints)
        return a - min_sum

## 正向思维，直接从开头和末尾取
## 第一次取前k张，第二次取前k-1张+最后一张，第三次取前k-2张+最后两张，...，第k次取前0张+最后k张
def maxScore_2(cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_sum = float('-inf')
        ans = 0
        if n == k: return sum(cardPoints)
        for i in range(k + 1):
            x1 = sum(cardPoints[:k-i])  ## 前端取
            x2 = sum(cardPoints[-i:])  ## 末端取
            if i == 0:  ## 前端取k张时，这时cardPoints[-i:]是整个列表，所以要将x2置0
                 x2 = 0
            s = x1 + x2
            if s > max_sum:
                max_sum = s
            s = 0
        return max_sum

cardpoints = [1,79,80,1,1,1,200,1]
k = 3
print(maxScore_2(cardpoints, k))