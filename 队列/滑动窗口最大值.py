from collections import deque
## 维护一个单调递减的队列，遍历数组，遍历到某一个数时代表滑动窗口右端已经将该数包含
## 这时令元素入队，若元素大于队尾元素，则将队尾元素剔除，直到当前元素小于队尾元素
## 这样可以保证队首元素始终是窗口内的最大值
def maxslidingwindow(nums: list[int], k: int) -> int:
    ans = []
    q = deque()
    for i, num in enumerate(nums):
        # 队尾入队
        while q and nums[q[-1]] < num:  ## 如果q不为空，且队尾元素小于入队元素，则违反递减，原队尾元素出队，新的元素入队
            q.pop()
        q.append(i)
        # 队首出队，保证队列的长度不超过窗口大小
        if i - q[0] >= k:
            q.popleft()
        # 记录答案
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans

def minslidingwindow(nums: list[int], k: int) -> int:
    ans = []
    q = deque()
    for i, num in enumerate(nums):
        ## 入队, 队列单调递增
        while q and nums[q[-1]] > num:
            q.pop()
        q.append(i)
        ## 出队
        if i - q[0] >= k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans


def MaxSlidingWindow(nums: list[int], k:int) -> list[int]:
    n = len(nums)
    result = []
    max_win = max(nums[0:k])
    result.append(max_win)
    for i in range(1, n - k + 1):
        left = i
        right = i + k
        new = nums[right - 1]  ## 新进入的
        last = nums[left - 1]  ## 刚退出的
        if last != max_win and new > max_win:  ## 上一次的最大值仍在window中，新进入的值更大
            result.append(new)
            max_win = new
        elif last != max_win and new <= max_win:  ## 上一个窗口的最大值仍然在window中，新进入的值小于等于
            result.append(max_win)
        elif last == max_win:
            max_win = max(nums[left:right])
            result.append(max_win)
    return result
nums = [1,3,-1,-3,5,3,6,7]
# nums = [1]
# nums = [-7,-8,7,5,7,1,6,0]
k = 3
# k = 1
# k = 4
print(minslidingwindow(nums, k))