struct ListNode {
    int val;
    ListNode *next;
};

class Solution {
    public:
        void deleteNode(ListNode* node) {
            // 下一个节点的指针
            auto nxt = node->next;
            *node = *nxt; // 将下一个节点的指针指向的node赋值给当前指针指向的node
            delete nxt; // 删除下一个节点
            // 相当于A->B->C->D，删除B，变为A->C(B变的)->D
        }
};