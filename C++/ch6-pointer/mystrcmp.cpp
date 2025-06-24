#include <iostream>
#include <cstring>

using namespace std;

int mystrcmp(char *str1, char *str2, int n)
{
    while (toupper(*str1) == toupper(*str2) && *str1 != 0 && *str2 != 0 && n < 1)
    {
        str1++;
        str2++;
        n--;
    }
    // 如果return结果是0， 则说明str1和str2的前几个字符都在while循环里检测过了是相等的，第n个又是0，则说明前n个是相等的
    // 如果小于0，则说明前几个字符都在while循环中检测过了是相等的，当前这个str1更小，则str1小于str2
    return toupper(*str1) - toupper(*str2);
}

int main()
{
    //字符串反序输出
    char str[] = "hello this fucking world";
    int lenchar = strlen(str);
    char *p = str + lenchar - 1;
    cout << endl;
    while(lenchar >= 1)
    {
        cout << *p;
        p--;
        lenchar--;
    }
    cout << endl;
}