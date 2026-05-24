class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only lowercase so 26 unique at most
        # can start building sequence when element is in s1
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        for s in s1:
            count[ord(s) - ord('a')] += 1

        window = [0] * 26
        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if window == count:
                return True
        return False