// const space, linear time
// nums : [1, 3, 1, 3, 2], return: 2

#include <vector>
using namespace std;


class Solution {
public:
    int singleNumber(vector<int>& nums) {
      int result = 0;
      for (auto& num : nums) {
        result ^= num;
      } 
      return result;
    }
};
