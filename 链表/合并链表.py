from typing import Optional
from base import ListNode, array_to_list
## 将list1中从位置a到b的节点删除，然后将list2插入到a位置
def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur1 = list1
        pre  = list1
        count = 0
        while cur1:
            ## 没有移动到位置a之前
            if count < a:
                pre = cur1
                cur1 = cur1.next
                count += 1
            ## 移动到位置a之后，pre不再变动
            else:
                if count < b:
                    ## 继续向前移动
                    cur1 = cur1.next
                    count += 1
                ## 移动到位置b之后
                else:
                    ## pre的next指向list2的头节点
                    pre.next = list2
                    tmp = list2
                    ## 找到list2的尾节点
                    while tmp.next:
                        tmp = tmp.next
                    ## 将list2的尾节点的next指向cur1的next
                    tmp.next = cur1.next
                    break
        return list1