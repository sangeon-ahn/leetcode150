class Solution {
    public:
    int removeElement(vector<int>& nums, int val) {
        int idx = 0; // 별도의 포인터 생성.
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
}