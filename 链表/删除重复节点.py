from typing import Optional, List
from base import ListNode, array_to_list
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set()
        cur = head
        pre = head
        while cur:
            if cur.val not in nums_set:
                nums_set.add(cur.val)
            else:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
                continue
            pre = cur
            cur = cur.next
        return head

def test(head: Optional[ListNode]) -> Optional[ListNode]:
        ## 删除多余的重复元素
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

def deleteDuplicates_2(head: Optional[ListNode]) -> Optional[ListNode]:
        ## 删除所有重复的元素 1-> 2->3->3->4->4->5 变为 1->2->5
        pre = None
        cur = head
        dummy = ListNode(0, next=head)
        pre = dummy
        hava_repeat = False
        while cur and cur.next:
            ## 如果当前节点和下一个节点的值相同，则移动到最后一个相同的节点
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                hava_repeat = True
            ## 说明有重复元素且此时位于最后一个重复元素 
            if hava_repeat:
                pre.next = cur.next
                cur = pre.next
                hava_repeat = False
                continue
            pre = cur
            cur = cur.next
        return dummy.next