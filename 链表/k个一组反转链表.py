from typing import Optional
from base import ListNode, array_to_list

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next or k == 1: return head;
        dummy = ListNode(0, next=head)
        ppre = dummy

        while True:
            count = 0
            check = ppre
            while count < k and check:
                check = check.next
                count += 1
            if not check: break;

            pre = ppre.next
            cur = pre.next
            for _ in range(1, k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            tail = ppre.next
            tail.next = cur
            ppre.next = pre

            ppre = tail
        
        return dummy.next