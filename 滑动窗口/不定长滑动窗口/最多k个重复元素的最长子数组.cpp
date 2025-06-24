#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution{
    public:
    int test(vector<int>& nums, int k){
        map<int, int> mp;
        int tem_res = 0;
        int res = 0;
        int left = 0;
        for(int i = 0; i < nums.size(); i++){
            while(mp[nums[i]] >= k){
                mp[nums[left]] -= 1;
                tem_res -= 1;
                left ++;
            }
            mp[nums[i]] += 1;
            tem_res += 1;
            res = max(res, tem_res);

        }
        return res;

    }
};

int main(){
    Solution solution;
    vector<int> nums = {1,2,3,1,2,3,1,2};
    int k = 2;
    cout << "Test1: " << solution.test(nums, k) << endl;
}
