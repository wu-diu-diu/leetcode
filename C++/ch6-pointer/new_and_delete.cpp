#include <iostream>

int main()
{
    int *ptr = new int (5);
    std::cout << "the value of ptr point to:" << *ptr << std::endl;
    delete ptr;
    std::cout << "the value of ptr point to:" << *ptr << std::endl;
    std::cout << "the value of ptr:" << ptr << std::endl;

    int *ptr1 = new int [5];
    *ptr1 = 1;
    ptr1[1] = 2;  // 指针的数组式访问，ptr[1] == *(ptr + 1)
    ptr1[2] = 3;
    std::cout << "the value of ptr1 point to: " << *ptr1 << std::endl;
    std::cout << "the second value of ptr1 point to : " << ptr1[1] << std::endl;
}