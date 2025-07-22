# 测试用例
# 1
# 3 3
# 7 3 2
# 5 1 9
# 6 8 4

import sys
import random
T = int(sys.stdin.readline().strip())

tmp = sys.stdin.readline().strip().split()
n, m = int(tmp[0]), int(tmp[1])
matrix = []

for _ in range(n):
    tmp_list = [int(num) for num in sys.stdin.readline().strip().split(" ")]
    matrix.append(tmp_list)

dp = [[0] * m for _ in range(n)]
dp[0][0] = matrix[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            ## 第0行的每个元素只能是通过向右走走到这里的，所以和左边的上一个元素进行与运算
            dp[i][j] = dp[i][j] & dp[i][j - 1]
        if j == 0:
            ## 第0列的每个元素只能是通过向下走走到这里的，所有和上边的上一个元素进行与运算
            dp[i][j] = dp[i][j] & dp[i - 1][j]
        else:
            ## 不是第0行和第0列的元素，就找他的上边的元素和左边的元素的与运算的最大值
            dp[i][j] = max(dp[i][j] & dp[i - 1][j], dp[i][j] & dp[i][j -1])
            ## 所以dp数组每个位置的值保存的是当到达当前位置时，进行与运算的结果的最大值，那么我们一直求，直到求出右下角元素的值，就可以直到从左上角到右下角的与运算最大值，同时也知道了从左上角到任何一个点的与运算的结果的最大值

print(dp[n - 1][m - 1])

