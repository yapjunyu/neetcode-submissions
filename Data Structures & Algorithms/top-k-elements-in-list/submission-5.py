class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get a count of the freq of nums
        # init array of array size n + 1 and then append the number inside
        # loop from the back of the array based on k
        res = []
        freq = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for key in freq.keys():
            arr[freq[key]].append(key)
        for item in arr[::-1]:
            for val in item:
                res.append(val)
                if len(res) == k:
                    return res
        
              