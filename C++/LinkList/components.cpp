#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
};

ListNode* construct(vector<int> nums)
{
    int len = nums.size();
    if (len == 0) return nullptr;
    ListNode* head = new ListNode{nums[0], nullptr};
    ListNode* current = head;
    for (int i = 1; i < len; i++)
    {
        ListNode* newNode = new ListNode{nums[i], nullptr};
        current->next = newNode;
        current = current->next;
    }
    return head;
}

int main(ListNode* head, vector<int>& nums)
{
    int count = 0;
    // 创建一个unordered_set来存储nums中的元素，是一个集合，查找效率为O(1)
    unordered_set<int> nums_set(nums.begin(), nums.end());
    ListNode* current = head;
    bool last_in_nums = false;
    while (current != nullptr)
    {
        // 如果当前节点的值在nums_set中，则current_in_nums为true，否则为false
        // find会返回一个迭代器，指向集合中等于当前值的元素，如果没有找到，则返回end迭代器
        // 这里的迭代器是一个类似指针的对象，用来访问容器vector或unordered_set中的元素，功能类似数组下标
        bool current_in_nums = (nums_set.find(current->val) != nums_set.end());
        if (current_in_nums && !last_in_nums) {
            count++;
        }
        last_in_nums = current_in_nums;
        current = current->next; // 移动指针
    }
    return count;

}
