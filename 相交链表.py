from typing import Optional, List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

arr_1 = [4,1,8,4,5]
arr_2 = [5,6,1,8,4,5]
head_A = array_to_list(arr_1)  ## 这里有个bug， headA和headB是两个独立的链表，是不相交的的， 所以下面的程序没有输出预期结果
head_B = array_to_list(arr_2)

## kimi
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        len_a = get_length(headA)
        len_b = get_length(headB)
        if len_a > len_b:
            for i in range(len_a - len_b):
                headA = headA.next
        else:
            for i in range(len_b - len_a):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
## 灵神解法
def test2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p is not q:  ## 两个链表的自有部分x,y和公共部分z，x+z+y=y+z+x所以只要让两个链表分别在走到尽头时返回到另一个链表的头节点
            ## 则它们会在相同的时间步内达到同一个点
            ## 如果两个链表不相交，则最终两个链表也都会到达空节点，则while循环终究会跳出
            p = p.next if p else headB  ## 如果链表A走到了尽头，则返回到链表B的头节点
            q = q.next if q else headA  ## 如果链表B走到了尽头，则返回链表A的头节点
        return p