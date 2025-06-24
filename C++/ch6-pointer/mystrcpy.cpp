#include <iostream>
#include <cstring>
using namespace std;
// target,source分别是两个指针，传入时分别指向目标字符串的首地址和源字符串的首地址
void mystrcpy(char * target, char * source)
{
    while(*source != 0)  // 指针指向的源字符串的当前字符不为0，即指针没有指向源字符串的末尾
    {
        *target = *source; // 源指针指向的地址的值，赋值给目标指针指向的地址的值
        source++;  // 指针向后移动一位
        target++; 
    }
    *target = 0; //将目标字符串的最后一位赋值为0
    // 以上while循环包括赋值为0这些代码可以用一行替代：while((* target++ == * source++) != 0)
}
void my_clear_array(float * ptr, int len)
{
    int cnt = 0;
    while(cnt != len)
    {
        *ptr = 0.0;
        ptr++;
        cnt++;
    }
}

void clear_array(float *ptr, int len)
{   
    float * qtr;
    qtr = ptr + len; //ptr 和 qtr都是指向float变量的指针，所以其+1，地址会移动4个字节，因为一个float变量占据四个字节
    while(*ptr != *qtr)  // while(ptr < qtr)
    {
        *ptr = 0.0;
        ptr++;
    }
}

int main()
{
    char string1[] = "this is source string";
    char string2[] = "this is target string";
    char str[6] = "big";
    char *ptr = str;
    cout << "the value of *ptr:" << *ptr << endl;
    cout << "the value of *++ptr:" << *++ptr << endl;
    cout << "the value of *++ptr:" << *++ptr << endl;
    int len = strlen(string1);
    mystrcpy(string2, string1);
    cout << "source string:" << string1 << endl;
    cout << "target string:" << string2 << endl;
    cout << "string length:" << len << endl;
    float arr[5] = {0.1,0.2,0.3,0.4,0.5};
    cout << "original arr:" << arr[0] << endl;
    int len_arr = sizeof(arr) / sizeof(arr[0]);
    clear_array(arr, len_arr);
    cout << "cleared arr:" << arr[0] << endl;
    
}