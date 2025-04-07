## 以下代码可以找到一个序列中的最长不连续子序列
## 想法是从左往右找到每个元素开头的最长不连续子序列，然后从右往左找到每个元素结尾的最长不连续子序列，最后将两个结果相加，取最大值再减去1即为最终结果
import math
# while True:
#     try:
#         num = int(input())
#         height = list(map(int, input().split()))
#         result_left = []
#         result_right = []
#         for i in range(num - 1):  ## 只搜索到序列的倒数第二个元素
#             max_count = 0
#             left = i
#             right = left + 1
#             count = 1
#             while True:
#                 if right == num:
#                     break
#                 if height[right] > height[left]:
#                     left = right
#                     count += 1
#                 right += 1
#             if count > max_count:
#                 max_count = count
#             result_left.append(max_count)
#         for i in range(num - 1, 0, -1):  ## 只搜索到序列的第二个元素
#             max_count = 0
#             right = i
#             left = right - 1
#             count = 1
#             while True:
#                 if left == -1:
#                     break
#                 if height[left] > height[right]:
#                     right = left
#                     count += 1
#                 left -= 1
#             if count > max_count:
#                 max_count = count
#             result_right.append(max_count)
#         print(result_left)
#         print(result_right)
#         result = list(map(lambda x, y: x + y, result_left, result_right))
#         print(num - (max(result) - 1))
#     except:
#         break


import bisect
##计算以每个元素结尾的最长递增子序列的长度
def inc_max(l):
    dp = [1]*len(l) # 初始化dp，最小递增子序列长度为1
    arr = [l[0]] # 创建数组
    for i in range(1,len(l)): # 从原序列第二个元素开始遍历
        if l[i] > arr[-1]:
            arr.append(l[i])
            dp[i] = len(arr)
        else:
            ##使用二分法找到第一个比l[i]大的元素的位置后，这个元素的序号是多少，就是有前面有多少个元素比l[i]小，再加上l[i]自己
            ## 就是以l[i]结尾的最长递增子序列的长度
            pos = bisect.bisect_left(arr, l[i]) # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
            arr[pos] = l[i]
            dp[i] = pos+1
    return dp
 
while True:
    try:
        N = int(input())
        s = list(map(int, input().split()))
        left_s = inc_max(s) # 从左至右
        right_s = inc_max(s[::-1])[::-1] # 从右至左
        sum_s = [left_s[i]+right_s[i]-1 for i in range(len(s))] # 相加并减去重复计算
        print(str(N-max(sum_s)))
    except:
        break