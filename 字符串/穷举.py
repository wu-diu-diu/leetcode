## 给定一个数，找到1到n中有多少个数包含7或者是7的倍数
while True:
    try:
        n = int(input())
        c = 0
        for i in range(1,n+1):
            if i % 7 == 0:
                c += 1
            elif str(i).count('7') > 0 :
                c += 1
        print(c)
    except:
        break