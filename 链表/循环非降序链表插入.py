from typing import Optional
from base import ListNode, array_to_list

def solutiuon(head: Optional[ListNode], insertVal: int) -> Optional[ListNode]:
    newnode = ListNode(insertVal)
    if not head:
        newnode.next = newnode
        return newnode
    cur = head

    while True:
        ## 情况1，在环形链表中能找到一个节点的值小于等于要插入的值，且下一个节点的值大于等于要插入的值，则插入在当前节点的后面
        if (cur.val <= insertVal or insertVal <= cur.next.val):
            break
        ## 找到非降序环形链表的最大值的位置，且下一个是最小值
        if (cur.val > cur.next.val):
            ## 情况2，如果插入点的值大于最大值，或者小于最小值，则插入到最大值即当前节点后面
            if (insertVal >= cur.val or insertVal <= cur.next.val):
                break
        ## 向后遍历
        cur = cur.next
        ## 如果遍历到头节点，则说明链表中所有节点的值都相等，此时可以将新节点插入到任意位置
        if cur == head:
            break
    newnode.next = cur.next
    cur.next = newnode
    return head