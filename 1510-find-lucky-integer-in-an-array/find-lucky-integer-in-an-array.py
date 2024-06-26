class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {}
        for a in arr:
            if a not in hash_map:
                hash_map[a] = 1
            else:
                hash_map[a] +=1
        max_key = 0
        for key, val in hash_map.items():
            if key == val and key > max_key:
                max_key = key
        if max_key == 0:
            return -1
        return max_key