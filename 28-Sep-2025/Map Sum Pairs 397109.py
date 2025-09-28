# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        total = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total