
class Solution {
public:
  int findMin(vector<int>& nums) {
    int st = 0, en = nums.size() - 1;

    while (st < en) {
      int mid = st + (en - st) / 2;

      int val = nums[mid];

      if (val < nums[en]) {
        en = mid;
      }
      else {
        st = mid + 1;
      }
    }

    return nums[st];
  }
};
