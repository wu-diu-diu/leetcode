# 得到k个黑色块的最少涂色次数
# 题目描述：给你一个字符串 blocks ，它只包含字符 'B' 和 'W' ，分别表示黑色和白色块。
# # 你可以给任意一个白色块涂成黑色块，或者给任意一个黑色块涂成白色块。
# # 你需要让所有连续的黑色块的数量 恰好 为 k 。
# # 请你返回至少需要涂色多少块白色块，才能使得连续的黑色块数量 恰好 为 k 。
# # 示例 1：输入：blocks = "WBBWWBBWBW", k = 7 输出：3
# 解释：你需要涂色 3 块白色块，才能得到连续的黑色块数量为 7
def minimumRecolors(blocks: str, k: int) -> int:
    s = ''
    cnt = 0
    ans = float('inf')
    for i, c in enumerate(blocks):
        # 入
        if c == 'W': # 如果滑进来的字符是白色块，则窗口内需要涂改的次数+1
            cnt += 1

        if i < k - 1: # 如果窗口还没有形成，继续滑动
            continue
        # 记录答案
        if cnt == 0: # 前k个字符即满足要求
            return 0
        else:
            ans = min(ans, cnt)  # 记录最小值
        
        # 出 如果滑出去的字符是白色块，则窗口内需要涂改的次数要减1
        if blocks[i + 1 - k] == 'W':
            cnt -= 1
    return ans