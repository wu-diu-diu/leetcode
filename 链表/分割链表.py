from typing import Optional, List
from base import ListNode, array_to_list

def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    index = 0
    cur_node = head
    while cur_node:
        index += 1
        cur_node = cur_node.next
    n, m = index // k, index % k ## n为每组至少需要几个节点，m为需要加1的组数，即有m组是(n+1)个节点，有(n-m)组是有n个节点
    ans = []
    p = head  ## p用来指向每组的头节点
    for i in range(k):
        cur_node = p  ## 临时指针，用来遍历
        num = n if i < m else n - 1 ## num为每组的节点数
        count = 0
        while count < num:
            cur_node = cur_node.next
            count += 1
        ans.append(p)
        if cur_node:
            p = cur_node.next
            cur_node.next = None  ## 在这里我们修改了链表的连接，即断开了链表
    return ans