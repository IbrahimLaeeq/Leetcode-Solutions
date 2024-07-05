class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        have one pointer at the start and one
        pointer at the end

        checks:
        check if hte current char at left and right is
        lower case and not alpha numeric before comparing
        
        if these checks pass and they are still not equal
        then return False , other-wise , return True
        '''
        l = 0 
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l +=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
        return True
        '''
        if else is wrong bc in this case both conditions 
        can be true simulatenously i.e a char on the 
        left and right pointer could be alphanumeric
        simultaneously where if we use if-elif
        then it only processes it for one of the 
        characters

        and if all the three
        '''
        
        