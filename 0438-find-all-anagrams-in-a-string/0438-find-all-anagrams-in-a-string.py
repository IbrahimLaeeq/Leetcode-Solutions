class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount , sCount = {} , {}
        #iterating through "p" first
        for i in range (len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i] , 0)
            sCount[s[i]] = 1 + sCount.get(s[i] , 0)
        res = [0] if sCount == pCount else []
        # if teh anagram starts from indice zero like in case one
        l = 0
        for r in range(len(p) , len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            #adding the new ele in sliding window
            sCount[s[l]] -=1
            # removing the previous element
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+=1
            if sCount == pCount:
                res.append(l)
                # if they are equal then append teh starin left indice
        return res



        