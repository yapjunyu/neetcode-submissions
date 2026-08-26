class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # both string only contain lowercase character
        # can use array of size 26 to count 
        freq, window = [0] * 26, [0] * 26
        l = 0
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            while r - l > len(s1) - 1:
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if window == freq:
                return True
        return False


        
        
       


