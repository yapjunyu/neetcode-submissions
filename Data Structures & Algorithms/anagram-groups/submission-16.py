class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map each word as an array of frequency and use it as a key to hashmap
        hmap = defaultdict(list)
        for i in range(len(strs)):
            arr = [0] * 26
            for ch in strs[i]:
                arr[ord(ch) - ord('a')] += 1
            hmap[tuple(arr)].append(strs[i])
        res = []
        for arr in hmap.values():
            res.append(arr)
        return res
            
        
        