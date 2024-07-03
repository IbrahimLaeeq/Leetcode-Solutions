class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS  , countT = {} , {}
        # two hash maps
        if len(s) != len(t):
            return False
        #cannto be anagram with diff lengths
        for i in range (len(s)):
            #lengths are same so can iterate over any one
            #creating hash maps
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        if countS != countT:
            return False
        return True 
        