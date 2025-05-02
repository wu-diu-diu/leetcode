# 书店老板开店n分钟，顾客在前n分钟到达，老板在前m分钟生气，老板生气时顾客不满意
# 你可以选择m分钟内的任意连续的时间段让老板不生气，求最多顾客满意的人数
from typing import List
# 时间复杂度有点高
# 遍历customers，得到所有的可能的连续的老板不生气的时间段，得到新的grumpy数组，遍历新的grumpy数组，得到满意的顾客数，取最大值
# 这个方法的时间复杂度是O(n^2)，空间复杂度是O(n)
def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = 0
        ans = float('-inf')
        for i, num in enumerate(customers):

            if i < minutes - 1:
                continue
            if i == minutes - 1:
                grumpy_sub = [0] * minutes + grumpy[i+1:]
            else:
                grumpy_sub = grumpy[:i+1-minutes] + [0] * minutes + grumpy[i+1:]

            for j, num in enumerate(grumpy_sub):
                if num == 0:
                     s += customers[j]
            if s > ans:
                ans = s
            s = 0
        return ans

## 灵神解法
## 这个解法是对第三种方法的进一步优化，将解法3的两个for循环整合到了一起
def maxSatisfied_2(customers: List[int], grumpy: List[int], minutes: int) -> int:
    ## 第一个元素存储满意顾客数，遍历完后会存储所有满意的顾客数
    ## 第二个元素存储不满意的顾客数，使用一个窗口，维护窗口的大小为minutes，求窗口内不满意顾客数的最大值
    s = [0, 0]
    max_s1 = 0
    for i, (c, g) in enumerate(zip(customers, grumpy)):
        s[g] += c
        if i < minutes - 1:  # 窗口长度不足 minutes
            continue
        max_s1 = max(max_s1, s[1])
        ## 因为s[1]存储的是不满意顾客数，所以这里只有在离开窗口的元素是不满意顾客时才会减去这个元素
        if grumpy[i - minutes + 1]:
            s[1] -= customers[i - minutes + 1]  # 窗口最左边元素离开窗口
    return s[0] + max_s1


## 题解解法
def maxSatisfied_3(customers: List[int], grumpy: List[int], minutes: int) -> int:
    s = 0
    n = len(customers)
    max_a = 0
    ## 先计算满意的顾客数，并将customers中满意的顾客数置为0，因为已经加过一次了
    for i in range(n):
        if grumpy[i] == 0:
            s += customers[i]
            customers[i] = 0
    ## 在滑动窗口中，不满意的顾客也会变得满意，又因为我们已经将满意顾客置0，所以实际上就是计算窗口中不满意顾客数的最大值
    ## 使用滑动窗口的模板即可
    a = 0
    for j in range(n):

        a += customers[j]

        if j < minutes - 1:
            continue

        max_a = max(max_a, a)

        a -= customers[j - minutes + 1]
    ## 最后将满意的顾客数和窗口中不满意顾客数的最大值相加即可
    ## 这里的max_a就是窗口中不满意顾客数的最大值，因为在窗口中，不满意也会变得满意，因为老板在窗口内生气也会变得不生气
    return s + max_a



customers = [1,0,1,2,1,1,7,5]
minutes = 3
grumpy = [0,1,0,1,0,1,0,1]
print(maxSatisfied_2(customers, grumpy, minutes))