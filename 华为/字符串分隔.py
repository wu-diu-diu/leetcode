# ## 将一个字符串分割成多个长度为8的字符串，然后输出，如果不足8位，则补0输出
import sys
import math
for line in sys.stdin:
    line = line.strip()
    times = math.ceil(len(line) / 8)  ## 除法向上取整
    for i in range(times):
        if len(line) < 8:
            output = line + '0' * (8 - len(line))
            print(output)
            break
        output = line[:8]
        line = line[8:]
        print(output)

## 输入 'hellocoder'
## 输出
#  'hellocod'
#  'er000000'

# x = input()
# for i in range(0, len(x), 8):
#     # print(x[i:i+8])  ## 第二次i=8时候，8+8会超出数组长度
#     print(x[i:i+8].ljust(8, '0'))  ## ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
# ljust() 是 Python 中字符串的一个内置方法，用于将字符串左对齐并填充到指定的宽度。如果字符串的长度小于指定的宽度，它会在字符串的右侧填充指定的字符（默认为空格），
# 以达到指定的宽度；如果字符串的长度大于或等于指定的宽度，则返回原始字符串