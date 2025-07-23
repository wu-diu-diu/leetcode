#include <vector>
#include <iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}  // 默认构造函数
    ListNode(int x) : val(x), next(nullptr) {}  // 构造函数，初始化val
    ListNode(int x, ListNode *next) : val(x), next(next) {}  // 构造函数，初始化val和next
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        ListNode* pre = nullptr;
        ListNode* cur = head;
        ListNode* nxt;
        while (cur != nullptr){
            nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};

// 反转一个链表中left到right的部分
class Solution_2 {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // 如果链表为空或只有一个节点，直接返回头节点
        if (head == nullptr || head->next == nullptr) return head;
        int count = 1;
        ListNode* cur = head;
        // 创建虚拟头节点，因为如果left=1，头节点按照程序会指向none，则我们需要一个虚拟头节点来处理这种情况
        ListNode dummy(0, head);
        ListNode* pre = &dummy;
        while (cur != nullptr){
            // 如果当前节点是需要反转的范围内的节点
            if (count == left){
                // qpre是反转操作中，用来指向当前节点的上一个节点的指针
                ListNode* qpre = cur;
                // nxt是反转操作中，用来指向当前节点的下一个节点的指针
                ListNode* nxt;
                // tmp是指向需要反转的子链表的头节点
                ListNode* tmp = cur;
                // 向后移动一步，因为下面的反转操作cur要和qpre不同
                cur = cur->next;
                // count表示cur当前所在的位置，以1开头
                count++;
                // 反转操作，从left到right
                while (count <= right){
                    nxt = cur->next;
                    cur->next = qpre;
                    qpre = cur;
                    cur = nxt;
                    count++;
                }
                // 处理反转链表的两头的节点的指向
                // 反转操作完成后，qpre指向了反转后的子链表的头节点
                // tmp指向了反转前的子链表的头节点
                // cur指向了反转后的子链表的下一个节点
                // pre指向了反转前的子链表的上一个节点
                pre->next = qpre;
                tmp->next = cur;
                break;

            }
            // 如果当前节点不是需要反转的范围内的节点，则继续向后移动
            pre = cur;
            cur = cur->next;
            count++;
        }
        return dummy.next;
    }
    public:
    ListNode* buildLinkedList(const vector<int>& arr) {
    if (arr.empty()) return nullptr;  // 空数组返回空链表

    ListNode* head = new ListNode(arr[0]);  // 创建头结点
    ListNode* current = head;

    for (size_t i = 1; i < arr.size(); ++i) {
        current->next = new ListNode(arr[i]);  // 创建新节点并连接
        current = current->next;
    }

    return head;
    }
    // 反转链表中偶数长度的组
    public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        if (!head->next || !head->next->next) return head;
        int groupnums = 1;
        ListNode dummy(0, head);
        ListNode* check = &dummy;
        ListNode* ppre = &dummy;
        ListNode* nxt;
        while(true){
            // 如果剩余的点不足以组成一个完整的组，但是是偶数个节点，则需要反转
            int left_nodes = -1;
            // 链表反转后，ppre总是在反转后的链表的尾节点，所以更新check让其位于尾部
            check = ppre;
            for (int i=0;i<groupnums && check;i++) {
                check = check->next; 
                left_nodes++;
            }
            // 如果不足以构成一个完整组且剩余奇数个点，则无需反转，直接退出
            if (!check && left_nodes % 2 != 0) {
                break;
            // 不剩余节点了，但是check指向nullptr，所以单拿出来讨论，这里也退出
            }else if (!check && left_nodes == 0){
                break;
            }
            // 如果剩余的点不足以组成一个完整的组，但是是偶数个节点，则需要反转
            else if (!check && left_nodes % 2 == 0){
                ListNode* pre = ppre->next;
                ListNode* cur = pre->next;
                for (int i=1;i<left_nodes;i++){
                    nxt = cur->next;
                    cur->next = pre;
                    pre = cur;
                    cur = nxt;
                }
                ListNode* tail = ppre->next;
                tail->next = cur;
                ppre->next = pre;
                ppre = tail;
                // 反转完直接退出
                break;
            }
            // 如果当前组的节点数是偶数个，则需要反转
            if (groupnums % 2 == 0){

                ListNode* pre = ppre->next;
                ListNode* cur = pre->next;
                for (int i=1;i<groupnums;i++){
                    nxt = cur->next;
                    cur->next = pre;
                    pre = cur;
                    cur = nxt;
                }
                ListNode* tail = ppre->next;
                tail->next = cur;
                ppre->next = pre;
                ppre = tail;
            }else{  // 如果当前组的节点数是奇数个，则不需要反转，向后遍历groupnums个节点,保证ppre位于每组节点的尾部
                for (int j=0;j<groupnums;j++) ppre = ppre->next;
            }
            groupnums++;
        }
        return dummy.next;
    }
};

// 测试代码
int main() {
    Solution_2 solution;
    vector<int> arr = {1,1,0,6,5};
    ListNode* head = solution.buildLinkedList(arr);
    
    // 测试反转链表
    ListNode* reversedHead = solution.reverseEvenLengthGroups(head);
    
    // 打印反转后的链表
    ListNode* current = reversedHead;
    while (current) {
        cout << current->val << " ";
        current = current->next;
    }
    cout << endl;

    return 0;
}
