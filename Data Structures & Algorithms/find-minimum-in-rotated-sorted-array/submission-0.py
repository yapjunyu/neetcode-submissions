class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # if mid element is greater than the rightmost element,
            # the min must be to the right.
            if nums[mid] > nums[r]:
                l = mid + 1
            # else mid could be the min so keep it in range
            else:
                r = mid
                
        return nums[l]