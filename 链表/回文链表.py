from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
## 反转链表
def ReverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre
## 找到链表的中间节点
## 因为fast的速度比slow速度快一倍，所以当slow走到中间的时候，fast正好走到结尾，这时while条件不成立则会跳出循环
## 对于偶数个的链表，算上尾指针指向的none，也可以看作是奇数个值，则当fast走到none的时候，slow刚好走到偶数中间的右边第一个节点
def MidListNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def test(head: Optional[ListNode]) -> bool:
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    for i in range(len(lst) // 2):  ## 判断一个列表是否是回文列表 从列表两端开始遍历，判断数是否始终相等
        if lst[i] != lst[-i - 1]:
            return False
    return True

def test2(head: Optional[ListNode]) -> bool:
    mid = MidListNode(head)  ## 先找到链表的中间节点
    reverse = ReverseList(mid)  ## 从中间节点开始，将之后的链表反转，则此时有两个链表，尾部指向同一个值
    while reverse:  ## 同时遍历两个链表，若他们的的值始终相等，则返回True否则返回false
        if reverse.val != head.val:
            return False
        reverse = reverse.next
        head = head.next
    return True

head = ListNode(1)
print(test2(head))