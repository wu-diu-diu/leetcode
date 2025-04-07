## 输入为：5 2 3 2 4 3 5 2 1 4 3
## 输出为：2 5 1 4
## 第一个数是链表长度，第二个数是头节点的值，后面num个数字对分别比如(3,2)表示3插在2后面，最后一个数是要删除的节点值

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert(self, val1, val2):
        cur = self.head
        node = Node(val2)  ## val1是之前的节点值，val2是新节点值
        while cur:
            if cur.val == val1:  ## 从头开始遍历链表，找到val1所在的节点
                node.next = cur.next  ## 新节点的next指向当前遍历到的节点的next
                cur.next = node  ## 当前遍历到的节点的next指向新节点
                ## 以上两步操作则将在指定节点之后插入了一个新的节点 5->6  ---->  5->7->6
                break
            else:
                cur = cur.next

    def remove(self, val):
        cur = self.head
        pre = None
        while cur:
            if cur.val == val:
                if not pre:  ## 如果pre为空，说明当前节点是头节点
                    self.head = cur.next  ## 直接将头节点指向当前节点的下一个节点
                else:
                    pre.next = cur.next  ## 如果当前节点不是头节点，将前一个节点的next指向当前节点的next
                    ## 则删除了当前节点   5->7->6  ---->  5->6
                break
            else:
                pre = cur
                cur = cur.next

    def walk(self):  ## 遍历链表的值并打印
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()  ## 换行


while True:
    try:
        nums = list(map(int, input().split()))
        L = LinkedList()  ## 初始化链表
        L.length, L.head.val = nums[0], nums[1]  ## 初始化链表长度和头节点值
        lst = nums[2:-1]  ## 获取链表中的值
        i, j, pairs = 0, 1, []
        while i < len(lst):
            pairs.append((lst[i], lst[j]))
            i += 2
            j += 2
        for p in pairs:
            L.insert(p[1], p[0])
        L.remove(nums[-1])
        L.walk()
    except:
        break