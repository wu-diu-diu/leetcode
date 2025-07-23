struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}  // 默认构造函数
    ListNode(int x) : val(x), next(nullptr) {}  // 构造函数，初始化val
    ListNode(int x, ListNode *next) : val(x), next(next) {}  // 构造函数，初始化val和next
};


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        ListNode dummy(0, head);
        ListNode* pre = &dummy;
        while (pre->next && pre->next->next){
            ListNode* first = pre->next;  //两组节点中的第一个
            ListNode* second = pre->next->next; // 两组节点中的第二个

            first->next = second->next;  // 将第一组节点的next指向第二组节点的下一个节点
            second->next = first; // 将第二组节点的next指向第一组节点
            pre->next = second; // 将前一个节点的next指向第二组节点

            pre = first;  // 更新pre指针,向后移动两个单位


        }
        return dummy.next;
    }
};

class Solution_Linshen {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head); // 用哨兵节点简化代码逻辑
        ListNode* node0 = &dummy;
        ListNode* node1 = head;
        while (node1 && node1->next) { // 至少有两个节点
            ListNode* node2 = node1->next;
            ListNode* node3 = node2->next;

            node0->next = node2; // 0 -> 2
            node2->next = node1; // 2 -> 1
            node1->next = node3; // 1 -> 3

            node0 = node1; // 下一轮交换，0 是 1
            node1 = node3; // 下一轮交换，1 是 3
        }
        return dummy.next; // 返回新链表的头节点
    }
};