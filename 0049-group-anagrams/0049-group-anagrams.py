class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []
        for s in strs:
            f = str(sorted(s))
            if f not in map:
                map[f] = []
            map[f].append(s)
        return list(map.values())        
        
