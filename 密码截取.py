## 找到一个字符串内最大的回文串
## 暴力解法，时间复杂度是n2
while True:
    try:
        str = input()
        n = len(str)
        list = []
        for i in range(0,n-1):
            for j in range(1,n):
                ## 第一个条件目的是找到回文串的两端
                ## 第二个条件是判断两端中中间的字符串正着读和反着读是否相等，若相等，则是回文串
                ## [i+1:j]取出i+1到j-1之间的字符串，不包括j
                ## [j-1:i:-1]从右往左取出j-1到i+1之间的字符串，不包括i
                if str[j] == str[i] and str[i+1:j] == str[j-1:i:-1]:
                    list.append(len(str[i:j+1]))
        print(max(list))
    except:
        break



while True:
    try:
        x = input()
        length = len(x)
        max_len = 0
        ## 对于每一个字符，检测两次，第一次检测其是否是ABA型回文串的中心
        ## 第二次检测其是否是ABBA型回文串的中心左边一格的字符
        for i in range(length):
            k = i - 1
            j = i + 1
            ABA_len = 1
            while k >= 0 and j < length:
                if x[k] == x[j]:
                    k -= 1
                    j += 1
                    ABA_len += 2
                else:
                    break

            k = i
            j = i + 1
            ABBA_len = 0
            while k >= 0 and j < length:
                if x[k] == x[j]:
                    k -= 1
                    j += 1
                    ABBA_len += 2
                else:
                    break
            now_len = max(ABA_len, ABBA_len)
            if now_len > max_len:
                max_len = now_len
        print(max_len)
    except:
        break