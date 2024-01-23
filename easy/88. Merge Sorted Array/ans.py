class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1 # nums1의 마지막 수 인덱스
        j = n - 1 # nums2의 마지막 수 인덱스
        k = m + n - 1 # nums1 + nums2의 마지막 수 인덱스

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]: # 아직 i 0이상이고, nums2쪽 숫자가 더 작으면 삽입
                nums1[k] = nums1[i]
                i -= 1
            else: # nums2쪽 숫자가 같거나 크면
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        