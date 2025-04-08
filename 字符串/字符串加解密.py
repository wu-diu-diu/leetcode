# 小写字母按字母表顺序后移一位，变成大写字母，大写字母按字母表顺序后移一位，变成小写字母，数字按数字表顺序后移一位，变成数字 'Z' -> 'a', 'z' -> 'A', '9' -> '0'
## 输入：abcdefg1  加密
#        0BCDEFGH  解密
## 输出：BCDEFGH2
#        abcdefg2
# 我这个方法太笨拙了
def jiami(x: str) -> str:
    result = ""
    for char in x:
        if char.islower() and char is not "z":
            result += chr(ord(char) - 32 + 1)
        if char == "z":
            result += "A"
        if char.isupper() and char is not "Z":
            result += chr(ord(char) + 32 + 1)
        if char == "Z":
            result += "a"
        if char.isnumeric() and char is not "9":
            result += chr(ord(char) + 1)
        if char == "9":
            result += "0"
    return result


def jiemi(y: str) -> str:
    result = ""
    for char in y:
        if char.islower() and char is not "a":
            result += chr(ord(char) - 32 - 1)
        if char == "a":
            result += "Z"
        if char.isupper() and char is not "A":
            result += chr(ord(char) + 32 - 1)
        if char == "A":
            result += "z"
        if char.isnumeric() and char is not "0":
            result += chr(ord(char) - 1)
        if char == "0":
            result += "9"
    return result

# while True:
#     try:
#         x = input()
#         y = input()
#         jiami_x = jiami(x)
#         jiemi_y = jiemi(y)
#         print(jiami_x)
#         print(jiemi_y)
#     except:
#         break

## 这里提前将加解密的映射关系写好，当字符串a输入进来后，直接将a的每一个字符按照映射关系加密或者解密
def check(a,b):
    ## L1 and L2 是互为映射的关系
    L1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    L2 = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
    result = ""
    if b == 1:
        for i in a:
            result += L2[L1.index(i)]
    elif b == -1:
        for i in a:
            result += L1[L2.index(i)]
    return result
while True:
    try:
        print(check(input(),1))
        print(check(input(), -1))

    except:
        break