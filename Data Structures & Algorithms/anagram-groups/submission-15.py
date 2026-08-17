class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a tuple as the dictionary key
        a = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            a[tuple(freq)].append(word)
        return list(a.values())
        