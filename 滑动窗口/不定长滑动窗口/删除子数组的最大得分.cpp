#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <map>

using namespace std;

class Solution {
    public:
    int test(vector<int>& nums){
        map<int,int>mp;
        int tem_res = 0;
        int res = 0;
        int left = 0;

        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            mp[num]++;
            tem_res += num;
            while (mp[num] >= 2){
                mp[nums[left]]--;
                tem_res -= nums[left];
                left++;
            }
            res = max(res, tem_res);
        }
        return res;
    }
};

int main(){
    Solution solution;
    vector<int> nums = {4,2,4,5,6};
    int result = solution.test(nums);
    cout << "test: " << result << endl;
    return 0;
}