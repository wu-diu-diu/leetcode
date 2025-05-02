## 给定一个数组fruits，其中每个数表示结某种水果的树，可以任选一个树开始采摘，但只有两个篮子即只能装两种水果
## 求最多能采摘多少水果
## 本质上是滑动窗口内只能有两种数字，求窗口的最大长度
from collections import defaultdict, Counter

def totalFruit(fruits: list[int]) -> int:
    ddict = defaultdict(int)
    total = max_total = left = 0
    for i, fruit in enumerate(fruits):
        ddict[fruit] += 1 ## 存储窗口内某种树出现的次数
        total += 1  ## 存储窗口的长度即水果的数目
        while len(ddict) > 2:
            ## 滑出的某种树的出现次数减1
            ddict[fruits[left]] -= 1
            ## 如果减到0了，则将这种树去除
            if ddict[fruits[left]] == 0:
                ddict.pop(fruits[left])
            ## 左边界右移
            left += 1
            total -= 1
        max_total = max(max_total, total)
    return max_total
## 灵神解法
def totalFruit_2(fruits: list[int]) -> int:
        cnt = Counter()

        left = ans = 0
        for right, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans

fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(totalFruit(fruits))