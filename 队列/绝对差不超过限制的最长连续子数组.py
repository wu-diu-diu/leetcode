from collections import deque
def longestSubarray(nums: List[int], limit: int) -> int:
    q = deque()
    for i, num in enumerate(nums):
        
        q.append(i)