## 将x从ip地址转换为10进制
## 将y从10进制转换为ip地址
## 字符串处理

while True:
    try:
        x = list(map(int, input().split('.')))
        y = int(input())
        result_x = ''
        for num in x:
            num = bin(num)[2:]  ## 不要0b
            num = '0' * (8 - len(num)) + num  ## 不足8位的补0
            result_x += num
        y = bin(y)[2:]
        if len(y) != 32:  ## 不足32位的补0
            y = '0' * (32 - len(y)) + y
        result_y = []
        for i in range(0, 32, 8):
            num = y[i:i+8]
            num = int(num, 2)
            result_y.append(num)
        print(int(result_x, 2))
        print('.'.join(str(num) for num in result_y))
    except:
        break