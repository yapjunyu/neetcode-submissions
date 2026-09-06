class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            
            # check if the left half is sorted
            if nums[l] <= nums[mid]:
                # check if target inside left sorted half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # means right side sorted
            else:
                # check if target inside right sorted half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1