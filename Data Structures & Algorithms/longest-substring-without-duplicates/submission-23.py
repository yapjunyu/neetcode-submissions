class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store a hashmap of last index of ch
        hmap = {}
        res = 0
        l = r = 0
        while r < len(s):
            ch = s[r]
            if ch in hmap:
                l = max(hmap[ch] + 1, l)
            hmap[ch] = r
            res = max(res, r - l + 1)
            r += 1
        return res