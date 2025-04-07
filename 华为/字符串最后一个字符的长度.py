import sys


for line in sys.stdin:  ## 逐行读取标准输入，不停读取

    line = line.strip()
    if not line:  ## line为空即 line=''时，跳过本次循环，继续下一次循环，即继续下一个输入
        continue
    x = line.split(' ')  ## 以空格为分隔符，将line分割成一个list
    if x:
        print(len(x[-1]))
        
## 使用input()输入只能输入一行

# x = input()
# x = x.split(' ')  ## 以空格分割字符串形成列表
# print(len(x[-1]))