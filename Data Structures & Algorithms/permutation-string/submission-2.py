class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        window = [0] * 26
        l = 0
        for ch in s1:
            s1Count[ord(ch) - ord('a')] += 1
        for r in range(len(s2)):
            ch = s2[r]
            window[ord(ch) - ord('a')] += 1
            print(window)
            if window == s1Count:
                return True
            if r >= len(s1) - 1:
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
        