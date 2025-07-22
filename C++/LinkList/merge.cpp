struct ListNode {
    int val;
    ListNode *next;
};

class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* cur1 = list1;
        ListNode* pre = list1;
        int count = 0;

        while (cur1) {
            if (count < a) {
                pre = cur1;
                cur1 = cur1->next;
                count++;
            } else {
                if (count < b) {
                    cur1 = cur1->next;
                    count++;
                } else {
                    pre->next = list2;

                    // 找到 list2 的尾节点
                    ListNode* tmp = list2;
                    while (tmp->next) {
                        tmp = tmp->next;
                    }

                    // 连接 list1 的剩余部分
                    tmp->next = cur1->next;
                    break;
                }
            }
        }

        return list1;
    }
};