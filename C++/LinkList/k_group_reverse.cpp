struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}  // 默认构造函数
    ListNode(int x) : val(x), next(nullptr) {}  // 构造函数，初始化val
    ListNode(int x, ListNode *next) : val(x), next(next) {}  // 构造函数，初始化val和next
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head->next == nullptr || k == 1) return head;
        ListNode dummy(0, head);
        ListNode* ppre = &dummy;
        ListNode* nxt;
        
        while (true){
        // 检查之后是否有k个节点
        ListNode* check = ppre;
        for (int i =0; i<k && check != nullptr;i++) check = check->next;
        if (check == nullptr) break;
        // 从ppre开始翻转k个节点
        ListNode* pre = ppre->next;
        ListNode* cur = pre->next;
        // 反转k个节点
        for(int i=1;i<k;i++){
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        ListNode* tail = ppre->next; // 当前组原来的头 -> 现在是尾
        tail->next = cur;            // 尾连接到下一段
        ppre->next = pre;            // 头接上翻转后新的头

        ppre = tail;                 // 移动到当前组末尾，为下一组准备

        }
        return dummy.next;
    }
};