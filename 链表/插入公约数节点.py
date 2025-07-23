from typing import Optional, List
from base import ListNode, array_to_list
## 在原链表的基础上，在相邻节点之间插入两个节点值的公约数
def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        pre = None
        cur = head
        while cur:
            if not pre:
                pre = cur
                cur = cur.next
            pre_val = pre.val
            cur_val = cur.val
            new_val = gcd(pre_val, cur_val)
            node = ListNode(new_val, next=cur)
            pre.next = node
            pre = cur
            cur = cur.next
        return head

## 返回两个数最大的公约数，a,b大小不定，传入参数的时候a>b或者b>a都行
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a