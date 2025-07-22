from typing import Optional, List
from base import ListNode, array_to_list
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        cur = head.next
        while cur.next:
            if cur.val:
                tail.val += cur.val
            else:
                tail = tail.next
                tail.val = 0
            cur = cur.next
        tail.next = None
        return head
head = [0,1,0,3,0,2,2,0]
print(mergeNodes(array_to_list(head)))