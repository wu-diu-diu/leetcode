#include <iostream>
#include <cstring>

using namespace std;

// 使用动态分配的方法求斐波那契数列的前n项
int main()
{
    int n;
    cout << "please input n = ?";
    cin >> n;
    // 动态分配的本质就是使用new运算符，从堆区动态的申请一块可以存放n+1个int的连续内存控件，并将这块空间的首地址赋值给p
    int *p = new int [n + 1];
    // p==0表示没有申请到内存
    if (p == 0 || n <= 0)
    {
        cout << "Error!" << endl;
        return -1;
    }
    p[0] = 0;
    p[1] = 1;
    cout << p[0] << endl;
    cout << p[1] << endl;
    for (int i = 2; i <= n; i++)
    {
        p[i] = p[i-1] + p[i-2];
        cout << p[i] << endl;
    }
    delete []p;
    return 0;

}