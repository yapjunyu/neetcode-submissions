class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, replace the most frequent character in the window
        hmap = {}
        freq = 0
        l = 0
        res = 0
        for idx, val in enumerate(s):
            hmap[val] = hmap.get(val, 0) + 1
            freq = max(freq, hmap[val])
            if idx - l + 1 - freq > k:
                hmap[s[l]] -= 1
                l += 1
            # dont need to update the max freq because the freq needs to be higher to get a better res
            res = max(res, idx - l + 1)
        return res
