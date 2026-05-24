class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            if tuple(key) not in a:
                a[tuple(key)] = [s]
            else:
                a[tuple(key)].append(s)
        return list(a.values())
        