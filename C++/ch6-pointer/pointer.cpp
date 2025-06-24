#include <iostream>
using namespace std;

int main()
{
    double x, a[10], *ptr = a;
    a[0] = 10;
    a[1] = 11;
    a[2] = 12;
    int b = 25;
    int* ptr2 = &b;
    cout << "the ptr value is:" << ptr <<endl; // ptr是一个指针，它的值即是所指向变量的地址，这里初始化是ptr指向了数组a的第一个元素
    cout << "the address of a is:" << a << endl;  //数组的数组名可以代表数组首个元素的地址
    cout << "the ++ptr value is:" << (++ptr) <<endl;  //++ptr是前缀自增运算，即先对ptr自增，然后输出ptr自增后的值，这里为a第二个元素的地址
    cout << "the address of a[1] is:" << &a[1] << endl;
    cout << "the value of ptr point to:" << *ptr << endl; // *ptr是指ptr指向的元素的值，这里是a的第二个元素
    cout << "the value of a[0] is:" << a[0] << endl;
    cout << "the value of ptr++ point to:" << *(ptr++) << endl; // ptr++是后缀自增运算，即先赋值，再对ptr进行自增，所以这里还是第二个元素的值
    cout << "now the value of ptr point to:" << *ptr << endl;
    cout << "the value of a[1] is:" << a[1] << endl;
    cout << "the value of b is:" << b << endl;
    cout << "the address of b is:" << &b << endl;
    cout << "the value of *ptr2 is:" << *ptr2 << endl;
    cout << "the value of ptr2 is:" << ptr2 << endl;
    return 0;
    
}