## 查找兄弟单词，这个就是字母异位词，使用哈希表
## 兄弟单词即一个字符串内的字符所有可能的排列方式，但是不包括字符串本身
## 如何判断一个字符是否是另一个字符的兄弟单词，可以将字符串排序后比较二者是否相等
## 或者使用counter函数，将字符串转化为字典，比较两个字典是否相等
from collections import Counter

while True:
    try:
        z = input().split()
        length = int(z[0])
        bro = z[1:-2]
        x = z[-2]
        x_len = len(x)
        if x_len == 1:
            print(0)
            break
        bro = [item for item in bro if len(item) == x_len]
        counter_x = Counter(x)
        index = int(z[-1])
        result = []
        for string in bro:
            if string == x:
                continue
            counter_bro = Counter(string)
            if counter_bro == counter_x:
                result.append(string)
        ## 使用 sorted 函数对包含字符串的列表进行排序时，排序的依据是字符串的字典序
        result = sorted(result)
        print(len(result))
        print(result[index-1])
    except:
        break