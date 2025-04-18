DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 元组的集合，表示方向向量，四个方向，由于方向向量是固定的所以使用元组，占用空间小

def test(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix), len(matrix[0]) # 获取矩阵的行数和列数
    ans = [] # 初始化一个空数组，存储结果
    i = j = di = 0

    for _ in range(m * n):
        ans.append(matrix[i][j])
        matrix[i][j] = None # 将当前元素标记为已访问
        ## di表示当前的方向，di=0表示向右，di=1表示向下，di=2表示向左，di=3表示向上
        # 计算下一个位置
        ni, nj = i + DIRS[di][0], j + DIRS[di][1]
        if ni < 0 or ni >= m or nj < 0 or nj >= n or matrix[ni][nj] is None:
            di = (di + 1) % 4  ## 改变方向，顺时针旋转90度
        i, j = i + DIRS[di][0], j + DIRS[di][1]
    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(test(matrix))  # 输出: [1, 2, 3, 6, 9, 8, 7, 4, 5]