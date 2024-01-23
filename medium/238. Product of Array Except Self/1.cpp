#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(), 1);

        int prefix = 1;
        int postfix = 1;
        int n = nums.size();

        for (auto i = 0; i < n; ++i) {
            ans[i] *= prefix;
            prefix *= nums[i];

            ans[n - 1 - i] *= postfix;
            postfix *= nums[n - 1 - i];
        }

        return ans;        
    }
};