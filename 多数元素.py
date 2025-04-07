from collections import Counter

def test(nums: list[int]) -> int:
    y = Counter(nums)
    ## 返回值最大的键
    ## 这里使用了max方法的key参数，这个参数是一个函数，这个函数的作用是对每个元素进行处理，返回一个值，然后max方法根据这个值来比较大小
    ## 这里的lambda函数的作用是返回y[x]，也就是返回x这个键对应的值，也就是这个键出现的次数
    ## 这里的x默认是y的键
    return max(y, key=lambda x: y[x])

## 如果我想返回键最大的值
# max_value = my_dict[max(my_dict.keys())]