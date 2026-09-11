class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2) # m is the shorter arr that will be used for the binary search
        half = (m + n + 1) // 2
        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i # the remaining elements in b
            a_left = nums1[i - 1] if i > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_left = nums2[j - 1] if j > 0 else float('-inf')
            b_right = nums2[j] if j < n else float('inf')
            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2 != 0:
                    return float(max(a_left, b_left))
                return (max(a_left, b_left) + min(b_right, a_right)) / 2.0
            else:
                if a_left > b_right:
                    r = i - 1
                else:
                    l = i + 1
             
        