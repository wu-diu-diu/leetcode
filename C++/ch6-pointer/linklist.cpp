#include <iostream>
#include <cstring>

using namespace std;

struct ListNode {
    int val;  // 数据域
    // 结构体包含可以指向自身的指针
    ListNode *next;  // 指针域  next是指向listnode类型的指针
};
// head是指针的引用，也就是传入的指针变量的引用，则修改head的值就是修改传入的指针的值
// 变量的引用就是变量的别名，修改变量的引用即可修改这个变量
// 传递引用主要是为了方便的修改传入的指针变量的值，如果不适用应用，那么head就是传入的指针变量的副本，修改head的值并不会影响传入的指针的值
void append(ListNode*& head, int newData) {
    // newnode是一个指针，指向listnode类型的变量
    // 假设newnode的地址为0x1000，则此时newnode变量值为0x1000
    ListNode* newNode = new ListNode{newData, nullptr};
    // 如果是空指针，空指针即值为空，不指向任何值
    if (head == nullptr) {
        head = newNode;  // 修改head的值，即传入的指针的值修改为newnode，上面新建的一个listnode的地址，此时head的值为0x1000
        return;
    }
    
    ListNode* last = head; // 创建一个新的指针用于遍历
    // 遍历到链表末尾
    // c++中的last->val是(*last).val的语法糖，即->会自动解引用并访问成员变量
    while (last->next != nullptr) {
        last = last->next;
    }
    last->next = newNode;
}
// 第二种方案是使用二级指针，即head是指向传入的指针变量的指针，则要想修改传入的指针变量，则需要使用解引用的方法修改
// void append(Node** head, int newData) {
//     Node* newNode = new Node{newData, nullptr};
//     if (*head == nullptr) {
//         *head = newNode;  // ✅ 解引用后修改外部的指针
//         return;
//     }
//     // ... 其他代码
// }

void traverseLinkedList(ListNode* head) {
    ListNode* current = head;
    
    cout << "链表元素: ";
    while (current != nullptr) {
        cout << current->val << " ";
        current = current->next;
    }
    cout << endl;
}

int main() {
    ListNode* head = nullptr;  // 初始为空链表
    
    // 动态添加节点
    append(head, 15);
    append(head, 20);
    append(head, 30);
    append(head, 40);
    
    // 遍历链表
    traverseLinkedList(head);
    
    // 释放内存（需要遍历链表逐个删除）
    ListNode* current = head;
    while (current != nullptr) {
        ListNode* next = current->next;
        delete current;
        current = next;
    }
    
    return 0;
}