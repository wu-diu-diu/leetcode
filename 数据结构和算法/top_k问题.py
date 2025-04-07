## 选择排序，时间复杂度是O(n^2)
def find_top_k(x: list, k: int) -> list[int]:
    result = []
    for i in range(k):
        max_num = 0
        for j in range(len(x)):
            if x[j] > max_num:
                max_num = x[j]
                max_index = j
        x.pop(max_index)
        result.append(max_num)
    return result

## 堆排序，时间复杂度是O(nlogk)
import heapq
def find_top_heap(x: list, k: int) -> list[int]:
    heap = []
    for i in range(k):
        heapq.heappush(heap, x[i])  ## 元素入堆会自动进行堆化，这里默认形成小顶堆，则堆顶元素是最小的
    for i in range(k, len(x)):
        if x[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, x[i])
    return heap

lst = [1,7,6,3,2]
heap = find_top_heap(lst, 5)
print(heap)
heapq.heappop(heap)  ## 弹出堆顶元素后会自动从上到下进行堆化
print(heap)
