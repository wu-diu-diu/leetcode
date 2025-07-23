// 在c++中，结构体（struct）是一种用户自定义的数据类型，可以包含不同类型的成员变量。
// 结构体的默认访问权限不同，与类（class）相比，结构体的成员默认是公有的（public），而类的成员默认是私有的（private）。
// 其中val和next是结构体的成员变量，val是一个整数类型的变量，next是一个指向同类型结构体的指针，用于实现链表结构。
// 其中三个ListNode()都是构造函数，区别在于初始化成员变量的方式不同。
struct ListNode {
      int val;
      ListNode *next;
      // 下面这种写法是初始化列表，即成员变量在对象构造时直接获得初始值
      ListNode() : val(0), next(nullptr) {}  // 不提供任何初始值，使用默认值
      ListNode(int x) : val(x), next(nullptr) {}  // 只提供val的初始值，next指向nullptr
      ListNode(int x, ListNode *next) : val(x), next(next) {} // 提供val和next的初始值，next指向指定的ListNode对象
 };

// 初始化方法
ListNode head;
ListNode head1(1); // val=1, next=nullptr
ListNode head2(2, &head1); // val=2, next指向head1对象

// 以下是一个Node类，有两个成员变量val和next，val是一个整数类型的变量，next是一个指向同类型Node对象的指针。
// 有三个构造函数，分别用于不同的初始化方式。
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = nullptr;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};

// 初始化方法
Node node1; // 默认构造函数，val和next未初始化
Node node2(10); // val=10, next=nullptr
Node node3(20, &node2); // val=20, next指向node2对象