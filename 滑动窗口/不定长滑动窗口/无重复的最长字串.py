## 不定长滑动窗口
def LengthOflongestSubstring(s: str) -> int:
    if not s:return 0
    left = 0 ## 滑动窗口左指针
    max_len = 0
    cur_len = 0
    result = set()
    for i in range(len(s)):  ## for循环扩展滑动窗口又边界
        ## while循环扩展滑动窗口左边界 遇到重复字符，则左边界右移动，直到没有为止，这样保证滑动窗口内都是不重复的元素
        while s[i] in result:
            result.remove(s[left])
            left += 1
            cur_len -= 1
        result.add(s[i])
        cur_len += 1
        if cur_len > max_len: max_len = cur_len
    return max_len
        

s = 'abcabcbb'
print(LengthOflongestSubstring(s))
