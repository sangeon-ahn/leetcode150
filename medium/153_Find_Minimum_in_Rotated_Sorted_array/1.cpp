#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 1 || nums[0] < nums[nums.size() - 1]) return nums[0];
        
        
        int st = 0;
        int en = nums.size() - 1;

        while (st <= en) {
          int mid = (st + en) / 2;

          int val = nums[mid];

          if ((mid - 1 < 0 || nums[mid - 1] < val) && (mid + 1 >= nums.size() || val < nums[mid + 1])) {
            if (val > nums[en]) {
              st = mid + 1;
            }
            else {
              en = mid - 1;
            }
          }
          else if ((mid - 1 < 0 || nums[mid - 1] > val) && (mid + 1 >= nums.size() || val < nums[mid + 1])) {
            return val;
          }
          else if ((mid - 1 < 0 || nums[mid - 1]) < val && val > (mid + 1 >= nums.size() || nums[mid + 1])) {
            return nums[mid + 1];
          }
        }
        return 0;
    }
};


int main()
{
  vector<int> nums{4, 5, 6, 7, 0,1,2};
  Solution sol;
  int res = sol.findMin(nums);
  cout << res << endl;
}
