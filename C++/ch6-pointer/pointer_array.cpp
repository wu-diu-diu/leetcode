#include <iostream>
#include <cstring>
using namespace std;
// 二分法查字典
// 函数返回的是一个char类型的指针
// char *word表示word是一个指向字符类型的指针
// char *dic[]表示，dic是一个指针数组，其中每一个元素都是一个char类型的指针
char *search_word(char *word, char *dic[], int n)
{
    int low = 0;
    int high = n - 1;
    int mid, searchpos, wordlen = strlen(word);
    do
    {
        mid = (low + high) / 2;
        // word是被查找单词的首地址
        // dic[mid]是字典中第mid个单词的首地址
        // wordlen是要比较的字符数
        searchpos = strnicmp(word, dic[mid], wordlen);
        if(searchpos == 0)
        {
            return dic[mid];
        }
        else if(searchpos < 0) //针对word第一个与dic[mid]不同的字符，word的值更小，则word在dic中的位置应该小于mid
        {
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    } while (high > low);
    return NULL;
}