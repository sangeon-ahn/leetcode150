// 애초에 nums1에 n개의 0이 들어 있었던 이유는 해당 0을 답으로 스위칭하라는 것이었음.
// 그래서, 각 배열별로 끝부분 숫자를 가리키는 포인터를 만든 후, k 포인터를 만들어서 하나씩 더 큰숫자부터 추가해주면 됐었음.
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            }
            else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
    }
};