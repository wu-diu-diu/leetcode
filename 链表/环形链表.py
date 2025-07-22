from typing import Optional
from base import ListNode, array_to_list
n0 = ListNode(3)
n1 = ListNode(2)
n2 = ListNode(0)
n3 = ListNode(-4)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n1
## 快慢指针
## fast是快指针，slow是慢指针，fast每次走一个
def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def detectCycle(head: Optional[ListNode]) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

print(detectCycle(n0))