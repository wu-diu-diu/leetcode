from collections import defaultdict

def maxLengthSubstring(s: str) -> int:
    ## ddict中的元素表示滑动窗口包含的元素
    ddict = defaultdict(int)
    cur_len = max_len = 0
    left = 0
    for ch in s:
        ## 随着滑动窗口右边界的移动，遇到新的元素为ch且内部ch这个元素已经出现两次，则不符合题目要求：最多出现两次
        ## 此时滑动窗口左边界需要右移
        while ddict[ch] == 2: 
            ddict[s[left]] -= 1  ## 滑出的元素出现次数减1
            left += 1  ## 左边界右移动
            cur_len -= 1  ## 长度减1
        ddict[ch] += 1  ## 新滑入的元素计数加1
        cur_len += 1  ## 长度加1
        if cur_len > max_len: max_len = cur_len
    return max_len

s = 'bcbbbcba'
print(maxLengthSubstring(s))