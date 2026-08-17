class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a tuple as the dictionary key
        res = []
        a = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            a[tuple(freq)].append(word)
        for val in a.values():
            res.append(val)
        return res
        