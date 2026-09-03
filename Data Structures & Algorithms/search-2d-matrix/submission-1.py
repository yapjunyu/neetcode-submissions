class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use the first/last value of each row to create a sorted list
        # binary search based on that value to identify the specific row
        # binary search again to get the value inside the row 
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                rl, rr = 0, len(matrix[mid]) - 1
                while rl <= rr:
                    rmid = (rl + rr) // 2
                    if matrix[mid][rmid] == target:
                        return True
                    elif matrix[mid][rmid] > target:
                        rr = rmid - 1
                    else:
                        rl = rmid + 1
                return False
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        return False 