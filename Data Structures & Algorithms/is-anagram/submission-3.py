class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for i in range(len(s)):
            a[s[i]] = 1 + a.setdefault(s[i], 1)
            b[t[i]] = 1 + b.setdefault(t[i], 1)
        return a == b