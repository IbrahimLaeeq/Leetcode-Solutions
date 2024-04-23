class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False

        p1 = x
        counter = 0 

        while x != 0:
            counter = (counter * 10) + (x % 10)
            x = x // 10
        return p1 == counter 
        '''
        counter % 10 gives us the last element
        counter * 10 gives us the place i.e. 10^ 0 , 10^1 , 10^2 etc
        x = x// 10 gives us the remaining digits in the original no 
        and discards the last number 
        '''