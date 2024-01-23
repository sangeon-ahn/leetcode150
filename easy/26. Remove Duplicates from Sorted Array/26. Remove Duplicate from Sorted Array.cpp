class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int idx = 1;
        for (int p = 1; p < nums.size(); p++) {
            if (nums[p - 1] != nums[p]) {
                nums[idx] = nums[p];
                idx++;
            }
        }
        
        return idx;
    }
};