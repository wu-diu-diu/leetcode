from collections import deque
def test(nums:list[int], k:int) -> list[int]:
    dq = deque()
    res = []
    for i, num in enumerate(nums):
        # 如果队列内有值并且当前要入队的值大于队尾元素，则队尾元素出队，知道队内无值或者当前元素小于等于队尾元素
        while dq and num > dq[-1]:
            dq.pop()
        # 当前值入队，这样队内的元素从首到尾是降序的
        dq.append(num)
        # 如果滑动窗口成型，则开始将队首元素添加到结果列表中
        if i + 1 - k >= 0:
            res.append(dq[0])
        # 如果队内元素大于等于滑动窗口值，则队首元素需要出队
        # 使用队列的长度来控制窗口大小
        if len(dq) >= k:
            dq.popleft()
    return res
# 和上一个不同的是，这里的队列存储的是索引而非值
def test_2(nums:list[int], k:int) -> list[int]:
    dq = deque()
    res = []
    for i, num in enumerate(nums):

        while dq and num > nums[dq[-1]]:
            dq.pop()
        
        dq.append(i)
        # 使用索引来判断是否超出窗口大小更为直观
        if dq[0] <= i - k:
            dq.popleft()
        
        if i + 1 >= k:
            res.append(nums[dq[0]])
    return res
        



test_list = [5,6,8,3,2,7,9,1]
print(test(test_list, 3))

        
