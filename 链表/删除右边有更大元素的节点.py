## 给定一个链表的头节点，删除这个链表右边有更大元素的节点。
## 应该反着看，从链表的尾部看，将链表的尾节点当作头节点，即为删除比当前节点更小的节点
from typing import Optional, List
from base import ListNode, array_to_list, print_linked_list
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = self.reverseList(head)  ## 先把链表反转
        while cur.next:
            if cur.val > cur.next.val:  ## 如果下一个节点的值小于当前节点
                cur.next = cur.next.next  ## 则删除下一个节点
            else:
                cur = cur.next ## 否则继续向下遍历
        return self.reverseList(head)  ## 最后再反转回来
    
if __name__ == "__main__":
    s = Solution()
    head = array_to_list([5, 2, 13, 3, 8])
    res = s.removeNodes(head)
    print(print_linked_list(res))  # 输出: [13, 8]
    head = array_to_list([1, 1, 1, 1])
    res = s.removeNodes(head)
    print(print_linked_list(res))  # 输出: [1]