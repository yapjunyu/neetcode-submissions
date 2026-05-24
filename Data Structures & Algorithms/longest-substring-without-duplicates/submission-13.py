class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of each ch last appearance in a hmap
        # when a ch reappears, move the window to the ch previous index + 1 and update the index
        # record down the max length 
        hmap = {}
        res = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in hmap:
                l = max(hmap[ch] + 1, l)
            hmap[ch] = r
            res = max(res, r - l + 1)
        return res