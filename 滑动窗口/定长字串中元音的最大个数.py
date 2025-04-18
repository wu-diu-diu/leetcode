# 给定一个字符串 s 和一个整数 k，返回字符串中最多有多少个元音字母的子字符串的最大长度。
# 元音字母是 'a'，'e'，'i'，'o' 和 'u'。
# 暴力枚举所有字串时间复杂度太高，使用滑动窗口来优化
# 维护一个大小为k的窗口，对于每个进入窗口的字符判断其是否为元音，如果是则加1，离开窗口的字符判断其是否为元音，如果是则减1，更新答案
def maxVowels(s: str, k: int) -> int:
    ans = vowel = 0
    for i, c in enumerate(s):
        # 入
        if c in 'aeiou':
            vowel += 1
        if i < k - 1:
            continue
        # 更新答案
        ans = max(vowel, ans)
        # 离开
        if s[i + 1 - k] in 'aeiou':
            vowel -= 1
    return ans