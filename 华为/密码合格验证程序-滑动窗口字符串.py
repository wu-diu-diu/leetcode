## 判断是否有连续的重复子串，使用变长的滑动窗口
def has_repeated_sub(x):
    repeated = 0
    for length in range(3, len(x) // 2):
        result = []
        for i in range(len(x) - length):
            s_sub = x[i:i + length]  ## 滑动窗口
            if s_sub not in result:
                result.append(s_sub)
            else:
                repeated = 1
    return repeated
        

while True:
    try:
        x = input()
        
        if len(x) < 8:
            print('NG')
            continue
        if has_repeated_sub(x):
            print('NG')
            continue
        num = 0
        up_char = 0
        lower_char = 0
        special = 0
        for char in x:
            if 48 <= ord(char) <= 57:  ## 判断是否有数字
                num = 1
            if 65 <= ord(char) <= 90:  ## 判断是否有大写字母
                up_char = 1
            if 97 <= ord(char) <= 122:  ## 判断是否有小写字母
                lower_char = 1
            ## 判断是否有特殊字符
            if 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord  (char) <= 126:
                special = 1
        if num + up_char + lower_char + special >= 3:  ## 以上四种包含三种则合格
            print('OK')
        else:
            print('NG')
    except:
        break