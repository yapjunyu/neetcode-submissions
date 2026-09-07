class TimeMap:
    # timing can be used for binary search?
    # {alice: [(1, happy), (3, sad)]}
    def __init__(self):
        self.hmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap.get(key, [])
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= arr[mid][0]:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


        
