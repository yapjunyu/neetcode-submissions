class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        hmap = {}

        for i in range(len(s)):
            if s[i] in hmap:
                l = max(l, hmap[s[i]] + 1)
            hmap[s[i]] = i
            res = max(res, i - l + 1)
        return res