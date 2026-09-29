from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        timemap = self.m[key] #sorted dict
        # 1 : cat
        # 2 : dog
        # 3 : yel

        idx = timemap.bisect_right(timestamp) - 1
        if idx >= 0:
            return timemap[timemap.keys()[idx]]

        return ""