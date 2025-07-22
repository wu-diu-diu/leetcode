from typing import Optional, List
from base import ListNode, array_to_list

## my solution  遍历整个链表一次，时间复杂度O(n),values存储链表的值， 创建一个新的链表current，与原链表长度相同，则空间复杂度
## 为O(n)
def reverse(head: ListNode) -> Optional[ListNode]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    if not values:
        return None
    head = ListNode(values[-1])
    current = head
    for i in range(len(values) - 2, -1, -1):
        current.next = ListNode(values[i])
        current = current.next
    return head

def print_node(head: ListNode):
    while head:
        print(head.val)
        head = head.next
## my solution2 递归解法，我们只需要每次改变节点的指向就可以，不需要对值有任何动作
## 递归调用会使用栈空间，每次递归调用都会将当前的上下文压入栈中，最坏情况下，递归深度为链表长度，因此空间复杂度是O(n)
def test2(head: ListNode) -> Optional[ListNode]:
    def _reverse(current_node: ListNode, last_node: ListNode):
        if not current_node:
            return last_node
        next_node = current_node.next  ## 这一操作的是常数时间复杂度，但是由于每个节点都要执行一遍，故时间复杂度是O(n)
        current_node.next = last_node
        return  _reverse(next_node, current_node)  ## 将递归的部分写在return上，可以将最后一层的递归层层返回到第一层
    return _reverse(head, None)

## 灵神
## 迭代法，使用常数级别的存储空间，空间复杂度是O(1)，要遍历整个链表，时间复杂度是O(n)
def test3(head: ListNode) -> Optional[ListNode]:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


    

arr_1 = [4,1,8,4,5]
head = array_to_list(arr_1)

reversed_head = test3(head)
print_node(reversed_head)


