from typing import Optional, List
from base import ListNode, array_to_list
## 只给你一个要删除的节点，请你在链表中删除这个节点，无需返回任何值
## 如果不知道前驱节点，可以将要删除的节点的值替换为下一个节点的值，然后删除下一个节点
## 其实就是将下一个节点的值以及下一个节点的next都复制给当前节点(删除下一个节点)
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

