## 输入一个字符串，按照三个规则排序：
# ∙按照字母表中的顺序排序（不区分大小写）；
# ∙同一字母的大小写同时存在时，按照输入顺序排列；
# ∙非字母字符保持原来的位置不参与排序；
# 示例：abAB -> aAbB
## 知识点：字符串的isalpha函数，sorted函数，双指针法
# s原字符串，b字符串中所有的字母，统统大写再ascii码排序后，d：返回的结果
# 双指针遍历s和b，s中是字母的位置，将b中对应字母加到d中，s中不是字母的位置，将s中的非字母加到d中
while True:
    try:
        s = input()
        a = ''
        ## for循环结束之后将s中所有的字母都按原来的顺序提取了出来
        for i in s:
            if i.isalpha():  ## 如果字符是字母(大写小写都行),则返回True，否则返回false
                a += i
        ## 将字符串都转换成大写去比较，然返回一个排序后的字符列表，排序后的结果仍然保持原始字符的大小写
        b = sorted(a, key=str.upper)
        index = 0
        d = ''
        for i in range(len(s)):
            ## 如果原字符串的该位置是字符，则将排序后的字符插入
            if s[i].isalpha():
                d += b[index]
                index += 1
            ## 如果原字符串的该位置不是字符，则将非字符插入
            else:
                d += s[i]
        print(d)
    except:
        break