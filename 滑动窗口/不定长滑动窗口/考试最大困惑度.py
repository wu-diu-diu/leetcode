from collections import defaultdict
def test(string: str, k: int) -> int:
    left = 0
    res = 0
    my_dic = defaultdict(int)
    ## for循环控制窗口右边界，while控制窗口左边界
    ## 难点在于左边界向前运动的条件，即while循环的条件
    for right, char in enumerate(string):
        my_dic[char] += 1
        while my_dic['T'] > k and my_dic['F'] > k:
            my_dic[string[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res

string = 'TTFTTFTT'
print(test(string, 1))
