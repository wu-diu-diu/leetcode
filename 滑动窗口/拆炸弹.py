# 给定一个循环数组code和整数k
# 如果k>0，返回code中每个元素的k个后继元素之和
# 如果k<0，返回code中每个元素的k个前驱元素之和
def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    if k == 0: return [0] * n
    ans = []
    code = code + code
    if k > 0:
        for i in range(1, n + 1):
            s = sum(code[i:i + k])
            ans.append(s)
    else:
        for i in range(n, 2 * n):
            s = sum(code[i + k:i])
            ans.append(s)
    return ans
## 使用滑动窗口
## k>0和k<0是一样的，只是滑动窗口的起点不同
## 循环可以用取余来解决
def decrypt_2(code: list[int], k: int) -> list[int]:
    n = len(code)
    ans = [0] * n
    r = k + 1 if k > 0 else n  ## 滑动窗口起始位置的右端点
    ## 无论k>0还是k<0，窗口的长度都是|k|
    k = abs(k)
    s = sum(code[r - k:r])  ## ans[0]即ans的第一个元素，第一个滑动窗口的和
    for i in range(n):
        ans[i] = s
        s = s + code[r % n]
        s = s - code[(r - k) % n]
        ## 右端点不断加1
        r += 1
    return ans


code = [2,4,9,3]
k = -2
print(decrypt_2(code, k))
