#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    vector<int> vec = {1, 2, 3};

    // 访问
    cout << "vec[1] = " << vec[1] << endl;  // 2

    // 修改
    vec.push_back(4);      // {1, 2, 3, 4}
    vec.pop_back();        // {1, 2, 3}
    vec.insert(vec.begin() + 1, 99);  // {1, 99, 2, 3}

    // 遍历
    for (auto it = vec.begin(); it != vec.end(); ++it) {
        cout << *it << " ";
    }
    // 输出: 1 99 2 3
    cout << "vec.begin:" << *vec.begin() << endl;  // vec.begin返回的是一个指向第一个元素的是一个指针类型的迭代器
    cout << "vec.end:" << *(vec.end() - 1) << endl;  // 注意end()返回的是一个指向尾后元素的迭代器

    // 清空
    vec.clear();
    cout << "\nSize after clear: " << vec.size() << endl;  // 0

    unordered_set<int> s = {1, 2, 3};
    //这里的auto是指让编译器自动推断变量的类型
    auto it = s.find(2);     // 返回一个指向 2 的迭代器
    if (it != s.end()) {
        cout << *it;    // 输出 2
    }
}