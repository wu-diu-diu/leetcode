#include <iostream>

using namespace std;
// 选择排序
void selectsort(int *list, int count)
{
    for(int i = 0; i < count - 1; i++)
    {
        int k = i;
        for (int j = i + 1; j < count; j++)
        {
            if (*(list + j) < *(list + k)) k = j;  //k保存[i,end]内的最小值的索引
        }
        if (k != i)
        {
            int tmp = list[k];
            list[k] = list[i];
            list[i] = tmp;
        }
    }
}

int main()
{
    int list[6] = {2,4,1,3,8,6};
    selectsort(list, 6);
    for (int i = 0; i < 6; i++){
        cout << list[i] << " ";
    }
    cout << endl;
}