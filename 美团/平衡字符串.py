##平衡字符串的定义是：字符串内只有两种字符，且两个字符的数量相等。现在给你一个字符串，请你找出所有可能的平衡字符子串。这个子串是原字符串从左到右取的若干字符，可以不连续。
from typing import List
def test(s: str) -> List[str]:
    result = []
    char_count = {}
    balanced_string = set()
    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        for before_char in char_count:
            if before_char != char and char_count[char] == char_count[before_char]:
                balanced_string.add((before_char, char))
    for char in balanced_string:
        for i in range(char_count[char[0]]):
            result.append(char[0] * (i + 1) + char[1] * (i + 1))
    return result

s = 'aabbcc'
print(test(s))
                
