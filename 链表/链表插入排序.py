from typing import Optional
from base import ListNode, array_to_list
## 对链表进行插入排序，即将链表的节点按值从小到大排序，返回排序后的链表头节点
## 插入排序的原理和整理扑克牌一样，假设前面已经有序，将当前节点插入到前面有序的某个合适位置中

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        ## 一个虚拟头节点指向链表的头节点
        dummy = ListNode(0, next=head)
        pre = head
        cur = head.next
        while cur:
            ## 如果当前节点的值大于等于前一个节点的值，则继续向后遍历
            if pre.val <= cur.val:
                pre = cur
                cur = cur.next
            else:
                ## 首先保存当前节点位置
                tmp = cur
                ## 将当前节点从链表中删除
                pre.next = cur.next
                ## 更新当前节点为下一个节点
                cur = pre.next

                ## 这里是插入逻辑，从头开始寻找插入位置
                ## qpre是前一个节点，qcur是当前节点，这两个指针是用来寻找插入位置并插入的
                qpre = dummy
                qcur = head
                ## 如果当前节点的值小于要插入节点的值，则继续向后遍历
                while tmp.val > qcur.val:
                    qpre = qcur
                    qcur = qcur.next
                ## 此时qcur的位置是第一个大于要插入节点的值的位置
                qpre.next = tmp
                tmp.next = qcur
                ## 如果要插入的节点比链表的头节点还要小，则头节点变为要插入的节点，head此时是没插入之前的头节点也就是第二个节点，所以这里要更新头节点
                ## 更新头节点为dummy的下一个节点
                ## 如果要插入的节点比链表的头节点还要大，则头节点不变
                head = dummy.next
        return head