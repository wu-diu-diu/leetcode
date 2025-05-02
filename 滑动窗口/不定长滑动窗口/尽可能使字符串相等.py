## 两个字符串s和t，长度相同，给定一个最大代价maxCost
## 你可以将s中的字符替换为t中的字符，代价为两个字符的ASCII码之差的绝对值
## 求在代价之和小于给定的最大代价的前提下，s中可以替换的最长子串的长度，返回这个长度
## 例如s = "abcd", t = "bcdf", maxCost = 3， 返回3，因为可以将s中的前3个字符替换为t中的前3个字符，代价为1+1+1=3

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    cur_len = max_len = 0
    cost = 0
    left = 0
    for i in range(len(s)):

        cost += abs(ord(s[i]) - ord(t[i]))
        cur_len += 1

        while cost > maxCost:
            cur_len -= 1
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        max_len = max(max_len, cur_len)
    return max_len

s = 'abcd'
t = 'bcdf'
maxCost = 3
print(equalSubstring(s, t, maxCost))

        