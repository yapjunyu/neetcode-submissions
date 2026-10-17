class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialise an arr of 0 of len(nums)
        # loop back arr until k 
        res = []
        arr = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for key, val in count.items():
            arr[val].append(key)
        for item in arr[::-1]:
            for temp in item:
                res.append(temp)
                if len(res) == k:
                    return res


        