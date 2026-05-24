class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use tuple of frequency as key
        a = defaultdict(list)
        
        for s in strs:
            b = [0] * 26
            for ch in s:
                b[ord(ch) - ord('a')] += 1
            a[tuple(b)].append(s)
        return list(a.values())