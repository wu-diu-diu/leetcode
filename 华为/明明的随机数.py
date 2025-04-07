# import sys
# result = []
# first_input = None
# for line in sys.stdin:
#     line = int(line.strip())  ## 在终端输入一个数按下空格则赋值给line: '3\n'，再输入一个数按下空格：'2\n'直到按住ctrl+z再按回车结束输入,所以这里需要去掉尾部换行符再转换为整数
#     if first_input == None:  ## 第一个数表示随机数的个数，不能添加到结果中，这里相当于一个标志位
#         first_input = line
#         continue

#     if line not in result:  ## 去重
#         result.append(line)
# result = sorted(result)

# for num in result:
#     print(num)

# ##输入
# 3
# 2
# 2
# 1
# ##输出
# 1
# 2

while True:
    lst = []
    try:
        num = int(input())  ## input()返回的是字符串不包含换行符
        for i in range(num):
            lst.append(int(input()))
        test_set = set(lst)
        lst = list(test_set)
        lst.sort()
        for i in lst:
            print(i)
    except:
        break