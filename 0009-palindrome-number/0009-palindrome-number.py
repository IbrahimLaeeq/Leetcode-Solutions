class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False 
        ''' 
        because -121 will evaluate to 121- so no need to 
        check for negative values 
        '''
        original_no = x
        counter = 0
        '''
        doing this because we are going to be modifying the 
        original no "x"
        '''
        while x > 0:
            '''
            we are going to keep dividign the no until
            we get zero 
            '''
            counter = (counter * 10) + ( x % 10)
            '''
            counter * 10 gives us the location of the decimal 
            part i.e. 10 ^0 , 10^1 , 10^ 2
            etc

            x % 10 gives us the last no from our input integer

            '''
            x = x // 10 
            '''
            storing the remaining integers from teh x value 
            i.e. the remaining integer without the last
            value as we have included that in teh "counter
            '''
        return original_no == counter
