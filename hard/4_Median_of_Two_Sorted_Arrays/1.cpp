class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            nums1.swap(nums2);
        }

        int n = nums1.size();
        int m = nums2.size();
        int total = n + m;
        int half = total / 2;

        // nums1에서 왼쪽 지점에 포함되는 수의 개수 범위(0<=N<=n)
        int st = 0;
        int en = n;

        while (st <= en) {
            int mid = (st + en) / 2; // mid개 포함.
            int remain = half - mid;

            int min_n = mid >= n ? INT_MAX : nums1[mid];
            int min_m = remain >= m ? INT_MAX : nums2[remain];

            int max_n = mid <= 0 ? INT_MIN : nums1[mid - 1];
            int max_m = remain <= 0 ? INT_MIN : nums2[remain - 1];

            if (max_n <= min_m && max_m <= min_n) {
                if (total % 2 == 0) {
                    return (max(max_n, max_m) + min(min_n, min_m)) / 2.0;
                }
                return min(min_n, min_m);
            } 

            if (max_n > min_m) {
                en = mid - 1;
            }
            else if (max_m > min_n) {
                st = mid + 1;
            }
        }
        return 0;
    }
};
