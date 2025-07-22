
from typing import Optional, List
from base import ListNode, array_to_list, print_linked_list
def modifiedList(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        nums_set = set(nums)
        pre = None
        while p:
            cur_val = p.val
            if cur_val in nums_set and pre:
                nxt_node = p.next
                pre.next = nxt_node
                p.next = None
                p = nxt_node
                continue
            if cur_val in nums_set and not pre:
                ## 如果第一个节点就在nums中，这里把head指向为None之后，head并没有更新
                nxt_node = p.next
                p.next = None
                p = nxt_node
                continue
            pre = p
            p = p.next
        return head

def test(nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            cur_val = cur.val
            if cur_val in nums_set:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        ## 并不能返回head,因为head指向的指可能已经修改
        ## dummy的存在就是保证dummy的下一个节点就是删除后链表的头节点
        return dummy.next

head = [1,2,3,4,5]
nums = [1,2,3]
print(print_linked_list(test(nums, array_to_list(head))))