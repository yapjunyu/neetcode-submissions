class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            y = [0] * 26
            for ch in s:
                y[ord(ch) - 97] += 1
            x[tuple(y)].append(s)
        return list(x.values())