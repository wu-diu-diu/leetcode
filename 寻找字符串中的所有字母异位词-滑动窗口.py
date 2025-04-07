from typing import List
## mysolution
## sorted的时间复杂度是O(nlogn) 每个字串都进行了排序操作，一共有n-m+1个子串，n是s的长度，m是p的长度, 每个字串排序的复杂度是mlogm
## 所以时间复杂度是O((n-m+1)*mlogm)较高
def test(s: str, p: str) -> List[int]:
    len_p = len(p)
    len_s = len(s)
    p = sorted(p)  ## 这里不能用set，因为set会把p中的重复元素去掉，比如p = 'aab', 子串为'bba',二者的集合是相等的，但是明显'bba'不是'aab'的的异位词
    result = []
    for i in range(len_s - len_p + 1):
        s_sub = s[i:i+len_p]
        s_sub = sorted(s_sub)
        if s_sub == p:
            result.append(i)
    return result

## kimi解法
from collections import Counter
def test2(s: str, p: str) -> List[int]:
    len_p = len(p)
    len_s = len(s)
    p_counter = Counter(p)
    result = []

    for i in range(len_s - len_p + 1):
        window_counter = Counter(s[i:i+len_p])
        if window_counter == p_counter:
            result.append(i)
    return result


s = 'abab'
p = 'ab'
print(test2(s, p))