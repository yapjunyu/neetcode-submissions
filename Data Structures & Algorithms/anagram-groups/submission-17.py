class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialise a default dictionary of list
        # use a tuple of frequency as hmap key
        hmap = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - ord('a')] += 1
            hmap[tuple(arr)].append(s)
        return list(hmap.values())



        