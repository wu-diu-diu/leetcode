## 简单解法
def test(s: str) -> int:
        length = len(s)
        result = []
        for i, char in enumerate(s):
            lst = []
            lst.append(char)
            if length == 1:
                 return 1
            for j in range(i+1,length):
                if s[j] not in lst:
                    lst.append(s[j])
                else:
                    result.append(len(lst))
                    break
                result.append(len(lst))
        if result:
            return max(result)
        else:
            return 0
##滑动窗口解法
def test2(s: str) -> int:
        if not s:return 0
        left = 0 ## 滑动窗口左指针
        max_len = 0
        cur_len = 0
        result = set()
        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[left])
                left += 1
                cur_len -= 1
            result.add(s[i])
            cur_len += 1
            if cur_len > max_len: max_len = cur_len
        return max_len

print(test2('abcabcbb'))  # 3
print(test(' '))
print(test(''))
print(test('au'))