class Solution {
public:
    int singleNumber(vector<int>& nums) {
       int ones = 0;
       int twos = 0;

       // x is appeared 3 times in nums, there are no xes in ones and twos;
       // so, after iteration there is only that number appeared once.
       //
       for (const auto& num : nums) {
         ones ^= (num & ~twos);
         twos ^= (num & ~ones);
       }

       return ones;
    }
};
