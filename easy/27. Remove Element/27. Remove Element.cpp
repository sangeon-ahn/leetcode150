#include <bits/stdc++.h>

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // 2의 위치를 별도의 배열에 저장한 후, 
        vector<int> saved;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                saved.push_back(i);
            }
        }

        for (int i = 0; i < saved.size(); i++) {
            nums[i] = nums[saved[i]];
        }
        
        return saved.size();
    }
};