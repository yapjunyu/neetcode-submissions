class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use the have need approach
        if len(t) > len(s):
            return ""
        res = [0, 0]
        resLen = float("inf")
        l = 0
        freq = Counter(t)
        need = len(freq)
        have = 0
        match = {}
        for r in range(len(s)):
            ch = s[r]
            match[ch] = match.get(ch, 0) + 1
            if ch in freq and match[s[r]] == freq[ch]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                match[s[l]] -= 1
                if s[l] in freq and match[s[l]] < freq[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""
