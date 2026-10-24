class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window of length s1, hashmap the freq 
        if len(s1) > len(s2):
            return False
        s1arr, s2arr = [0] * 26, [0] * 26
        for ch in s1:
            s1arr[ord('a') - ord(ch)] += 1
        l, r = 0, 0
        while r < len(s2):
            s2arr[ord('a') - ord(s2[r])] += 1
            if r > len(s1) - 1:
                s2arr[ord('a') - ord(s2[l])] -= 1
                l += 1
            r += 1
            if s1arr == s2arr:
                return True
        return False

        