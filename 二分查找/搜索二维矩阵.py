def search(nums: list[int], target: int) -> bool:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return True
    return False

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        if search(matrix[i], target):
            return True
    return False
## 灵神解法
## 由于矩阵的每一行是递增的，且每行的第一个数大于前一行的最后一个数，如果把矩阵每一行拼在一起，我们可以得到一个递增数组。
## 但不用真的将矩阵拼接成一个数组，只需要将这个递增数组的索引转化为矩阵的行索引和列索引就好了
def searchM_lin(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])  #行，列
    left, right = -1, m * n  ## right将
    while left + 1 < right:
        mid = (left + right) // 2
        x = matrix[mid // n][mid % n]  ## mid // n即为索引位于的行， mid % n即为索引位于的列
        if x == target:
            return True
        if x < target:
            left = mid
        else:
            right = mid
    return False

m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
print(searchMatrix(m, target))
