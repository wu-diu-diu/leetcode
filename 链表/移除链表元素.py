from typing import Optional, List
from base import ListNode, array_to_list
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        while (head and head.val == val):
            head = head.next
        p = head
        if not p: return None
        while p.next:
            nxt_node = p.next
            while nxt_node and nxt_node.val == val:
                nxt_nxt_node = nxt_node.next
                nxt_node = nxt_nxt_node
                p.next = nxt_node
            if p.next:
                p = p.next 
            else:
                break
        return head