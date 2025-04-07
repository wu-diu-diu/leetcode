## 将命令行输入的十六进制转换位十进制
## 输入： 0xFA93
## 输出： 64147 = 16^3 * 15 + 16^2 * 10 + 16^1 * 9 + 16^0 * 3

## MY-method
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     length = len(line)
#     e = 0 ## 指数位
#     result = 0
#     for i in range(length - 1, 1, -1):  ## 从最后一位开始，遍历到倒数第三位 5 4 3 2 因为最后两位0x不需要计算
#         try:
#             num = int(line[i])  ## 从后开始计算，每一位的值乘以16的指数次方
#             result += num * 16 ** e
#             e += 1  ## 指数位加1
#         except:  ## int('A')会报错，所以遍历到字母时会跳到except
#             num = ord(line[i]) - 55  ## 'A'对应的ASCII码为65，'A'对应的十六进制数为10，所以需要减去55
#             result += num * 16 ** e
#             e += 1
#     print(result)


## Other-method
# x = input()
# print(int(x, 16))  ## int()函数第二个参数表示进制，这里是16进制

## 两种方法的区别在于第一种方法是手动计算，第二种方法是直接调用int()函数，第二种方法更简洁
## 第三种
# while True:
#     try:
#         x = input()
#         final = 0
#         dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
#         for i in range(2, len(x)):
#             final += dic[x[i]] * 16 ** (len(x) - i - 1)
#         print(final)
#     except:
#         break
