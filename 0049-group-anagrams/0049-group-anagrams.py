class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []
        for s in strs:
            srt = str(sorted(s))
            if srt not in map:
                map[srt] = []
            map[srt].append(s)
        return list(map.values())
        '''
        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #anagram strings are after sorting the same 
        mp ={}
        
        for s in strs:
            f=str(sorted(s))
            if f not in mp:
                mp[f]=[]
            mp[f].append(s)
        return list(mp.values())
        '''
        