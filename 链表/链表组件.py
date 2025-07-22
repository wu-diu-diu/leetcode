from typing import Optional, List
from base import ListNode, array_to_list

def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    count = 0
    flag = False  ## 标志位，判断上一个节点是否在nums中
    nums_set = set(nums)
    while head:
        val = head.val
        if val in nums_set and not flag:
            count += 1
        flag = (val in nums_set)
        head = head.next
    return count

head = [0,1,2,3,4]
nums = [0,3,1,4]
print(numComponents(array_to_list(head), nums))