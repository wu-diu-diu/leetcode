s1 = [3,4,5,6,7]
s2 = [1,2,3,4,5]
s3 = [1,3,5,7,9]
s4 = [2,4,6,8,10]
## 归并排序分为分解和合并两个阶段，这里的思想可以用于合并阶段
## 逆向双指针的思想
def merge(s1:list[int], s2:list[int]) -> list[int]:
    p1 = len(s1) - 1
    p2 = len(s2) - 1

    p = len(s1) + len(s2) - 1
    s1 = s1 + len(s2) * [0]  ## 扩充s1数组
    while p1 >= 0 and p2 >= 0:
        if s1[p1] > s2[p2]:
            s1[p] = s1[p1]
            p1 -= 1
        elif s1[p1] < s2[p2]:  # 严格小于时取s2
            s1[p] = s2[p2]
            p2 -= 1
        else:                  # 相等时只取一个，跳过另一个
            s1[p] = s1[p1]
            p1 -= 1
            p2 -= 1
        p -= 1

    while p2 >= 0:
        s1[p] = s2[p2]
        p -= 1
        p2 -= 1
    # 如果p大于零，则说明两个数组中有重合的元素，合并后的数组的长度 < 两个数组长度之和
    return s1[p+1:] if p > 0 else s1

print(merge(s3,s4))
    
    