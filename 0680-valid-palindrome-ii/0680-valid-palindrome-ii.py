class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        we could delete one char and store that copy
        somewhere and then run the loop condition 
        to check if this new copy could be a palindrome
        or not
        '''
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                '''
                here we can remove one value so we either
                remove the value at the left pointer or
                we reomve the vlaue at the rigth pointer
                and we use -1 to reverse the string
                '''
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True # if loop runs and dones treturn false 
