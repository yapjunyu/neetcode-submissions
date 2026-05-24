class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for _ in range(len(nums) + 1)]

        for key, val in Counter(nums).items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        